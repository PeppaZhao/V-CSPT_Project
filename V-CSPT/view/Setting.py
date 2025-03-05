"""
        主界面设置模块
        copyright ： CheneyZhao
        版本号 ： 1.0


"""
import os
import sys

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QSettings, QDateTime
from PyQt6.QtWidgets import QApplication, QDialog, QMessageBox, QDialogButtonBox


class SettingWindow(QDialog):

    def __init__(self):
        super(SettingWindow, self).__init__()
        self.setupUi(self)
        # 储存数据以供修改
        self.app_data = QSettings('./.inif/settingconfig.ini', QSettings.Format.IniFormat)
        # 检查是否有数据进行初始化
        if os.path.exists('./.inif/settingconfig.ini'):
            # 直接读取数据
            self.save_settingData()
        else:
            # 没有配置文件就创建配时文件进行数据初始化
            self.init_settingData()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Setting")
        Dialog.resize(408, 472)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon_main/setting.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        self.buttonBoxSettingCtro = QtWidgets.QDialogButtonBox(parent=Dialog)
        self.buttonBoxSettingCtro.setGeometry(QtCore.QRect(230, 440, 171, 32))
        self.buttonBoxSettingCtro.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBoxSettingCtro.setStandardButtons(
            QtWidgets.QDialogButtonBox.StandardButton.Apply | QtWidgets.QDialogButtonBox.StandardButton.Cancel)
        self.buttonBoxSettingCtro.setObjectName("buttonBoxSettingCtro")
        self.labelSetting_veh = QtWidgets.QLabel(parent=Dialog)
        self.labelSetting_veh.setGeometry(QtCore.QRect(40, 40, 70, 20))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.labelSetting_veh.setFont(font)
        self.labelSetting_veh.setObjectName("labelSetting_veh")
        self.lineEditSetting_vehinput = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEditSetting_vehinput.setGeometry(QtCore.QRect(160, 40, 121, 20))
        self.lineEditSetting_vehinput.setInputMask("")
        self.lineEditSetting_vehinput.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEditSetting_vehinput.setDragEnabled(False)
        self.lineEditSetting_vehinput.setObjectName("lineEditSetting_vehinput")
        self.labelSetting_vehunint = QtWidgets.QLabel(parent=Dialog)
        self.labelSetting_vehunint.setGeometry(QtCore.QRect(290, 40, 70, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.labelSetting_vehunint.setFont(font)
        self.labelSetting_vehunint.setObjectName("labelSetting_vehunint")
        self.labelSetting_weight = QtWidgets.QLabel(parent=Dialog)
        self.labelSetting_weight.setGeometry(QtCore.QRect(40, 165, 70, 20))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.labelSetting_weight.setFont(font)
        self.labelSetting_weight.setObjectName("labelSetting_weight")
        self.lineEditSetting_weightInbound = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEditSetting_weightInbound.setGeometry(QtCore.QRect(230, 150, 51, 20))
        self.lineEditSetting_weightInbound.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEditSetting_weightInbound.setObjectName("lineEditSetting_weightInbound")
        self.lineEditSetting_weightOutbound = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEditSetting_weightOutbound.setGeometry(QtCore.QRect(230, 180, 51, 20))
        self.lineEditSetting_weightOutbound.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEditSetting_weightOutbound.setObjectName("lineEditSetting_weightOutbound")
        self.labelSetting_weightInbound = QtWidgets.QLabel(parent=Dialog)
        self.labelSetting_weightInbound.setGeometry(QtCore.QRect(160, 150, 70, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.labelSetting_weightInbound.setFont(font)
        self.labelSetting_weightInbound.setObjectName("labelSetting_weightInbound")
        self.labelSetting_weightOutbound = QtWidgets.QLabel(parent=Dialog)
        self.labelSetting_weightOutbound.setGeometry(QtCore.QRect(160, 180, 70, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.labelSetting_weightOutbound.setFont(font)
        self.labelSetting_weightOutbound.setObjectName("labelSetting_weightOutbound")
        self.labelSetting_common = QtWidgets.QLabel(parent=Dialog)
        self.labelSetting_common.setGeometry(QtCore.QRect(40, 320, 81, 20))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.labelSetting_common.setFont(font)
        self.labelSetting_common.setObjectName("labelSetting_common")
        self.lineEditSetting_commonAinput = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEditSetting_commonAinput.setGeometry(QtCore.QRect(230, 240, 51, 20))
        self.lineEditSetting_commonAinput.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEditSetting_commonAinput.setObjectName("lineEditSetting_commonAinput")
        self.labelSetting_commonA = QtWidgets.QLabel(parent=Dialog)
        self.labelSetting_commonA.setGeometry(QtCore.QRect(160, 240, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.labelSetting_commonA.setFont(font)
        self.labelSetting_commonA.setObjectName("labelSetting_commonA")
        self.line = QtWidgets.QFrame(parent=Dialog)
        self.line.setGeometry(QtCore.QRect(30, 80, 331, 20))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(parent=Dialog)
        self.line_2.setGeometry(QtCore.QRect(30, 210, 331, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.labelSetting_commonB = QtWidgets.QLabel(parent=Dialog)
        self.labelSetting_commonB.setGeometry(QtCore.QRect(160, 280, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.labelSetting_commonB.setFont(font)
        self.labelSetting_commonB.setObjectName("labelSetting_commonB")
        self.lineEditSetting_commonBinput = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEditSetting_commonBinput.setGeometry(QtCore.QRect(230, 280, 51, 20))
        self.lineEditSetting_commonBinput.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEditSetting_commonBinput.setObjectName("lineEditSetting_commonBinput")
        self.labelSetting_commonG = QtWidgets.QLabel(parent=Dialog)
        self.labelSetting_commonG.setGeometry(QtCore.QRect(160, 320, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.labelSetting_commonG.setFont(font)
        self.labelSetting_commonG.setObjectName("labelSetting_commonG")
        self.lineEditSetting_commonGinput = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEditSetting_commonGinput.setGeometry(QtCore.QRect(230, 320, 51, 20))
        self.lineEditSetting_commonGinput.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEditSetting_commonGinput.setObjectName("lineEditSetting_commonGinput")
        self.labelSetting_commonT = QtWidgets.QLabel(parent=Dialog)
        self.labelSetting_commonT.setGeometry(QtCore.QRect(160, 360, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.labelSetting_commonT.setFont(font)
        self.labelSetting_commonT.setObjectName("labelSetting_commonT")
        self.lineEditSetting_commonTinput = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEditSetting_commonTinput.setGeometry(QtCore.QRect(230, 360, 51, 20))
        self.lineEditSetting_commonTinput.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEditSetting_commonTinput.setObjectName("lineEditSetting_commonTinput")
        self.labelSetting_commonM = QtWidgets.QLabel(parent=Dialog)
        self.labelSetting_commonM.setGeometry(QtCore.QRect(160, 400, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.labelSetting_commonM.setFont(font)
        self.labelSetting_commonM.setObjectName("labelSetting_commonM")
        self.lineEditSetting_commonMinput = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEditSetting_commonMinput.setGeometry(QtCore.QRect(230, 400, 51, 20))
        self.lineEditSetting_commonMinput.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEditSetting_commonMinput.setObjectName("lineEditSetting_commonMinput")
        self.labelSetting_veh_2 = QtWidgets.QLabel(parent=Dialog)
        self.labelSetting_veh_2.setGeometry(QtCore.QRect(40, 110, 70, 20))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.labelSetting_veh_2.setFont(font)
        self.labelSetting_veh_2.setObjectName("labelSetting_veh_2")
        self.labelSetting_vehunint_2 = QtWidgets.QLabel(parent=Dialog)
        self.labelSetting_vehunint_2.setGeometry(QtCore.QRect(290, 110, 70, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.labelSetting_vehunint_2.setFont(font)
        self.labelSetting_vehunint_2.setObjectName("labelSetting_vehunint_2")
        self.lineEditSetting_stop_threshold = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEditSetting_stop_threshold.setGeometry(QtCore.QRect(160, 110, 121, 20))
        self.lineEditSetting_stop_threshold.setInputMask("")
        self.lineEditSetting_stop_threshold.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEditSetting_stop_threshold.setDragEnabled(False)
        self.lineEditSetting_stop_threshold.setObjectName("lineEditSetting_stop_threshold")

        self.retranslateUi(Dialog)
        self.buttonBoxSettingCtro.accepted.connect(Dialog.accept)  # type: ignore
        self.buttonBoxSettingCtro.rejected.connect(Dialog.reject)  # type: ignore
        # # 绑定槽函数
        self.buttonBoxSettingCtro.clicked.connect(self.reSetting)

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Setting):
        _translate = QtCore.QCoreApplication.translate
        Setting.setWindowTitle(_translate("Setting", "设置"))
        self.labelSetting_veh.setText(_translate("Setting", "饱和流量"))
        self.lineEditSetting_vehinput.setText(_translate("Setting", "1800"))
        self.lineEditSetting_vehinput.setPlaceholderText(_translate("Setting", "1800"))
        self.labelSetting_vehunint.setText(_translate("Setting", "veh/lane/h"))
        self.labelSetting_weight.setText(_translate("Setting", "评价权重"))
        self.lineEditSetting_weightInbound.setText(_translate("Setting", "1"))
        self.lineEditSetting_weightInbound.setPlaceholderText(_translate("Setting", "1"))
        self.lineEditSetting_weightOutbound.setText(_translate("Setting", "1"))
        self.lineEditSetting_weightOutbound.setPlaceholderText(_translate("Setting", "1"))
        self.labelSetting_weightInbound.setText(_translate("Setting", "Inbound"))
        self.labelSetting_weightOutbound.setText(_translate("Setting", "Outbound"))
        self.labelSetting_common.setText(_translate("Setting", "无量纲常量"))
        self.lineEditSetting_commonAinput.setText(_translate("Setting", "0.85"))
        self.lineEditSetting_commonAinput.setPlaceholderText(_translate("Setting", "0.85"))
        self.labelSetting_commonA.setText(_translate("Setting", "Alpha"))
        self.labelSetting_commonB.setText(_translate("Setting", "Beta"))
        self.lineEditSetting_commonBinput.setText(_translate("Setting", "0.90"))
        self.lineEditSetting_commonBinput.setPlaceholderText(_translate("Setting", "0.9"))
        self.labelSetting_commonG.setText(_translate("Setting", "Gamma"))
        self.lineEditSetting_commonGinput.setText(_translate("Setting", "0.95"))
        self.lineEditSetting_commonGinput.setPlaceholderText(_translate("Setting", "0.95"))
        self.labelSetting_commonT.setText(_translate("Setting", "Tau"))
        self.lineEditSetting_commonTinput.setText(_translate("Setting", "1"))
        self.lineEditSetting_commonTinput.setPlaceholderText(_translate("Setting", "1"))
        self.labelSetting_commonM.setText(_translate("Setting", "Mu"))
        self.lineEditSetting_commonMinput.setText(_translate("Setting", "1"))
        self.lineEditSetting_commonMinput.setPlaceholderText(_translate("Setting", "1"))
        self.labelSetting_veh_2.setText(_translate("Setting", "停车阈值"))
        self.labelSetting_vehunint_2.setText(_translate("Setting", "km/h"))
        self.lineEditSetting_stop_threshold.setText(_translate("Setting", "5"))
        self.lineEditSetting_stop_threshold.setPlaceholderText(_translate("Setting", "5"))

    def reSetting(self, button):
        # 判断点击的是哪个btn
        # 若点击Apply则判断是否为空，为空返回默认值
        # 若点击Cancel则直接返回默认值

        if button == self.buttonBoxSettingCtro.button(QDialogButtonBox.StandardButton.Apply):
            """
            判断输入值是否为空
            :return:
            """
            # 获取输入框数据
            settingData = [self.lineEditSetting_vehinput.text(), self.lineEditSetting_weightInbound.text(),
                           self.lineEditSetting_weightOutbound.text(), self.lineEditSetting_commonAinput.text(),
                           self.lineEditSetting_commonBinput.text(), self.lineEditSetting_commonGinput.text(),
                           self.lineEditSetting_commonTinput.text(), self.lineEditSetting_commonMinput.text(),
                           self.lineEditSetting_stop_threshold.text()]
            res = any(not element.strip() for element in settingData)  # 判断是否非空
            if res:
                QMessageBox.warning(self, "系统提示", "设置输入不能为空")
                # print(settingData)  # 输出结果
                # main.Ui_MainWindow.returnData(main.Ui_MainWindow, settingData)
            else:
                # 如果非空则关闭窗口并更新配置数据
                time = QDateTime.currentDateTime()  # 获取当前时间，并存储在self.qpp_data
                self.app_data.setValue('time', time.toString())  # 数据0：time.toString()为字符串类型
                # 读取默认数据并存储
                self.app_data.setValue('LESetting_vehinput', settingData[0])
                self.app_data.setValue('LESetting_weightInbound', settingData[1])
                self.app_data.setValue('LESetting_weightOutbound', settingData[2])
                self.app_data.setValue('LESetting_commonAinput', settingData[3])
                self.app_data.setValue('LESetting_commonBinput', settingData[4])
                self.app_data.setValue('LESetting_commonGinput', settingData[5])
                self.app_data.setValue('LESetting_commonTinput', settingData[6])
                self.app_data.setValue('LESetting_commonMinput', settingData[7])
                self.app_data.setValue('LESetting_stop_threshold', settingData[8])
                self.close()
                # main.Ui_MainWindow.returnData(main.Ui_MainWindow, settingData)
                # print(settingData)  # 输出结果
        else:
            self.close()

    # 存在配时文件则读取并设置
    def save_settingData(self):
        time = self.app_data.value('time')
        # print(time)

        settingData = [self.app_data.value('LESetting_vehinput'),
                       self.app_data.value('LESetting_weightInbound'),
                       self.app_data.value('LESetting_weightOutbound'),
                       self.app_data.value('LESetting_commonAinput'),
                       self.app_data.value('LESetting_commonBinput'),
                       self.app_data.value('LESetting_commonGinput'),
                       self.app_data.value('LESetting_commonTinput'),
                       self.app_data.value('LESetting_commonMinput'),
                       self.app_data.value('LESetting_stop_threshold')
                       ]
        # 读取并设置
        self.lineEditSetting_vehinput.setText(settingData[0])
        self.lineEditSetting_weightInbound.setText(settingData[1])
        self.lineEditSetting_weightOutbound.setText(settingData[2])
        self.lineEditSetting_commonAinput.setText(settingData[3])
        self.lineEditSetting_commonBinput.setText(settingData[4])
        self.lineEditSetting_commonGinput.setText(settingData[5])
        self.lineEditSetting_commonTinput.setText(settingData[6])
        self.lineEditSetting_commonMinput.setText(settingData[7])
        self.lineEditSetting_stop_threshold.setText(settingData[8])

    # 若第一次打开则初始化
    def init_settingData(self):
        time = QDateTime.currentDateTime()  # 获取当前时间，并存储在self.qpp_data
        self.app_data.setValue('time', time.toString())  # 数据0：time.toString()为字符串类型
        # 读取默认数据并存储
        self.LESetting_vehinput = self.lineEditSetting_vehinput.placeholderText()
        self.app_data.setValue('LESetting_vehinput', self.LESetting_vehinput)
        self.LESetting_weightInbound = self.lineEditSetting_weightInbound.placeholderText()
        self.app_data.setValue('LESetting_weightInbound', self.LESetting_weightInbound)
        self.LESetting_weightOutbound = self.lineEditSetting_weightOutbound.placeholderText()
        self.app_data.setValue('LESetting_weightOutbound', self.LESetting_weightOutbound)
        self.LESetting_commonAinput = self.lineEditSetting_commonAinput.placeholderText()
        self.app_data.setValue('LESetting_commonAinput', self.LESetting_commonAinput)
        self.LESetting_commonBinput = self.lineEditSetting_commonBinput.placeholderText()
        self.app_data.setValue('LESetting_commonBinput', self.LESetting_commonBinput)
        self.LESetting_commonGinput = self.lineEditSetting_commonGinput.placeholderText()
        self.app_data.setValue('LESetting_commonGinput', self.LESetting_commonGinput)
        self.LESetting_commonTinput = self.lineEditSetting_commonTinput.placeholderText()
        self.app_data.setValue('LESetting_commonTinput', self.LESetting_commonTinput)
        self.LESetting_commonMinput = self.lineEditSetting_commonMinput.placeholderText()
        self.app_data.setValue('LESetting_commonMinput', self.LESetting_commonMinput)
        self.LESetting_stop_threshold = self.lineEditSetting_stop_threshold.placeholderText()
        self.app_data.setValue('LESetting_stop_threshold', self.LESetting_stop_threshold)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = SettingWindow()

    ui.show()

    sys.exit(app.exec())
