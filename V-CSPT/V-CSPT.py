"""
        主界面模块
        copyright ： CheneyZhao
        版本号 ： 1.0
"""
import ast
import copy
import ctypes
import os
import sys

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QSettings, QDateTime
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QWidget, QApplication, QMessageBox, QMenu

from order_set import order
from order_set.order import CSPTLIB, exit_vissim, compress_folder_except_init, selectFolder, output_result, \
    ExternalDataAnalyses
from setting import Setting, BaseData, NetData, SignalData, SimData, Result, UploadData

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")  # 将任务栏图标做更换


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.active_threads = []  # 存储活动线程
        self.task_counter = 0  # 任务计数器
        # 储存数据以供修改
        self.loadData = None
        self.upload_action = None
        self.open_action = None
        self.menu = None
        self.app_loaddata = None
        self.data_loc_file = None
        self.LoadingData = None
        self.folder_path = None
        self.resultData = None
        self.loc_file = None
        self.signalData = None
        self.simData = None
        self.SimData = None
        self.NetData = None
        self.SingalData = None
        self.netData = None
        self.baseData = None
        self.settingData = None
        self.BaseData = None
        self.Setting = None
        self.pushButtonNetdata = None
        self.pushButtonBasedata = None
        self.pushButtonSimdata = None
        self.pushButtonSignaldata = None
        self.gridLayout_2 = None
        self.pushButtonClose = None
        self.line = None
        self.pushButtonOpen = None
        self.commandLinkButton = None
        self.verticalLayout_2 = None
        self.pushButtonStart = None
        self.pValue = None
        self.progressBar = None
        self.pushButtonSetting = None
        self.label = None
        self.pushButtonSave = None
        self.pushButtonHelp = None
        self.gridLayout = None
        self.app_data = QSettings('.inif/resconfig.ini', QSettings.Format.IniFormat)
        # 输出结果
        if not os.path.exists('.inif/resconfig.ini'):
            self.init_result()
        self.setupUi(self)
        # 储存数据以供修改
        self.app_settingdata = QSettings('.inif/settingconfig.ini', QSettings.Format.IniFormat)
        self.app_netdata = QSettings('.inif/netconfig.ini', QSettings.Format.IniFormat)
        self.app_basedata = QSettings('.inif/baseconfig.ini', QSettings.Format.IniFormat)
        self.app_signaldata = QSettings('.inif/signalconfig.ini', QSettings.Format.IniFormat)
        self.app_simdata = QSettings('.inif/simconfig.ini', QSettings.Format.IniFormat)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.WindowModality.WindowModal)
        Form.setEnabled(True)
        Form.resize(1020, 530)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(1420, 730))
        Form.setMaximumSize(QtCore.QSize(16777215, 16777215))
        Form.setSizeIncrement(QtCore.QSize(0, 0))
        Form.setBaseSize(QtCore.QSize(0, 0))
        Form.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icon.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Form.setWindowIcon(icon)
        Form.setToolTipDuration(-5)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 0, 10, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButtonHelp = QtWidgets.QPushButton(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonHelp.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon_main/help.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonHelp.setIcon(icon1)
        self.pushButtonHelp.setIconSize(QtCore.QSize(18, 18))
        self.pushButtonHelp.setFlat(True)
        self.pushButtonHelp.setObjectName("pushButtonHelp")

        # 绑定槽函数
        self.pushButtonHelp.clicked.connect(self.helpOrder)

        self.gridLayout.addWidget(self.pushButtonHelp, 0, 3, 1, 1)
        self.pushButtonSave = QtWidgets.QPushButton(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonSave.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icon_main/save.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonSave.setIcon(icon2)
        self.pushButtonSave.setIconSize(QtCore.QSize(18, 18))
        self.pushButtonSave.setFlat(True)
        self.pushButtonSave.setObjectName("pushButtonSave")

        # 绑定槽函数
        self.pushButtonSave.clicked.connect(self.save_output_data)

        self.gridLayout.addWidget(self.pushButtonSave, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("view/p1.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 9, 6)
        self.pushButtonSetting = QtWidgets.QPushButton(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonSetting.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icon_main/setting.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonSetting.setIcon(icon3)
        self.pushButtonSetting.setIconSize(QtCore.QSize(18, 18))
        self.pushButtonSetting.setFlat(True)
        self.pushButtonSetting.setObjectName("pushButtonSetting")

        # 绑定槽函数
        self.pushButtonSetting.clicked.connect(self.settingOrder)

        self.gridLayout.addWidget(self.pushButtonSetting, 0, 2, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(parent=Form)
        # 设置进度条范围
        self.progressBar.setMaximum(100)
        self.progressBar.setMinimum(0)
        self.progressBar.setMinimumHeight(20)  # 设置最小高度
        self.progressBar.setMaximumHeight(20)  # 设置最大高度
        self.progressBar.setStyleSheet("""
                                        QProgressBar {
                                            border: 2px solid grey;
                                            border-radius: 5px;
                                            background-color: #FFFFFF;
                                            text-align: center;
                                        }
                                        QProgressBar::chunk {
                                            background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0,
                                                                       stop: 0 #00FF00, stop: 1 #009900);
                                        }
                                        """)
        # 配置当前进度值
        self.pValue = 0
        self.progressBar.setValue(self.pValue)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 0, 4, 1, 1)
        self.pushButtonStart = QtWidgets.QPushButton(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonStart.setFont(font)
        self.pushButtonStart.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icon_main/strart.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonStart.setIcon(icon4)
        self.pushButtonStart.setIconSize(QtCore.QSize(22, 22))
        self.pushButtonStart.setFlat(True)
        self.pushButtonStart.setToolTip("开始")
        self.pushButtonStart.setObjectName("pushButtonStart")
        self.gridLayout.addWidget(self.pushButtonStart, 0, 5, 1, 1)

        # 绑定槽函数
        self.pushButtonStart.clicked.connect(self.startAll)

        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, 10, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(parent=Form)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.commandLinkButton.setFont(font)
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.verticalLayout_2.addWidget(self.commandLinkButton)

        # 绑定槽函数
        self.commandLinkButton.clicked.connect(self.returnResult)

        self.gridLayout.addLayout(self.verticalLayout_2, 11, 9, 1, 1)
        self.pushButtonOpen = QtWidgets.QPushButton(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonOpen.setFont(font)
        self.pushButtonOpen.setAutoFillBackground(False)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icon_main/open.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonOpen.setIcon(icon5)
        self.pushButtonOpen.setIconSize(QtCore.QSize(18, 18))
        self.pushButtonOpen.setCheckable(False)
        self.pushButtonOpen.setAutoDefault(False)
        self.pushButtonOpen.setDefault(False)
        self.pushButtonOpen.setFlat(True)
        self.pushButtonOpen.setObjectName("pushButtonOpen")
        # 绑定槽函数
        # 创建一个 QMenu 对象
        self.menu = QMenu(self)
        # 创建两个 QAction 对象
        self.open_action = QAction("打开文件", self)
        self.upload_action = QAction("上传数据", self)
        # 将 QAction 添加到 QMenu 中
        self.menu.addAction(self.open_action)
        self.menu.addAction(self.upload_action)
        # 设置按钮的菜单
        self.pushButtonOpen.setMenu(self.menu)
        # 设置按钮的样式表，隐藏下拉箭头
        self.pushButtonOpen.setStyleSheet("QPushButton::menu-indicator { image: none; }")
        # 为 QAction 绑定槽函数
        self.open_action.triggered.connect(self.open_file)
        self.upload_action.triggered.connect(self.upload_data)

        self.gridLayout.addWidget(self.pushButtonOpen, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(parent=Form)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 7)
        # self.pushButtonClose = QtWidgets.QPushButton(parent=Form)
        # font = QtGui.QFont()
        # font.setPointSize(10)
        # self.pushButtonClose.setFont(font)
        # self.pushButtonClose.setText("")
        # icon6 = QtGui.QIcon()
        # icon6.addPixmap(QtGui.QPixmap("icon_main/close.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        # self.pushButtonClose.setIcon(icon6)
        # self.pushButtonClose.setIconSize(QtCore.QSize(22, 22))
        # self.pushButtonClose.setFlat(True)
        # self.pushButtonClose.setToolTip("关闭当前进程")
        # self.pushButtonClose.setObjectName("pushButtonClose")
        # self.gridLayout.addWidget(self.pushButtonClose, 0, 6, 1, 1)
        #
        # # 绑定槽函数
        # self.pushButtonClose.clicked.connect(self.closeAll)

        spacerItem = QtWidgets.QSpacerItem(50, 60, QtWidgets.QSizePolicy.Policy.Minimum,
                                           QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout.addItem(spacerItem, 6, 7, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.gridLayout_2.setHorizontalSpacing(50)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButtonSignaldata = QtWidgets.QPushButton(parent=Form)
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(28)
        self.pushButtonSignaldata.setFont(font)
        self.pushButtonSignaldata.setObjectName("pushButtonSignaldata")
        self.gridLayout_2.addWidget(self.pushButtonSignaldata, 5, 0, 1, 1)

        # 绑定槽函数
        self.pushButtonSignaldata.clicked.connect(self.signalData_inputOrder)

        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 2, 0, 1, 1)
        self.pushButtonSimdata = QtWidgets.QPushButton(parent=Form)
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(28)
        self.pushButtonSimdata.setFont(font)
        self.pushButtonSimdata.setObjectName("pushButtonSimdata")
        self.gridLayout_2.addWidget(self.pushButtonSimdata, 7, 0, 1, 1)

        # 绑定槽函数
        self.pushButtonSimdata.clicked.connect(self.simData_inputOrder)

        self.pushButtonBasedata = QtWidgets.QPushButton(parent=Form)
        self.pushButtonBasedata.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(28)
        self.pushButtonBasedata.setFont(font)
        self.pushButtonBasedata.setAutoFillBackground(False)
        self.pushButtonBasedata.setObjectName("pushButtonBasedata")

        # 绑定槽函数
        self.pushButtonBasedata.clicked.connect(self.baseData_inputOrder)

        self.gridLayout_2.addWidget(self.pushButtonBasedata, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 4, 0, 1, 1)
        self.pushButtonNetdata = QtWidgets.QPushButton(parent=Form)
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(28)
        self.pushButtonNetdata.setFont(font)
        self.pushButtonNetdata.setObjectName("pushButtonNetdata")
        self.gridLayout_2.addWidget(self.pushButtonNetdata, 3, 0, 1, 1)

        # 绑定槽函数
        self.pushButtonNetdata.clicked.connect(self.netData_inputOrder)

        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 0, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem4, 6, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 5, 7, 1, 3)
        self.label.raise_()
        self.pushButtonOpen.raise_()
        self.line.raise_()
        self.pushButtonSave.raise_()
        self.pushButtonSetting.raise_()
        self.pushButtonHelp.raise_()
        self.pushButtonStart.raise_()
        # self.pushButtonClose.raise_()
        self.progressBar.raise_()

        self.retranslateUi(Form)
        self.progressBar.valueChanged['int'].connect(self.commandLinkButton.show)  # type: ignore
        # 未完成任务之前隐藏
        # self.commandLinkButton.setHidden(True)

        # 绑定槽函数
        self.commandLinkButton.clicked.connect(self.resultWindow)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "V-CSPT"))
        self.pushButtonHelp.setText(_translate("Form", "帮助"))
        self.pushButtonSave.setText(_translate("Form", "保存"))
        self.pushButtonSetting.setText(_translate("Form", "设置"))
        self.commandLinkButton.setText(_translate("Form", "轨迹图及评价结果"))
        self.pushButtonOpen.setText(_translate("Form", "打开"))
        self.pushButtonSignaldata.setText(_translate("Form", "配时数据"))
        self.pushButtonSimdata.setText(_translate("Form", "仿真数据"))
        self.pushButtonBasedata.setText(_translate("Form", "基础数据"))
        self.pushButtonNetdata.setText(_translate("Form", "路网数据"))

    # 设置菜单槽函数
    def settingOrder(self):
        self.Setting = Setting.SettingWindow()
        self.Setting.show()

    # 设置读取文件位置槽函数
    def open_file(self):
        self.loc_file = order.selectFile('INP文件(*.inp *.in0)')  # 文件位置
        # print(self.loc_file)

    # 从外部导入数据
    def upload_data(self):
        self.LoadingData = UploadData.UpLoadData()
        self.LoadingData.show()

    def helpOrder(self):
        # 检查文件是否存在
        file_path = 'doc'
        if os.path.exists(file_path):
            os.startfile(file_path)
        else:
            QMessageBox.critical(self, "系统提示", "文件不存在！")

    # 设置基础数据输入槽函数
    def baseData_inputOrder(self):
        self.BaseData = BaseData.BaseDataWindow()
        self.BaseData.show()

    # 设置路网数据输入槽函数
    def netData_inputOrder(self):
        self.NetData = NetData.NetDataWindow()
        self.NetData.show()

    def signalData_inputOrder(self):
        self.SingalData = SignalData.SingalDataWindow()
        self.SingalData.show()

    # 设置仿真数据输入槽函数
    def simData_inputOrder(self):
        self.SimData = SimData.SimDataWindow()
        self.SimData.show()

    def resultWindow(self):
        self.resultData = Result.ResultWindow()
        self.resultData.show()

    # def returnData(self, Data):
    #     print("回调参数", Data)

    # 运行VIS-SIM以获取数据分析数据
    def run_Vissim(self):

        if os.path.exists('.inif/settingconfig.ini'):
            # 读取数据
            self.settingData = [self.app_settingdata.value(i) for i in
                                ['LESetting_vehinput', 'LESetting_weightInbound', 'LESetting_weightOutbound',
                                 'LESetting_commonAinput', 'LESetting_commonBinput', 'LESetting_commonGinput',
                                 'LESetting_commonTinput', 'LESetting_commonMinput', 'LESetting_stop_threshold']]

        if os.path.exists('.inif/baseconfig.ini'):
            self.baseData = [self.app_basedata.value(i) for i in
                             ['LEgreenspeedinput', 'LElimspeedinput', 'LEvehVolumes_Ininput', 'LEvehVolumes_Outinput']]

        if os.path.exists('.inif/netconfig.ini'):
            self.netData = [self.app_netdata.value(i) for i in
                            ['LEnetnumIninput', 'LEnetnumOutinput', 'LEphasesIninput', 'LEphasesOutinput',
                             'LEsidelanenumInput']]

        if os.path.exists('.inif/signalconfig.ini'):
            self.signalData = [self.app_signaldata.value(i) for i in
                               ['LEsingalnumIninput', 'LEsingalnumOutinput', 'LEsingalnumLIninput',
                                'LEsingalnumLOutinput']]

        if os.path.exists('.inif/simconfig.ini'):
            self.simData = [self.app_simdata.value(i) for i in
                            ['LESimperiod', 'LEBottime', 'LEtrishowinput', 'LEDertaseed', 'LESeedinterval']]

        # 先读取储存数据,格式正确进行数据输入，格式不对则输出错误标识
        # 若返回值存在为空，则弹出错误标识
        if self.loc_file is None:
            QMessageBox.critical(self, "系统提示", "未选择路网文件（in0 & inp）！")
        elif len(self.loc_file) != 2:
            QMessageBox.critical(self, "系统提示", "缺少路网文件（in0 or inp）！")
        elif self.baseData == ['示例：55', '示例：60', '示例：[836, 1258, 1456, 968]', '示例：[836, 1258, 1456, 968]']:
            QMessageBox.critical(self, "系统提示", "基础数据未输入！")
        elif self.netData == ['示例：[1, 10001, 2, 10035, 12, 10009, 13, 17, 10012, 18, 10014, 19]',
                              '示例：[52, 10074, 48, 10032, 49, 10033, 50, 10067, 28, 10020, 29, 10021, 30]',
                              '示例：[lead, lag, lag, lead]', '示例：[lead, lag, lag, lead]', '示例：[6, 8, 8, 4]']:
            QMessageBox.critical(self, "系统提示", "路网数据未输入！")
        elif self.netData == ['示例：[1, 10001, 2, 10035, 12, 10009, 13, 17, 10012, 18, 10014, 19]',
                              '示例：[52, 10074, 48, 10032, 49, 10033, 50, 10067, 28, 10020, 29, 10021, 30]',
                              '示例：[lead, lag, lag, lead]', '示例：[lead, lag, lag, lead]', '示例：[6, 8, 8, 4]']:
            QMessageBox.critical(self, "系统提示", "路网数据未输入！")
        elif self.signalData == ['示例：[[5, 2], [5, 18], [5, 46], [4, 65]]',
                                 '示例：[[2, 57], [1, 27], [1, 1], [2, 4]]',
                                 '示例：[[1, 1], [2, 220], [2, 33], [1, 54]]',
                                 '示例：[[5, 67], [6, 47], [6, 20], [6, 6]]']:
            QMessageBox.critical(self, "系统提示", "配时数据数据未输入！")
        elif self.simData == ['示例：3600', '示例：600', '示例：[1800, 2500]', '示例：10', '示例：[10, 100]']:
            QMessageBox.critical(self, "系统提示", "仿真数据未输入！")
        else:
            self.pushButtonStart.setDisabled(True)
            '''
            调用csptlib
            LoadNet_name, LoadLayout_name, link_num_inbound, link_num_outbound, period=period,
                                   seed_input=seed_input, step=step)
            '''
            constants = [ast.literal_eval(i) for i in self.settingData]  # 无量纲常量、 路线权重、饱和车流量、停车阈值与限速
            cspt = CSPTLIB([constants[3:8], constants[1:3], constants[0], constants[8], int(self.baseData[0])])

            # 数据准备
            cspt.process_data(self.loc_file[1], self.loc_file[0],
                              ast.literal_eval(self.netData[0]), ast.literal_eval(self.netData[1]),
                              ast.literal_eval(self.netData[2]), ast.literal_eval(self.netData[3]),
                              ast.literal_eval(self.signalData[0]), ast.literal_eval(self.signalData[1]),
                              ast.literal_eval(self.signalData[2]), ast.literal_eval(self.signalData[3]))
            # 采集数据
            period, seed_input, step = int(self.simData[0]), ast.literal_eval(self.simData[4]), int(self.simData[3])
            seed = self.creat_seed(seed_input, step)
            progress_value = int(95 / len(seed))
            # 用for 循环作next迭代器 更新进度
            for _ in cspt.initial_getdata(ast.literal_eval(self.netData[0]), ast.literal_eval(self.netData[1]),
                                          period, seed_input, step):
                self.progressBarvalue(progress_value)

            # 输出数据
            cspt.output_data()
            # 绘制图像
            '''
                link_num_inbound, link_num_outbound,
                phase_inbound, phase_outbound,
                SignalHeads_num_inbound, SignalHeads_num_outbound,
                SignalHeads_num_inboundL, SignalHeads_num_outboundL, 
                gw_speed, period, show_interval
            '''
            cspt.initial_transplotlib(ast.literal_eval(self.netData[0]), ast.literal_eval(self.netData[1]),
                                      ast.literal_eval(self.netData[2]), ast.literal_eval(self.netData[3]),
                                      ast.literal_eval(self.signalData[0]), ast.literal_eval(self.signalData[1]),
                                      ast.literal_eval(self.signalData[2]), ast.literal_eval(self.signalData[3]),
                                      int(self.baseData[0]), period, ast.literal_eval(self.simData[2]))
            # 评价干线协调性能
            '''
            SignalHeads_num_outbound, SignalHeads_num_inboundL, phase_inbound,
                                  SignalHeads_num_inbound, SignalHeads_num_outboundL, phase_outbound,
                                  inter_traffic_volume, ari_traffic_volume, lane_side
            输出结果：
                inbound_grade_set = [in_ave_speed, inbound_ave_aip_score, 
                                        inbound_ave_aus_score, in_grade, in_description]
                outbound_grade_set = [out_ave_speed, outbound_ave_aip_score, 
                                        outbound_ave_aus_score, out_grade, out_description]
                ratio = [self.in_POG, self.out_POG, self.ari_POG, 
                self.ari_stop_percent, self.in_stop_percent, self.out_stop_percent]
                arterial_veh = [self.in_num_veh, self.out_num_veh]
                stop_num = [self.in_num_of_stops, self.out_num_of_stops]
                ari_grade, ari_description, inbound_grade_set, outbound_grade_set = per.output_performance_grade()
            '''
            ratio, arterial_veh, stop_num, ari_grade, ari_description, \
                inbound_grade_set, outbound_grade_set \
                = cspt.initial_performance_grade((ast.literal_eval(self.baseData[2]),
                                                  ast.literal_eval(self.baseData[3])),
                                                 (ast.literal_eval(self.baseData[2])[0],
                                                  ast.literal_eval(self.baseData[3])[-1]),
                                                 ast.literal_eval(self.netData[4]))
            # 输出结果
            self.save_result(ratio, stop_num, arterial_veh, inbound_grade_set, outbound_grade_set, ari_grade,
                             ari_description)

            output_result(ratio, stop_num, arterial_veh, inbound_grade_set, outbound_grade_set, ari_grade,
                          ari_description)

            self.progressBar.setValue(99)  # 更新进度至100%
            # 退出VIS-SIM
            exit_vissim()
            self.progressBar.setValue(100)  # 更新进度至100%
            self.pushButtonStart.setDisabled(False)  # 全部执行结束打开开始按钮

    # 获取轨迹图显示区间
    @staticmethod
    def get_show_interval():
        if os.path.exists('.inif/simconfig.ini'):
            app_simdata = QSettings('.inif/simconfig.ini', QSettings.Format.IniFormat)
            if app_simdata.value('LEtrishowinput') != '':
                return ast.literal_eval(app_simdata.value('LEtrishowinput'))
            else:
                return [1800, 2500]
        else:
            return [1800, 2500]

    @staticmethod
    def convert_load_data(LoadData):
        global converted
        load_data = [None] * len(LoadData)
        for i, item in enumerate(LoadData):
            try:
                # 使用ast安全转换数据结构
                converted = ast.literal_eval(item)
            except (SyntaxError, ValueError):
                # 特殊处理带括号的元组字符串（如："(1, 2)"）
                try:
                    converted = ast.literal_eval(item.strip("()"))
                    if isinstance(converted, list):  # 处理"([1,2], [3,4])"的情况
                        converted = tuple(converted)
                except:
                    converted = item  # 无法转换则保留原字符串
            finally:
                load_data[i] = converted
        return load_data

    # 运行External以获取数据分析数据
    def run_External(self):
        self.pushButtonStart.setDisabled(True)
        if os.path.exists('.inif/settingconfig.ini'):
            # 读取数据
            self.settingData = [self.app_settingdata.value(i) for i in
                                ['LESetting_vehinput', 'LESetting_weightInbound', 'LESetting_weightOutbound',
                                 'LESetting_commonAinput', 'LESetting_commonBinput', 'LESetting_commonGinput',
                                 'LESetting_commonTinput', 'LESetting_commonMinput', 'LESetting_stop_threshold']]
        # 读取数据
        index_input = ['cycle_input', 'offset_input', 'inbound_phase_input',
                       'outbound_phase_input', 'signal_RG1_input',
                       'signal_RG2_input', 'green_speed_input',
                       'collect_data_period_input', 'arterial_length_input',
                       'side_lanenum_input',
                       'arterial_lanenum_input', 'veh_volumes_input',
                       'inboundinter_loc_input', 'outboundinter_loc_input']
        text_input = ["示例：[148, 148, 148]", "示例：[0, 56, 15]", "示例：['lead', 'lead', 'lead']",
                      "示例：['lag', 'lead', 'lag']",
                      "示例：{'yr1': [...], 'green1': [...], 'yr2': [...], 'green2': [...], 'red': ...]}",
                      "示例：{'yr1': [...], 'green1': [...], 'yr2': [...], 'green2': [...], 'red': ...]}",
                      '示例：50', '示例：3600', '示例：2500', "示例：[6, 10, 10]", "示例：([3, 6, 8], [3, 7, 7])",
                      "示例：([1311, 866, 1430], [1480, 1788, 1012])", "示例：[154.42, 1271.24, 1998.41]",
                      "示例：[202.49, 1347.52, 2083.13]"]
        LoadData = [self.app_loaddata.value(i) for i in index_input]
        show_interval = self.get_show_interval()
        if text_input != LoadData:
            self.progressBarvalue(10)
            self.loadData = self.convert_load_data(LoadData)
            '''
            调用csptlib.External，分析数据
            LoadNet_name, LoadLayout_name, link_num_inbound, link_num_outbound, period=period,
                                   seed_input=seed_input, step=step)
            '''
            constants = [ast.literal_eval(i) for i in self.settingData]  # 无量纲常量、 路线权重、饱和车流量、停车阈值
            # 限速 = 绿波速度
            extAnalyses = ExternalDataAnalyses(self.loadData, show_interval, [constants[3:8], constants[1:3],
                                                                              constants[0], constants[8]])
            # 获取文件扩展名并转为小写
            res = extAnalyses.get_trajectory_pkl(self.data_loc_file, ['inbound', 'outbound'])
            self.progressBarvalue(10)

            if res is None:
                QMessageBox.critical(self, "系统提示", "轨迹数据文件格式不统一！")
                self.pushButtonStart.setDisabled(False)
                return None
            extAnalyses.initial_transplotlib()  # 绘图
            self.progressBarvalue(30)
            extAnalyses.output_data()  # 输出数据
            ratio, arterial_veh, stop_num, ari_grade, ari_description, \
                inbound_grade_set, outbound_grade_set = extAnalyses.initial_performance_grade()  # 评价
            # 输出结果
            self.progressBarvalue(30)
            self.save_result(ratio, stop_num, arterial_veh, inbound_grade_set, outbound_grade_set, ari_grade,
                             ari_description)

            output_result(ratio, stop_num, arterial_veh, inbound_grade_set, outbound_grade_set, ari_grade,
                          ari_description)
            self.progressBarvalue(20)

        else:
            QMessageBox.critical(self, "系统提示", "未输入分析数据！")
        if os.path.exists('./.inif/loaddataconfig.ini'):
            app_loaddata = QSettings('.inif/loaddataconfig.ini', QSettings.Format.IniFormat)
            app_loaddata.setValue('inbound_trajectory_file_loc', '')
            app_loaddata.setValue('outbound_trajectory_file_loc', '')

        self.pushButtonStart.setDisabled(False)

        return True

    def startAll(self):
        """
        加一个判断函数
        if input Data:
            run External
        else:
            run Vissim
        """
        # 提取导入数据
        if os.path.exists('.inif/loaddataconfig.ini'):
            self.app_loaddata = QSettings('.inif/loaddataconfig.ini', QSettings.Format.IniFormat)
            self.data_loc_file = [self.app_loaddata.value('inbound_trajectory_file_loc'),
                                  self.app_loaddata.value('outbound_trajectory_file_loc')]
        # 判断运行方式
        if self.loc_file is not None:
            self.progressBar.setValue(0)  # 更新进度至100%
            self.run_Vissim()
        elif self.data_loc_file is not None:
            if os.path.exists(self.data_loc_file[0]) and os.path.exists(self.data_loc_file[1]):
                self.progressBar.setValue(0)  # 更新进度至100%
                res = self.run_External()
                if res is None:
                    QMessageBox.warning(self, "系统提示", "数据输入有误！")
            elif os.path.exists(self.data_loc_file[0]):
                QMessageBox.warning(self, "系统提示", "下行轨迹数据文件(.csv or .pkl)不存在！")
            elif os.path.exists(self.data_loc_file[1]):
                QMessageBox.warning(self, "系统提示", "上行轨迹数据文件(.csv or .pkl)不存在！")
            else:
                QMessageBox.warning(self, "系统提示", "轨迹数据文件(.csv or .pkl)不存在！")

        else:
            QMessageBox.critical(self, "系统提示", "未选择评价文件！")

    # 终止一切进程
    @staticmethod
    def closeAll():
        exit_vissim()

    # 存在配时文件则读取并设置
    def save_result(self, ratio, stop_num, arterial_veh, inbound_grade_set, outbound_grade_set, ari_grade,
                    ari_description):
        time = self.app_data.value('time')
        print(time)

        resultData = [ratio,
                      stop_num,
                      arterial_veh,
                      inbound_grade_set,
                      outbound_grade_set,
                      ari_grade,
                      ari_description
                      ]
        resultDataTepy = ['', '', '', '', '', '', '']
        if resultData != resultDataTepy:
            self.app_data.setValue('ratio', str(resultData[0]))
            self.app_data.setValue('stop_num', str(resultData[1]))
            self.app_data.setValue('arterial_veh', str(resultData[2]))
            self.app_data.setValue('inbound_grade_set', str(resultData[3]))
            self.app_data.setValue('outbound_grade_set', str(resultData[4]))
            self.app_data.setValue('ari_grade', str(resultData[5]))
            self.app_data.setValue('ari_description', str(resultData[6]))

    # 若第一次打开则初始化
    def init_result(self):

        time = QDateTime.currentDateTime()  # 获取当前时间，并存储在self.qpp_data
        self.app_data.setValue('time', time.toString())  # 数据0：time.toString()为字符串类型
        # 读取默认数据并存储
        '''
        输出结果：

            ratio = [self.in_POG, self.out_POG, self.ari_POG,
            self.ari_stop_percent, self.in_stop_percent, self.in_stop_percent]
            arterial_veh = [self.in_num_veh, self.out_num_veh]
            stop_num = [self.in_num_of_stops, self.out_num_of_stops]
            inbound_grade_set = [in_ave_speed, inbound_ave_aip_score, 
                        inbound_ave_aus_score, in_grade, in_description]
            outbound_grade_set = [out_ave_speed, outbound_ave_aip_score, 
                        outbound_ave_aus_score, out_grade, out_description]
            ari_grade, ari_description, inbound_grade_set, outbound_grade_set = per.output_performance_grade()
        '''
        self.app_data.setValue('ratio', """['None', 'None', 'None', 'None', 'None', 'None']""")
        self.app_data.setValue('stop_num', """['None', 'None']""")
        self.app_data.setValue('arterial_veh', """['None', 'None']""")
        self.app_data.setValue('inbound_grade_set', """['None', 'None', 'None', 'None', 'None']""")
        self.app_data.setValue('outbound_grade_set', """['None', 'None', 'None', 'None', 'None']""")
        self.app_data.setValue('ari_grade', """['None']""")
        self.app_data.setValue('ari_description', """['None']""")

    # 生成种子列表
    @staticmethod
    def creat_seed(seed_input: list, step: int) -> list:
        if len(seed_input) == 2:
            return [i for i in range(seed_input[0], seed_input[1] + 1, step)]
        else:
            return copy.deepcopy(seed_input)

    def progressBarvalue(self, progress_value: int):
        self.pValue += progress_value
        self.progressBar.setValue(self.pValue)

    def returnResult(self):
        # 将进度条设置值归0
        self.pValue = 0
        self.progressBar.setValue(0)
        # 显示评估结果窗口
        # self.evluResult = evluResult.evluResultWindow()
        # self.evluResult.show()

    # 导出结果
    @staticmethod
    def save_output_data():
        output_path = selectFolder()
        if output_path is not None:
            compress_folder_except_init(output_path[0])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MainWindow()

    ui.show()

    sys.exit(app.exec())
