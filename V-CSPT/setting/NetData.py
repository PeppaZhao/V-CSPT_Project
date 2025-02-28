"""
        主界面路网数据输入模块
        copyright ： CheneyZhao
        版本号 ： 1.0

"""
import os
import sys
from PyQt6.QtCore import QSettings, QDateTime
from PyQt6.QtWidgets import QApplication, QDialog, QDialogButtonBox, QMessageBox
from PyQt6 import QtCore, QtGui, QtWidgets


class NetDataWindow(QDialog):

    def __init__(self):
        super(NetDataWindow, self).__init__()
        self.LEsidelanenumInput = None
        self.LEphasesOutinput = None
        self.LEphasesIninput = None
        self.LEnetnumOutinput = None
        self.LEnetnumIninput = None
        self.buttonBox_NetDataCtro = None
        self.line_5 = None
        self.lineEdit__sidelanenumInput = None
        self.label_sidelanenum = None
        self.label_phasesOut = None
        self.label_phasesIn = None
        self.label_phases = None
        self.lineEdit_phasesIninput = None
        self.lineEdit_phasesOutinput = None
        self.label_netnumOut = None
        self.lineEdit_netnumOutinput = None
        self.lineEdit_netnumIninput = None
        self.label_netnumIn = None
        self.label_netnum = None
        self.line_4 = None
        self.setupUi(self)
        # 储存数据以供修改
        self.app_data = QSettings('./.inif/netconfig.ini', QSettings.Format.IniFormat)
        # 检查是否有数据进行初始化
        if os.path.exists('./.inif/netconfig.ini'):
            # 直接读取数据
            self.save_netData()
        else:
            # 没有配置文件就创建配时文件进行数据初始化
            self.init_netData()

    def setupUi(self, NetData):
        NetData.setObjectName("NetData")
        NetData.resize(792, 528)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icon_sub/netdata.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        NetData.setWindowIcon(icon)
        self.line_4 = QtWidgets.QFrame(parent=NetData)
        self.line_4.setGeometry(QtCore.QRect(30, 180, 721, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_netnum = QtWidgets.QLabel(parent=NetData)
        self.label_netnum.setGeometry(QtCore.QRect(30, 30, 101, 20))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label_netnum.setFont(font)
        self.label_netnum.setObjectName("label_netnum")
        self.label_netnumIn = QtWidgets.QLabel(parent=NetData)
        self.label_netnumIn.setGeometry(QtCore.QRect(30, 80, 70, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_netnumIn.setFont(font)
        self.label_netnumIn.setObjectName("label_netnumIn")
        self.lineEdit_netnumIninput = QtWidgets.QLineEdit(parent=NetData)
        self.lineEdit_netnumIninput.setGeometry(QtCore.QRect(100, 80, 671, 21))
        self.lineEdit_netnumIninput.setText("")
        self.lineEdit_netnumIninput.setMaxLength(50000)
        self.lineEdit_netnumIninput.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_netnumIninput.setObjectName("lineEdit_netnumIninput")
        self.lineEdit_netnumOutinput = QtWidgets.QLineEdit(parent=NetData)
        self.lineEdit_netnumOutinput.setGeometry(QtCore.QRect(100, 140, 671, 20))
        self.lineEdit_netnumOutinput.setText("")
        self.lineEdit_netnumOutinput.setMaxLength(50000)
        self.lineEdit_netnumOutinput.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_netnumOutinput.setObjectName("lineEdit_netnumOutinput")
        self.label_netnumOut = QtWidgets.QLabel(parent=NetData)
        self.label_netnumOut.setGeometry(QtCore.QRect(30, 140, 70, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_netnumOut.setFont(font)
        self.label_netnumOut.setObjectName("label_netnumOut")
        self.lineEdit_phasesOutinput = QtWidgets.QLineEdit(parent=NetData)
        self.lineEdit_phasesOutinput.setGeometry(QtCore.QRect(100, 320, 671, 20))
        self.lineEdit_phasesOutinput.setText("")
        self.lineEdit_phasesOutinput.setMaxLength(50000)
        self.lineEdit_phasesOutinput.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_phasesOutinput.setObjectName("lineEdit_phasesOutinput")
        self.lineEdit_phasesIninput = QtWidgets.QLineEdit(parent=NetData)
        self.lineEdit_phasesIninput.setGeometry(QtCore.QRect(100, 250, 671, 20))
        self.lineEdit_phasesIninput.setText("")
        self.lineEdit_phasesIninput.setMaxLength(50000)
        self.lineEdit_phasesIninput.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_phasesIninput.setObjectName("lineEdit_phasesIninput")
        self.label_phases = QtWidgets.QLabel(parent=NetData)
        self.label_phases.setGeometry(QtCore.QRect(30, 210, 101, 20))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label_phases.setFont(font)
        self.label_phases.setObjectName("label_phases")
        self.label_phasesIn = QtWidgets.QLabel(parent=NetData)
        self.label_phasesIn.setGeometry(QtCore.QRect(30, 250, 70, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_phasesIn.setFont(font)
        self.label_phasesIn.setObjectName("label_phasesIn")
        self.label_phasesOut = QtWidgets.QLabel(parent=NetData)
        self.label_phasesOut.setGeometry(QtCore.QRect(30, 320, 70, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_phasesOut.setFont(font)
        self.label_phasesOut.setObjectName("label_phasesOut")
        self.line_5 = QtWidgets.QFrame(parent=NetData)
        self.line_5.setGeometry(QtCore.QRect(30, 370, 721, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_5.setObjectName("line_5")
        self.label_sidelanenum = QtWidgets.QLabel(parent=NetData)
        self.label_sidelanenum.setGeometry(QtCore.QRect(30, 420, 91, 20))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label_sidelanenum.setFont(font)
        self.label_sidelanenum.setObjectName("label_sidelanenum")
        self.lineEdit__sidelanenumInput = QtWidgets.QLineEdit(parent=NetData)
        self.lineEdit__sidelanenumInput.setGeometry(QtCore.QRect(140, 420, 591, 20))
        self.lineEdit__sidelanenumInput.setText("")
        self.lineEdit__sidelanenumInput.setMaxLength(50000)
        self.lineEdit__sidelanenumInput.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit__sidelanenumInput.setObjectName("lineEdit__sidelanenumInput")
        self.buttonBox_NetDataCtro = QtWidgets.QDialogButtonBox(parent=NetData)
        self.buttonBox_NetDataCtro.setGeometry(QtCore.QRect(610, 490, 171, 32))
        self.buttonBox_NetDataCtro.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox_NetDataCtro.setStandardButtons(
            QtWidgets.QDialogButtonBox.StandardButton.Apply | QtWidgets.QDialogButtonBox.StandardButton.Cancel)
        self.buttonBox_NetDataCtro.setObjectName("buttonBox_NetDataCtro")

        self.retranslateUi(NetData)
        self.buttonBox_NetDataCtro.accepted.connect(NetData.accept)  # type: ignore
        self.buttonBox_NetDataCtro.rejected.connect(NetData.reject)  # type: ignore
        # 获取 Apply 按钮并设置中文文本
        self.buttonBox_NetDataCtro.button(QtWidgets.QDialogButtonBox.StandardButton.Apply).setText("应用")
        self.buttonBox_NetDataCtro.button(QtWidgets.QDialogButtonBox.StandardButton.Apply).setDefault(True)
        # 获取 Cancel 按钮并设置中文文本
        self.buttonBox_NetDataCtro.button(QtWidgets.QDialogButtonBox.StandardButton.Cancel).setText("取消")
        # 绑定槽函数
        self.buttonBox_NetDataCtro.clicked.connect(self.reSetting)

        QtCore.QMetaObject.connectSlotsByName(NetData)

    def retranslateUi(self, NetData):
        _translate = QtCore.QCoreApplication.translate
        NetData.setWindowTitle(_translate("NetData", "路网数据"))
        self.label_netnum.setText(_translate("NetData", "干线道路编号"))
        self.label_netnumIn.setText(_translate("NetData", "上行"))
        self.lineEdit_netnumIninput.setPlaceholderText(
            _translate("NetData", "示例：[1, 10001, 2, 10035, 12, 10009, 13, 17, 10012, 18, 10014, 19]"))
        self.lineEdit_netnumOutinput.setPlaceholderText(
            _translate("NetData", "示例：[52, 10074, 48, 10032, 49, 10033, 50, 10067, 28, 10020, 29, 10021, 30]"))
        self.label_netnumOut.setText(_translate("NetData", "下行"))
        self.lineEdit_phasesOutinput.setPlaceholderText(_translate("NetData", "示例：['lead', 'lag', 'lag', 'lead']"))
        self.lineEdit_phasesIninput.setPlaceholderText(_translate("NetData", "示例：['lead', 'lag', 'lag', 'lead']"))
        self.label_phases.setText(_translate("NetData", "相序设置"))
        self.label_phasesIn.setText(_translate("NetData", "上行"))
        self.label_phasesOut.setText(_translate("NetData", "下行"))
        self.label_sidelanenum.setText(_translate("NetData", "侧街车道数"))
        self.lineEdit__sidelanenumInput.setPlaceholderText(_translate("NetData", "示例：[6, 8, 8, 4]"))

    def reSetting(self, button):
        # 判断点击的是哪个btn
        # 获取输入框数据
        netData = [self.lineEdit_netnumIninput.text(), self.lineEdit_netnumOutinput.text(),
                   self.lineEdit_phasesIninput.text(), self.lineEdit_phasesOutinput.text(),
                   self.lineEdit__sidelanenumInput.text()]

        if button == self.buttonBox_NetDataCtro.button(QDialogButtonBox.StandardButton.Apply):
            """
            判断输入值是否为空
            :return:
            """

            res = any(not element.strip() for element in netData)  # 判断是否非空
            if res:
                QMessageBox.warning(self, "系统提示", "输入不能为空！")
            else:

                are_all_lists = all(isinstance(eval(item, {"__builtins__": {}}, {}), list) for item in netData)
                # 如果非空且格式正确则关闭窗口并更新配置数据
                if are_all_lists:
                    time = QDateTime.currentDateTime()  # 获取当前时间，并存储在self.qpp_data
                    self.app_data.setValue('time', time.toString())  # 数据0：time.toString()为字符串类型
                    # 读取默认数据并存储
                    self.app_data.setValue('LEnetnumIninput', netData[0])
                    self.app_data.setValue('LEnetnumOutinput', netData[1])
                    self.app_data.setValue('LEphasesIninput', netData[2])
                    self.app_data.setValue('LEphasesOutinput', netData[3])
                    self.app_data.setValue('LEsidelanenumInput', netData[4])
                    self.close()
                else:
                    QMessageBox.warning(self, "系统提示", "数据格式有误！")
        else:
            self.close()

    # 存在配时文件则读取并设置
    def save_netData(self):
        time = self.app_data.value('time')
        print(time)

        baseData = [self.app_data.value('LEnetnumIninput'),
                    self.app_data.value('LEnetnumOutinput'),
                    self.app_data.value('LEphasesIninput'),
                    self.app_data.value('LEphasesOutinput'),
                    self.app_data.value('LEsidelanenumInput')]
        baseDataTepy = [self.lineEdit_netnumIninput.placeholderText(),
                        self.lineEdit_netnumOutinput.placeholderText(),
                        self.lineEdit_phasesIninput.placeholderText(),
                        self.lineEdit_phasesOutinput.placeholderText(),
                        self.lineEdit__sidelanenumInput.placeholderText()]
        if baseData != baseDataTepy:
            self.lineEdit_netnumIninput.setText(baseData[0])
            self.lineEdit_netnumOutinput.setText(baseData[1])
            self.lineEdit_phasesIninput.setText(baseData[2])
            self.lineEdit_phasesOutinput.setText(baseData[3])
            self.lineEdit__sidelanenumInput.setText(baseData[4])

    # 若第一次打开则初始化
    def init_netData(self):
        time = QDateTime.currentDateTime()  # 获取当前时间，并存储在self.qpp_data
        self.app_data.setValue('time', time.toString())  # 数据0：time.toString()为字符串类型
        # 读取默认数据并存储
        self.LEnetnumIninput = self.lineEdit_netnumIninput.placeholderText()
        self.app_data.setValue('LEnetnumIninput', self.LEnetnumIninput)

        self.LEnetnumOutinput = self.lineEdit_netnumOutinput.placeholderText()
        self.app_data.setValue('LEnetnumOutinput', self.LEnetnumOutinput)

        self.LEphasesIninput = self.lineEdit_phasesIninput.placeholderText()
        self.app_data.setValue('LEphasesIninput', self.LEphasesIninput)

        self.LEphasesOutinput = self.lineEdit_phasesOutinput.placeholderText()
        self.app_data.setValue('LEphasesOutinput', self.LEphasesOutinput)

        self.LEsidelanenumInput = self.lineEdit__sidelanenumInput.placeholderText()
        self.app_data.setValue('LEsidelanenumInput', self.LEsidelanenumInput)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = NetDataWindow()
    ui.show()
    sys.exit(app.exec())
