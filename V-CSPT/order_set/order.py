"""

    作者 : CheneyZhao
    用途 ： 用于执行菜单栏按键

"""
import os
import shutil

import win32com.client as com
from PyQt6.QtCore import QDateTime, QSettings
from PyQt6.QtWidgets import QFileDialog

from csptlib.datastore import load_variavle
from csptlib.getdata import GetVisTrajectoryData, ExternalTrajectoryData
from csptlib.systrajectorylib.ratedata import RateData
from csptlib.systrajectorylib.rateperformance import output_average_speed, output_stop_delay, \
    RateCoordinationPerformance, output_POG, output_stop_percent
from csptlib.transplotlib import *


# 选择文件
def selectFile(file_format: str) -> list:
    # 存在配时文件则读取并设置
    def save_fileloc(file_loc_s: str):
        # time = app_data.value('time')
        file_loc_type = 'c:\\'
        if file_loc_s != file_loc_type:
            app_data.setValue('file_loc', file_loc_s)

    # 若第一次打开则初始化
    def init_fileloc():
        time = QDateTime.currentDateTime()  # 获取当前时间，并存储在self.qpp_data
        app_data.setValue('time', time.toString())  # 数据0：time.toString()为字符串类型
        app_data.setValue('file_loc', 'c:\\')

    app_data = QSettings('./.inif/file_location.ini', QSettings.Format.IniFormat)
    # 检查是否有数据进行初始化
    if os.path.exists('./.inif/file_location.ini'):
        # 直接读取数据
        file_loc = app_data.value('file_loc')
    else:
        # 没有配置文件就创建配时文件进行数据初始化
        init_fileloc()
        file_loc = app_data.value('file_loc')

    fd = QFileDialog()
    fd.setFileMode(QFileDialog.FileMode.ExistingFiles)  # 设置多选
    if os.path.exists(file_loc):
        fd.setDirectory(file_loc)  # 设置初始化路径
    else:
        # 没有地址打开C盘
        fd.setDirectory('c:\\')  # 设置初始化路径

    fd.setNameFilter(file_format)
    if fd.exec():
        loc = fd.selectedFiles()
        save_fileloc(os.path.dirname(loc[0]))
    else:
        loc = None
    return loc


# 选择保存路径
def selectFolder() -> list:
    fd = QFileDialog()
    fd.setFileMode(QFileDialog.FileMode.Directory)  # 设置选择文件夹模式
    fd.setDirectory('c:\\')  # 设置初始化路径
    if fd.exec():
        loc = fd.selectedFiles()
    else:
        loc = None

    return loc


def output_result(ratio, stop_num, arterial_veh, inbound_grade_set, outbound_grade_set, ari_grade, ari_description):
    """
    输出结果：
        inbound_grade_set = [in_ave_speed, inbound_ave_aip_score,
                                inbound_ave_aus_score, in_grade, in_description]
        outbound_grade_set = [out_ave_speed, outbound_ave_aip_score,
                                outbound_ave_aus_score, out_grade, out_description]
        ratio = [self.in_POG, self.out_POG, self.ari_POG,
                    self.ari_stop_percent, self.in_stop_percent, self.in_stop_percent]
        arterial_veh = [self.in_num_veh, self.out_num_veh]
        stop_num = [self.in_num_of_stops, self.out_num_of_stops]
        ari_grade, ari_description, inbound_grade_set, outbound_grade_set = per.output_performance_grade()
    """
    # 定义文件内容
    content = f"""
    ===================================================
    \n
    上行方向平均停车次数为：{stop_num[0]} 次
    上行方向通过干线车辆数为：{arterial_veh[0]} 辆
    上行方向平均停车率为：{ratio[4]} %
    上行方向平均绿灯到达率为：{ratio[0]} %
    上行方向干线车辆平均速度为：{inbound_grade_set[0]} km/h
    上行方向AIP Score为：{inbound_grade_set[1]} /100
    上行方向AUS Score为：{inbound_grade_set[2]} /100
    上行方向干线协调性能评估等级为：{inbound_grade_set[3]} 
    {inbound_grade_set[4]} 
    \n
    ===================================================
    \n
    下行方向平均停车次数为：{stop_num[1]} 次
    下行方向通过干线车辆数为：{arterial_veh[1]} 辆
    下行方向平均停车率为：{ratio[5]} %
    下行方向平均绿灯到达率为：{ratio[1]} %
    下行方向干线车辆平均速度为：{outbound_grade_set[0]} km/h
    下行方向AIP Score为：{outbound_grade_set[1]} /100
    下行方向AUS Score为：{outbound_grade_set[2]} /100
    下行方向干线协调性能评估等级为：{outbound_grade_set[3]} 
    {outbound_grade_set[4]} 
    \n
    ===================================================
    \n
    干线协调性能等级为：{ari_grade}
    {ari_description}
    """

    # 创建文件并写入内容
    file_path = './csptlib/res/arterial_coordination_performance.txt'
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

    # print(f"文件已成功创建在：{file_path}")


# 导出数据
def compress_folder_except_init(output_path: str):
    folder_path = './csptlib/res/'
    output_path = f'{output_path}/performance_data.zip'

    """
    打包压缩某个文件夹下除init文件夹之外的所有文件进行保存

    Args:
        folder_path (str): 要压缩的文件夹路径
        output_path (str): 压缩文件的输出路径（包括文件名和后缀，如.zip）
    """
    # 检查文件夹路径是否存在
    if not os.path.exists(folder_path):
        # print(f"文件夹路径 '{folder_path}' 不存在")
        return

    # 检查输出路径的后缀是否为.zip
    if not output_path.endswith('.zip'):
        # print(f"输出路径 '{output_path}' 的后缀应为.zip")
        return

    # 创建一个临时文件夹用于存放需要压缩的文件
    temp_folder = 'temp_folder_for_compression'
    os.makedirs(temp_folder, exist_ok=True)

    # 遍历原文件夹下的所有文件和文件夹
    for root, dirs, files in os.walk(folder_path):
        # 跳过init文件夹
        if 'init' in dirs:
            dirs.remove('init')

        # 复制文件到临时文件夹
        for file in files:
            if file.endswith('.pkl'):
                continue  # 跳过.pkl文件
            file_path = os.path.join(root, file)
            # 计算文件在临时文件夹中的相对路径
            rel_path = os.path.relpath(file_path, folder_path)
            temp_file_path = os.path.join(temp_folder, rel_path)
            # 创建文件夹（如果不存在）
            os.makedirs(os.path.dirname(temp_file_path), exist_ok=True)
            # 复制文件
            shutil.copy2(file_path, temp_file_path)

    # 使用shutil.make_archive进行打包压缩临时文件夹
    # print(temp_folder)
    try:
        shutil.make_archive(output_path.replace('.zip', ''), 'zip', temp_folder)
        # print(f"文件夹 '{folder_path}'（除init文件夹外）已成功压缩为 '{output_path}'")
    except Exception as e:
        # print(f"压缩文件夹时出错：{e}")
        return e
    finally:
        # 删除临时文件夹
        shutil.rmtree(temp_folder)


def exit_vissim():
    Vissim = com.Dispatch("VISSIM.vissim.430")
    Vissim.Exit()


# 调用cspt用于采集轨迹数据
class CSPTLIB:

    # 实例化
    def __init__(self, constants: list):
        """
        constants: # 无量纲常量、 路线权重、饱和车流量、停车阈值与限速
        """
        self.dimensionless_constants, self.rount_weight, \
            self.saturation_veh, self.stop_speed_threshold, self.lim_speed = constants
        self.ari_stop_percent = None
        self.out_stop_percent = None
        self.in_stop_percent = None
        self.ari_POG = None
        self.out_POG = None
        self.in_POG = None
        self.out_num_veh = None
        self.out_num_of_stops = None
        self.in_num_veh = None
        self.in_num_of_stops = None
        self.ari_signal_plan_ring2 = None
        self.ari_signal_plan_ring1 = None
        self.offset = None
        self.cycle = None
        self.controllers_num = None
        self.outbound_rate_data = None
        self.inbound_rate_data = None
        self.outbound_trajectorydata = None
        self.inbound_trajectorydata = None
        self.inter_location_outbound = None
        self.inter_lane_num_outbound = None
        self.inter_lane_num_inbound = None
        self.inter_location_inbound = None
        self.arterial_length = None
        self.inter_lane_outbound = None
        self.inter_loc_outbound = None
        self.inter_lane_inbound = None
        self.inter_loc_inbound = None
        self.LoadLayout_name = None
        self.LoadNet_name = None

    # 数据准备
    def process_data(self, LoadNet_name, LoadLayout_name,
                     link_num_inbound, link_num_outbound,
                     phase_inbound, phase_outbound,
                     SignalHeads_num_inbound, SignalHeads_num_outbound,
                     SignalHeads_num_inboundL, SignalHeads_num_outboundL):
        # 读取数据
        # 读取交叉口位置、车道数
        self.LoadNet_name, self.LoadLayout_name = [x.replace('/', '\\') for x in [LoadNet_name, LoadLayout_name]]
        datas = AterialDataCollection(self.LoadNet_name, self.LoadLayout_name)
        self.inter_location_inbound, \
            self.inter_lane_num_inbound = datas.loc_arterial_intersection(link_num_inbound, SignalHeads_num_inbound,
                                                                          'inbound')
        self.inter_location_outbound, \
            self.inter_lane_num_outbound = datas.loc_arterial_intersection(link_num_outbound, SignalHeads_num_outbound,
                                                                           'outbound')
        self.arterial_length = datas.lane_length(link_num_outbound)
        self.controllers_num, self.cycle, self.offset = datas.get_controller()
        # 读取配时方案
        self.ari_signal_plan_ring1 = datas.get_signalplan(SignalHeads_num_outbound, SignalHeads_num_inboundL,
                                                          phase_inbound)
        self.ari_signal_plan_ring2 = datas.get_signalplan(SignalHeads_num_inbound, SignalHeads_num_outboundL,
                                                          phase_outbound)

    # 采集数据
    def initial_getdata(self, link_num_inbound: list, link_num_outbound: list,
                        period: int, seed: list, step: int):
        """
        用于获取轨迹数据
        LoadNet_name: 路网名称
        LoadLayout_name：布局文件名称
        link_num_inbound：上行方向路段编号
        link_num_outbound：下行方向路段编号
        seed：随机种子
        period：仿真周期时长
        """
        # 初始化路网所需数据

        getdata = GetVisTrajectoryData(self.LoadNet_name, self.LoadLayout_name, link_num_inbound, link_num_outbound,
                                       seed=seed, period=period, step=step)
        # 用for 循环作next迭代器
        for i in getdata.get_vis_trajectorydata():
            yield i

        self.inbound_trajectorydata = load_variavle('csptlib\\res\\inbound_trajectorydata.pkl')
        self.outbound_trajectorydata = load_variavle('csptlib\\res\\outbound_trajectorydata.pkl')

    # 输出数据
    def output_data(self):
        """
        用于输出数据
        """
        # 输出评价数据
        RD = RateData(self.inbound_trajectorydata, self.inter_location_inbound, self.stop_speed_threshold)
        self.inbound_rate_data = RD.output_rate_data()
        RD = RateData(self.outbound_trajectorydata, self.inter_location_outbound,
                      self.stop_speed_threshold, self.arterial_length)
        self.outbound_rate_data = RD.output_rate_data()
        # 存储评价数据
        inbound_rate_data = save_variable(self.inbound_rate_data, 'inbound_rate_data', '.\\csptlib\\res')
        outbound_rate_data = save_variable(self.outbound_rate_data, 'outbound_rate_data', '.\\csptlib\\res')
        # 输出速度
        output_average_speed(inbound_rate_data, 'inbound_ave_speed', '.\\csptlib\\res')
        output_average_speed(outbound_rate_data, 'outbound_ave_speed', '.\\csptlib\\res')
        # 输出延误
        self.in_num_of_stops, self.in_num_veh = output_stop_delay(inbound_rate_data, len(self.inter_location_inbound),
                                                                  'inbound_delay', '.\\csptlib\\res')
        self.out_num_of_stops, self.out_num_veh = output_stop_delay(outbound_rate_data,
                                                                    len(self.inter_location_outbound),
                                                                    'outbound_delay', '.\\csptlib\\res')

    # 绘制轨迹图
    def _tra(self, link_num_inbound, link_num_outbound,
             phase_inbound, phase_outbound,
             SignalHeads_num_inbound, SignalHeads_num_outbound,
             SignalHeads_num_inboundL, SignalHeads_num_outboundL, gw_speed, period, show_interval):
        tra = SignalPlanPlot(self.LoadNet_name, self.LoadLayout_name,
                             link_num_inbound, link_num_outbound,
                             phase_inbound, phase_outbound,
                             SignalHeads_num_inbound, SignalHeads_num_outbound,
                             SignalHeads_num_inboundL, SignalHeads_num_outboundL, gw_speed=gw_speed, period=period)
        tra.plot_signal_plan(band_text=(True, show_interval[0]))
        # 绘制轨迹
        tra.plot_trajectories(self.inbound_trajectorydata, self.outbound_trajectorydata)
        tra.set_show_lim(xlim=show_interval)
        transplt.savefig('csptlib\\res\\trajectory_diagram.png', format='png')
        transplt.close('all')

    # 绘制普渡图
    def _pu(self, phase_inbound, phase_outbound):
        pu = PurduePlot(cycle=self.cycle, offset=self.offset, arterial_length=self.arterial_length)
        pu.inter_location_inbound = self.inter_location_inbound
        pu.inter_location_outbound = self.inter_location_outbound
        pu.inbound_tradata = self.inbound_trajectorydata
        pu.outbound_tradata = self.outbound_trajectorydata
        # 读取配时方案
        pu.ari_signal_plan_ring1 = self.ari_signal_plan_ring1
        pu.ari_signal_plan_ring2 = self.ari_signal_plan_ring2
        pu.phase_inbound = phase_inbound
        pu.phase_outbound = phase_outbound
        self.purdue_inbound, self.purdue_outbound, self.inbound_BOG_EOG, self.outbound_BOG_EOG = pu.plot_purdue(
            title_language="C")

    # 绘制图像
    def initial_transplotlib(self, link_num_inbound: list, link_num_outbound: list,
                             phase_inbound: list, phase_outbound: list,
                             SignalHeads_num_inbound: list, SignalHeads_num_outbound: list,
                             SignalHeads_num_inboundL: list, SignalHeads_num_outboundL: list,
                             gw_speed: int, period: int, show_interval: list):
        """
        用于初始化图像绘制
        """
        # 输入数据

        self.inbound_trajectorydata = load_variavle('csptlib\\res\\inbound_trajectorydata.pkl')
        self.outbound_trajectorydata = load_variavle('csptlib\\res\\outbound_trajectorydata.pkl')
        # 绘制轨迹图
        self._tra(link_num_inbound, link_num_outbound,
                  phase_inbound, phase_outbound,
                  SignalHeads_num_inbound, SignalHeads_num_outbound,
                  SignalHeads_num_inboundL, SignalHeads_num_outboundL, gw_speed, period, show_interval)
        # 绘制普渡图
        self._pu(phase_inbound, phase_outbound)

    def initial_performance_grade(self, inter_traffic_volume, ari_traffic_volume, lane_side):
        """
        用于初始化评级
        """
        ratedata = (self.inbound_rate_data, self.outbound_rate_data)
        inter_location = (self.inter_location_inbound, self.inter_location_outbound)
        per = RateCoordinationPerformance(ratedata, inter_location, inter_traffic_volume, ari_traffic_volume,
                                          (self.inter_lane_num_inbound, self.inter_lane_num_outbound),
                                          lane_side, saturation_flow_rate=self.saturation_veh, lim_speed=self.lim_speed,
                                          dimensionless_constants=self.dimensionless_constants,
                                          weight=self.rount_weight)
        per.cycle = self.cycle
        per.ari_signal_plan_ring1 = self.ari_signal_plan_ring1
        per.ari_signal_plan_ring2 = self.ari_signal_plan_ring2
        '''
        # 返回评估数据
        inbound_grade_set = [in_ave_speed, inbound_ave_aip_score, inbound_ave_aus_score, in_grade, in_description]
        outbound_grade_set = [out_ave_speed, outbound_ave_aip_score, outbound_ave_aus_score, out_grade, out_description]
        '''
        self.in_POG = output_POG(self.purdue_inbound, self.inbound_BOG_EOG)
        self.out_POG = output_POG(self.purdue_outbound, self.outbound_BOG_EOG)
        self.ari_POG = (self.in_POG + self.out_POG) / 2
        # print('Average POG is：', (self.in_POG + self.out_POG) / 2)

        self.in_stop_percent = output_stop_percent(self.inter_location_inbound, self.inbound_trajectorydata,
                                                   self.stop_speed_threshold)
        self.out_stop_percent = output_stop_percent(self.inter_location_outbound, self.outbound_trajectorydata,
                                                    self.stop_speed_threshold)
        self.ari_stop_percent = (self.in_stop_percent + self.out_stop_percent) / 2
        # print('average stop percent is：', (self.in_stop_percent + self.out_stop_percent) / 2)
        ratio = [self.in_POG, self.out_POG, self.ari_POG,
                 self.ari_stop_percent, self.in_stop_percent, self.out_stop_percent]
        arterial_veh = [self.in_num_veh, self.out_num_veh]
        stop_num = [self.in_num_of_stops, self.out_num_of_stops]
        ari_grade, ari_description, inbound_grade_set, outbound_grade_set = per.output_performance_grade()

        return ratio, arterial_veh, stop_num, ari_grade, ari_description, inbound_grade_set, outbound_grade_set


# 外部数据导入分析
class ExternalDataAnalyses:
    def __init__(self, loadData: list, show_interval: list, constants: list):
        """
        :param loadData: 导入数据
                       'cycle_input', 'offset_input', 'inbound_phase_input',
                       'outbound_phase_input', 'signal_RG1_input',
                       'signal_RG2_input', 'green_speed_input',
                       'collect_data_period_input', 'arterial_length_input',
                       'side_lanenum_input',
                       'arterial_lanenum_input', 'veh_volumes_input',
                       'inboundinter_loc_input', 'outboundinter_loc_input'
        :param show_interval: 轨迹图显示区间
        """
        super().__init__()
        """
        constants: # 无量纲常量、 路线权重、饱和车流量、停车阈值与限速
        """
        self.dimensionless_constants, self.rount_weight, \
            self.saturation_veh, self.stop_speed_threshold = constants
        self.ari_stop_percent = None
        self.out_stop_percent = None
        self.in_stop_percent = None
        self.ari_POG = None
        self.out_POG = None
        self.in_POG = None
        self.lane_side = loadData[9]
        self.inter_lane_num_outbound = loadData[10][1]
        self.inter_lane_num_inbound = loadData[10][0]
        self.ari_traffic_volume = (loadData[11][0][0], loadData[11][1][-1])
        self.inter_traffic_volume = loadData[11]
        self.show_interval = show_interval
        self.ari_signal_plan_ring = [loadData[4], loadData[5]]
        self.cycle = loadData[0]
        self.offset = loadData[1]
        self.phase = [loadData[2], loadData[3]]
        self.gw_speed = loadData[6]
        self.lim_speed = loadData[6]
        self.period = loadData[7]
        self.out_num_veh = None
        self.out_num_of_stops = None
        self.in_num_veh = None
        self.in_num_of_stops = None
        self.outbound_rate_data = None
        self.inbound_rate_data = None
        self.arterial_length = loadData[8]
        self.inter_location_outbound = loadData[12]
        self.inter_location_inbound = loadData[13]
        self.inbound_trajectorydata = None
        self.outbound_trajectorydata = None

    # 使用.csv文件导出.pkl文件以进行数据分析
    def get_trajectory_pkl(self, filename: list, direction: list):
        """
        外部导入轨迹数据输出评价数据及轨迹pkl文件，用于绘图
        :param filename: 轨迹文件名，csv文件
        :param direction: 轨迹方向，标识符 -> inbound and outbound
        """
        ext_file = [os.path.splitext(filename[0])[1].lower(), os.path.splitext(filename[1])[1].lower()]
        if ext_file == ['.csv', '.csv']:
            ext = ExternalTrajectoryData(filename[0], direction[0])
            self.inbound_trajectorydata = ext.sys_trajectory()
            ext = ExternalTrajectoryData(filename[1], direction[1])
            self.outbound_trajectorydata = ext.sys_trajectory()
        elif ext_file == ['.pkl', '.pkl']:
            self.inbound_trajectorydata = load_variavle(filename[0])
            self.outbound_trajectorydata = load_variavle(filename[1])
        else:
            return None
        return True

    # 输出评价数据
    # 输出数据
    def output_data(self):
        """
        用于输出数据
        """
        # 输出评价数据
        RD = RateData(self.inbound_trajectorydata, self.inter_location_inbound, self.stop_speed_threshold)
        self.inbound_rate_data = RD.output_rate_data()
        RD = RateData(self.outbound_trajectorydata, self.inter_location_outbound, self.stop_speed_threshold,
                      self.arterial_length)
        self.outbound_rate_data = RD.output_rate_data()
        # 存储评价数据
        inbound_rate_data = save_variable(self.inbound_rate_data, 'inbound_rate_data', '.\\csptlib\\res')
        outbound_rate_data = save_variable(self.outbound_rate_data, 'outbound_rate_data', '.\\csptlib\\res')
        # 输出速度
        output_average_speed(inbound_rate_data, 'inbound_ave_speed', '.\\csptlib\\res')
        output_average_speed(outbound_rate_data, 'outbound_ave_speed', '.\\csptlib\\res')
        # 输出延误
        self.in_num_of_stops, self.in_num_veh = output_stop_delay(inbound_rate_data, len(self.inter_location_inbound),
                                                                  'inbound_delay', '.\\csptlib\\res')
        self.out_num_of_stops, self.out_num_veh = output_stop_delay(outbound_rate_data,
                                                                    len(self.inter_location_outbound),
                                                                    'outbound_delay', '.\\csptlib\\res')

    # 绘制轨迹图
    def _internal_tra(self):
        tra = SignalPlanPlot()
        tra.period = self.period
        tra.gw_speed = self.gw_speed
        tra.arterial_length = self.arterial_length
        tra.phase_inbound, tra.phase_outbound = self.phase[0], self.phase[1]
        tra.controllers_num, tra.cycle, tra.offset = len(self.phase[0]), self.cycle, self.offset
        tra.inter_location_inbound, tra.inter_location_outbound = self.inter_location_inbound, \
            self.inter_location_outbound
        tra.ari_signal_plan_ring1 = self.ari_signal_plan_ring[0]
        tra.ari_signal_plan_ring2 = self.ari_signal_plan_ring[1]
        Load = AterialDataCollection()
        tra.ari_signal_plan_ring1_color = Load.set_signal_color(self.phase[0], controllers_num=len(self.phase[0]))
        tra.ari_signal_plan_ring2_color = Load.set_signal_color(self.phase[1], controllers_num=len(self.phase[0]))
        tra.ari_signal_plan_ring1_hatch = Load.set_left_signal_hatch(self.phase[0], controllers_num_=len(self.phase[0]))
        tra.ari_signal_plan_ring2_hatch = Load.set_left_signal_hatch(self.phase[1], controllers_num_=len(self.phase[0]))
        tra.plot_signal_plan(band_text=(True, self.show_interval[0]))
        tra.set_show_lim(xlim=self.show_interval)

        # 绘制轨迹
        tra.plot_trajectories(self.inbound_trajectorydata, self.outbound_trajectorydata)

        transplt.savefig('csptlib\\res\\trajectory_diagram.png', format='png')
        transplt.close('all')

    # 绘制普渡图
    def _pu(self):
        pu = PurduePlot(cycle=self.cycle, offset=self.offset, arterial_length=self.arterial_length)
        pu.inter_location_inbound = self.inter_location_inbound
        pu.inter_location_outbound = self.inter_location_outbound
        pu.inbound_tradata = self.inbound_trajectorydata
        pu.outbound_tradata = self.outbound_trajectorydata
        # 读取配时方案
        pu.ari_signal_plan_ring1 = self.ari_signal_plan_ring[0]
        pu.ari_signal_plan_ring2 = self.ari_signal_plan_ring[1]
        pu.phase_inbound = self.phase[0]
        pu.phase_outbound = self.phase[1]
        self.purdue_inbound, self.purdue_outbound, self.inbound_BOG_EOG, self.outbound_BOG_EOG = pu.plot_purdue(
            title_language="C")

    # 绘制图像
    def initial_transplotlib(self):
        """
        用于初始化图像绘制
        """
        # 输入数据

        # self.inbound_trajectorydata = load_variavle('csptlib\\res\\inbound_trajectorydata.pkl')
        # self.outbound_trajectorydata = load_variavle('csptlib\\res\\outbound_trajectorydata.pkl')
        # 绘制轨迹图
        self._internal_tra()
        # 绘制普渡图
        self._pu()

    def initial_performance_grade(self):
        """
        用于初始化评级
        """
        ratedata = (self.inbound_rate_data, self.outbound_rate_data)
        inter_location = (self.inter_location_inbound, self.inter_location_outbound)
        per = RateCoordinationPerformance(ratedata, inter_location, self.inter_traffic_volume, self.ari_traffic_volume,
                                          (self.inter_lane_num_inbound, self.inter_lane_num_outbound), self.lane_side,
                                          saturation_flow_rate=self.saturation_veh, lim_speed=self.lim_speed,
                                          dimensionless_constants=self.dimensionless_constants,
                                          weight=self.rount_weight)
        per.cycle = self.cycle
        per.ari_signal_plan_ring1 = self.ari_signal_plan_ring[0]
        per.ari_signal_plan_ring2 = self.ari_signal_plan_ring[1]
        '''
        # 返回评估数据
        inbound_grade_set = [in_ave_speed, inbound_ave_aip_score, inbound_ave_aus_score, in_grade, in_description]
        outbound_grade_set = [out_ave_speed, outbound_ave_aip_score, outbound_ave_aus_score, out_grade, out_description]
        '''
        self.in_POG = output_POG(self.purdue_inbound, self.inbound_BOG_EOG)
        self.out_POG = output_POG(self.purdue_outbound, self.outbound_BOG_EOG)
        self.ari_POG = (self.in_POG + self.out_POG) / 2
        # print('Average POG is：', (self.in_POG + self.out_POG) / 2)

        self.in_stop_percent = output_stop_percent(self.inter_location_inbound, self.inbound_trajectorydata,
                                                   self.stop_speed_threshold)
        self.out_stop_percent = output_stop_percent(self.inter_location_outbound, self.outbound_trajectorydata,
                                                    self.stop_speed_threshold)
        self.ari_stop_percent = (self.in_stop_percent + self.out_stop_percent) / 2
        # print('average stop percent is：', (self.in_stop_percent + self.out_stop_percent) / 2)

        ratio = [self.in_POG, self.out_POG, self.ari_POG,
                 self.ari_stop_percent, self.in_stop_percent, self.out_stop_percent]
        arterial_veh = [self.in_num_veh, self.out_num_veh]
        stop_num = [self.in_num_of_stops, self.out_num_of_stops]
        ari_grade, ari_description, inbound_grade_set, outbound_grade_set = per.output_performance_grade()

        return ratio, arterial_veh, stop_num, ari_grade, ari_description, inbound_grade_set, outbound_grade_set
