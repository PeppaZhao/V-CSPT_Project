"""
        主界面基础数据获取模块
        copyright ： CheneyZhao
        版本号 ： 1.0


"""
import os
import sys
from PyQt6.QtCore import QSettings, QDateTime
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QDialog, QDialogButtonBox, QMessageBox
from PyQt6 import QtCore, QtGui, QtWidgets


class BaseDataWindow(QDialog):
    def __init__(self):
        super(BaseDataWindow, self).__init__()
        self.LEvehVolumes_Outinput = None
        self.LEvehVolumes_Ininput = None
        self.LElimspeedinput = None
        self.LEgreenspeedinput = None
        self.labell_vehVolumes_Outunint = None
        self.label_vehVolumes_Out = None
        self.lineEditl_vehVolumes_Outinput = None
        self.label_vehVolumes_In = None
        self.lineEdit_vehVolumes_Ininput = None
        self.line_3 = None
        self.label_vehVolumes_Inunint = None
        self.label_vehVolumes = None
        self.label_limspeed_2 = None
        self.label_limspeedunint = None
        self.lineEdit_limspeedinput = None
        self.label_greenspeedunint = None
        self.lineEdit_greenspeedinput = None
        self.buttonBox_BaseDataCtro = None
        self.label_greenspeed = None
        self.setupUi(self)
        # 储存数据以供修改
        self.app_data = QSettings('./.inif/baseconfig.ini', QSettings.Format.IniFormat)
        # 检查是否有数据进行初始化
        if os.path.exists('./.inif/baseconfig.ini'):
            # 直接读取数据
            self.save_baseData()
        else:
            # 没有配置文件就创建配时文件进行数据初始化
            self.init_baseData()

    def setupUi(self, BaseData):
        BaseData.setObjectName("BaseData")
        BaseData.resize(407, 317)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icon_sub/basedata.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        BaseData.setWindowIcon(icon)
        self.label_greenspeed = QtWidgets.QLabel(parent=BaseData)
        self.label_greenspeed.setGeometry(QtCore.QRect(20, 40, 101, 20))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label_greenspeed.setFont(font)
        self.label_greenspeed.setObjectName("label_greenspeed")
        self.buttonBox_BaseDataCtro = QtWidgets.QDialogButtonBox(parent=BaseData)
        self.buttonBox_BaseDataCtro.setGeometry(QtCore.QRect(230, 280, 171, 32))
        self.buttonBox_BaseDataCtro.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox_BaseDataCtro.setStandardButtons(
            QtWidgets.QDialogButtonBox.StandardButton.Apply | QtWidgets.QDialogButtonBox.StandardButton.Cancel)
        self.buttonBox_BaseDataCtro.setObjectName("buttonBox_BaseDataCtro")

        # 获取 Apply 按钮并设置中文文本
        self.buttonBox_BaseDataCtro.button(QtWidgets.QDialogButtonBox.StandardButton.Apply).setText("应用")
        self.buttonBox_BaseDataCtro.button(QtWidgets.QDialogButtonBox.StandardButton.Apply).setDefault(True)
        # 获取 Cancel 按钮并设置中文文本
        self.buttonBox_BaseDataCtro.button(QtWidgets.QDialogButtonBox.StandardButton.Cancel).setText("取消")

        self.lineEdit_greenspeedinput = QtWidgets.QLineEdit(parent=BaseData)
        self.lineEdit_greenspeedinput.setGeometry(QtCore.QRect(160, 40, 121, 20))
        self.lineEdit_greenspeedinput.setInputMask("")
        self.lineEdit_greenspeedinput.setText("")
        self.lineEdit_greenspeedinput.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_greenspeedinput.setDragEnabled(False)
        self.lineEdit_greenspeedinput.setObjectName("lineEdit_greenspeedinput")
        self.label_greenspeedunint = QtWidgets.QLabel(parent=BaseData)
        self.label_greenspeedunint.setGeometry(QtCore.QRect(290, 40, 70, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_greenspeedunint.setFont(font)
        self.label_greenspeedunint.setObjectName("label_greenspeedunint")
        self.lineEdit_limspeedinput = QtWidgets.QLineEdit(parent=BaseData)
        self.lineEdit_limspeedinput.setGeometry(QtCore.QRect(160, 90, 121, 20))
        self.lineEdit_limspeedinput.setInputMask("")
        self.lineEdit_limspeedinput.setText("")
        self.lineEdit_limspeedinput.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_limspeedinput.setDragEnabled(False)
        self.lineEdit_limspeedinput.setObjectName("lineEdit_limspeedinput")
        self.label_limspeedunint = QtWidgets.QLabel(parent=BaseData)
        self.label_limspeedunint.setGeometry(QtCore.QRect(290, 90, 70, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_limspeedunint.setFont(font)
        self.label_limspeedunint.setObjectName("label_limspeedunint")
        self.label_limspeed_2 = QtWidgets.QLabel(parent=BaseData)
        self.label_limspeed_2.setGeometry(QtCore.QRect(20, 90, 101, 20))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label_limspeed_2.setFont(font)
        self.label_limspeed_2.setObjectName("label_limspeed_2")
        self.label_vehVolumes = QtWidgets.QLabel(parent=BaseData)
        self.label_vehVolumes.setGeometry(QtCore.QRect(20, 150, 131, 20))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label_vehVolumes.setFont(font)
        self.label_vehVolumes.setObjectName("label_vehVolumes")
        self.line_3 = QtWidgets.QFrame(parent=BaseData)
        self.line_3.setGeometry(QtCore.QRect(20, 120, 351, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_vehVolumes_Inunint = QtWidgets.QLabel(parent=BaseData)
        self.label_vehVolumes_Inunint.setGeometry(QtCore.QRect(340, 190, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_vehVolumes_Inunint.setFont(font)
        self.label_vehVolumes_Inunint.setObjectName("label_vehVolumes_Inunint")
        self.lineEdit_vehVolumes_Ininput = QtWidgets.QLineEdit(parent=BaseData)
        self.lineEdit_vehVolumes_Ininput.setGeometry(QtCore.QRect(90, 190, 241, 20))
        self.lineEdit_vehVolumes_Ininput.setText("")
        self.lineEdit_vehVolumes_Ininput.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_vehVolumes_Ininput.setObjectName("lineEdit_vehVolumes_Ininput")
        self.label_vehVolumes_In = QtWidgets.QLabel(parent=BaseData)
        self.label_vehVolumes_In.setGeometry(QtCore.QRect(20, 190, 70, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_vehVolumes_In.setFont(font)
        self.label_vehVolumes_In.setObjectName("label_vehVolumes_In")
        self.lineEditl_vehVolumes_Outinput = QtWidgets.QLineEdit(parent=BaseData)
        self.lineEditl_vehVolumes_Outinput.setGeometry(QtCore.QRect(90, 240, 241, 20))
        self.lineEditl_vehVolumes_Outinput.setText("")
        self.lineEditl_vehVolumes_Outinput.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEditl_vehVolumes_Outinput.setObjectName("lineEditl_vehVolumes_Outinput")
        self.label_vehVolumes_Out = QtWidgets.QLabel(parent=BaseData)
        self.label_vehVolumes_Out.setGeometry(QtCore.QRect(20, 240, 70, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_vehVolumes_Out.setFont(font)
        self.label_vehVolumes_Out.setObjectName("label_vehVolumes_Out")
        self.labell_vehVolumes_Outunint = QtWidgets.QLabel(parent=BaseData)
        self.labell_vehVolumes_Outunint.setGeometry(QtCore.QRect(340, 240, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.labell_vehVolumes_Outunint.setFont(font)
        self.labell_vehVolumes_Outunint.setObjectName("labell_vehVolumes_Outunint")

        self.retranslateUi(BaseData)
        self.buttonBox_BaseDataCtro.accepted.connect(BaseData.reject)  # type: ignore
        self.buttonBox_BaseDataCtro.rejected.connect(BaseData.accept)  # type: ignore
        # 绑定槽函数
        self.buttonBox_BaseDataCtro.clicked.connect(self.reSetting)

        QtCore.QMetaObject.connectSlotsByName(BaseData)

    def retranslateUi(self, BaseData):
        _translate = QtCore.QCoreApplication.translate
        BaseData.setWindowTitle(_translate("BaseData", "基础数据"))
        self.label_greenspeed.setText(_translate("BaseData", "设计绿波速度"))
        self.lineEdit_greenspeedinput.setPlaceholderText(_translate("BaseData", "示例：55"))
        self.label_greenspeedunint.setText(_translate("BaseData", "km/h"))
        self.lineEdit_limspeedinput.setPlaceholderText(_translate("BaseData", "示例：60"))
        self.label_limspeedunint.setText(_translate("BaseData", "km/h"))
        self.label_limspeed_2.setText(_translate("BaseData", "道路限制速度"))
        self.label_vehVolumes.setText(_translate("BaseData", "干线方向进口流量"))
        self.label_vehVolumes_Inunint.setText(_translate("BaseData", "veh/h"))
        self.lineEdit_vehVolumes_Ininput.setPlaceholderText(_translate("BaseData", "示例：[836, 1258, 1456, 968]"))
        self.label_vehVolumes_In.setText(_translate("BaseData", "上行"))
        self.lineEditl_vehVolumes_Outinput.setPlaceholderText(_translate("BaseData", "示例：[836, 1258, 1456, 968]"))
        self.label_vehVolumes_Out.setText(_translate("BaseData", "下行"))
        self.labell_vehVolumes_Outunint.setText(_translate("BaseData", "veh/h"))

    def reSetting(self, button):
        # 判断点击的是哪个btn
        # 获取输入框数据
        baseData = [self.lineEdit_greenspeedinput.text(), self.lineEdit_limspeedinput.text(),
                    self.lineEdit_vehVolumes_Ininput.text(), self.lineEditl_vehVolumes_Outinput.text()]

        if button == self.buttonBox_BaseDataCtro.button(QDialogButtonBox.StandardButton.Apply):
            """
            判断输入值是否为空
            :return:
            """

            res = any(not element.strip() for element in baseData)  # 判断是否非空
            if res:
                QMessageBox.warning(self, "系统提示", "输入不能为空")
            else:
                are_all_lists = all(isinstance(eval(baseData[i], {"__builtins__": {}}, {}), list) for i in [2, 3])
                # 如果非空且格式正确则关闭窗口并更新配置数据
                if are_all_lists:
                    # 如果非空则关闭窗口并更新配置数据
                    time = QDateTime.currentDateTime()  # 获取当前时间，并存储在self.qpp_data
                    self.app_data.setValue('time', time.toString())  # 数据0：time.toString()为字符串类型
                    # 读取默认数据并存储
                    self.app_data.setValue('LEgreenspeedinput', baseData[0])
                    self.app_data.setValue('LElimspeedinput', baseData[1])
                    self.app_data.setValue('LEvehVolumes_Ininput', baseData[2])
                    self.app_data.setValue('LEvehVolumes_Outinput', baseData[3])
                    self.close()
                else:
                    QMessageBox.warning(self, "系统提示", "数据格式有误！")
        else:
            self.close()

    # 存在配时文件则读取并设置
    def save_baseData(self):
        # time = self.app_data.value('time')
        # print(time)

        baseData = [self.app_data.value('LEgreenspeedinput'),
                    self.app_data.value('LElimspeedinput'),
                    self.app_data.value('LEvehVolumes_Ininput'),
                    self.app_data.value('LEvehVolumes_Outinput')]
        baseDataTepy = [self.lineEdit_greenspeedinput.placeholderText(),
                        self.lineEdit_limspeedinput.placeholderText(),
                        self.lineEdit_vehVolumes_Ininput.placeholderText(),
                        self.lineEditl_vehVolumes_Outinput.placeholderText()]
        if baseData != baseDataTepy:
            self.lineEdit_greenspeedinput.setText(baseData[0])
            self.lineEdit_limspeedinput.setText(baseData[1])
            self.lineEdit_vehVolumes_Ininput.setText(baseData[2])
            self.lineEditl_vehVolumes_Outinput.setText(baseData[3])

    # 若第一次打开则初始化
    def init_baseData(self):
        time = QDateTime.currentDateTime()  # 获取当前时间，并存储在self.qpp_data
        self.app_data.setValue('time', time.toString())  # 数据0：time.toString()为字符串类型
        # 读取默认数据并存储
        self.LEgreenspeedinput = self.lineEdit_greenspeedinput.placeholderText()
        self.app_data.setValue('LEgreenspeedinput', self.LEgreenspeedinput)
        self.LElimspeedinput = self.lineEdit_limspeedinput.placeholderText()
        self.app_data.setValue('LElimspeedinput', self.LElimspeedinput)
        self.LEvehVolumes_Ininput = self.lineEdit_vehVolumes_Ininput.placeholderText()
        self.app_data.setValue('LEvehVolumes_Ininput', self.LEvehVolumes_Ininput)
        self.LEvehVolumes_Outinput = self.lineEditl_vehVolumes_Outinput.placeholderText()
        self.app_data.setValue('LEvehVolumes_Outinput', self.LEvehVolumes_Outinput)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = BaseDataWindow()

    ui.show()

    sys.exit(app.exec())
