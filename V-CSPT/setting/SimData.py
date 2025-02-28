"""
        主界面仿真设置模块
        copyright ： CheneyZhao
        版本号 ： 1.0


"""
import os
import sys

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QSettings, QDateTime
from PyQt6.QtWidgets import QApplication, QDialog, QDialogButtonBox, QMessageBox


class SimDataWindow(QDialog):

    def __init__(self):
        super(SimDataWindow, self).__init__()
        self.setupUi(self)
        # 储存数据以供修改
        self.app_data = QSettings('./.inif/simconfig.ini', QSettings.Format.IniFormat)
        # 检查是否有数据进行初始化
        if os.path.exists('./.inif/simconfig.ini'):
            # 直接读取数据
            self.save_simData()
        else:
            # 没有配置文件就创建配时文件进行数据初始化
            self.init_simData()

    def setupUi(self, SimData):
        SimData.setObjectName("SimData")
        SimData.resize(407, 347)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icon_sub/simdata.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        SimData.setWindowIcon(icon)
        self.buttonBox_BaseDataCtro = QtWidgets.QDialogButtonBox(parent=SimData)
        self.buttonBox_BaseDataCtro.setGeometry(QtCore.QRect(220, 310, 171, 32))
        self.buttonBox_BaseDataCtro.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox_BaseDataCtro.setStandardButtons(
            QtWidgets.QDialogButtonBox.StandardButton.Apply | QtWidgets.QDialogButtonBox.StandardButton.Cancel)

        # 获取 Apply 按钮并设置中文文本
        self.buttonBox_BaseDataCtro.button(QtWidgets.QDialogButtonBox.StandardButton.Apply).setText("应用")
        self.buttonBox_BaseDataCtro.button(QtWidgets.QDialogButtonBox.StandardButton.Apply).setDefault(True)
        # 获取 Cancel 按钮并设置中文文本
        self.buttonBox_BaseDataCtro.button(QtWidgets.QDialogButtonBox.StandardButton.Cancel).setText("取消")
        self.buttonBox_BaseDataCtro.setObjectName("buttonBox_BaseDataCtro")
        self.label_Seedinterval = QtWidgets.QLabel(parent=SimData)
        self.label_Seedinterval.setGeometry(QtCore.QRect(50, 260, 101, 20))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label_Seedinterval.setFont(font)
        self.label_Seedinterval.setObjectName("label_Seedinterval")
        self.lineEdit_Seedinterval = QtWidgets.QLineEdit(parent=SimData)
        self.lineEdit_Seedinterval.setGeometry(QtCore.QRect(190, 260, 121, 20))
        self.lineEdit_Seedinterval.setInputMask("")
        self.lineEdit_Seedinterval.setText("")
        self.lineEdit_Seedinterval.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_Seedinterval.setDragEnabled(False)
        self.lineEdit_Seedinterval.setObjectName("lineEdit_Seedinterval")
        self.lineEdit_Dertaseed = QtWidgets.QLineEdit(parent=SimData)
        self.lineEdit_Dertaseed.setGeometry(QtCore.QRect(190, 210, 121, 20))
        self.lineEdit_Dertaseed.setInputMask("")
        self.lineEdit_Dertaseed.setText("")
        self.lineEdit_Dertaseed.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_Dertaseed.setDragEnabled(False)
        self.lineEdit_Dertaseed.setObjectName("lineEdit_Dertaseed")
        self.label_Dertaseed = QtWidgets.QLabel(parent=SimData)
        self.label_Dertaseed.setGeometry(QtCore.QRect(50, 210, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_Dertaseed.setFont(font)
        self.label_Dertaseed.setObjectName("label_Dertaseed")
        self.line_4 = QtWidgets.QFrame(parent=SimData)
        self.line_4.setGeometry(QtCore.QRect(40, 180, 351, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_Bottime = QtWidgets.QLabel(parent=SimData)
        self.label_Bottime.setGeometry(QtCore.QRect(50, 90, 101, 20))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label_Bottime.setFont(font)
        self.label_Bottime.setObjectName("label_Bottime")
        self.lineEdit_Bottime = QtWidgets.QLineEdit(parent=SimData)
        self.lineEdit_Bottime.setGeometry(QtCore.QRect(190, 90, 121, 20))
        self.lineEdit_Bottime.setInputMask("")
        self.lineEdit_Bottime.setText("")
        self.lineEdit_Bottime.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_Bottime.setDragEnabled(False)
        self.lineEdit_Bottime.setObjectName("lineEdit_Bottime")
        self.label_Simperiod = QtWidgets.QLabel(parent=SimData)
        self.label_Simperiod.setGeometry(QtCore.QRect(50, 40, 101, 20))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label_Simperiod.setFont(font)
        self.label_Simperiod.setObjectName("label_Simperiod")
        self.label_limspeedunint_3 = QtWidgets.QLabel(parent=SimData)
        self.label_limspeedunint_3.setGeometry(QtCore.QRect(320, 90, 70, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_limspeedunint_3.setFont(font)
        self.label_limspeedunint_3.setObjectName("label_limspeedunint_3")
        self.lineEdit_Simperiod = QtWidgets.QLineEdit(parent=SimData)
        self.lineEdit_Simperiod.setGeometry(QtCore.QRect(190, 40, 121, 20))
        self.lineEdit_Simperiod.setInputMask("")
        self.lineEdit_Simperiod.setText("")
        self.lineEdit_Simperiod.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_Simperiod.setDragEnabled(False)
        self.lineEdit_Simperiod.setObjectName("lineEdit_Simperiod")
        self.label_greenspeedunint_2 = QtWidgets.QLabel(parent=SimData)
        self.label_greenspeedunint_2.setGeometry(QtCore.QRect(320, 40, 70, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_greenspeedunint_2.setFont(font)
        self.label_greenspeedunint_2.setObjectName("label_greenspeedunint_2")
        self.label__trishowunint = QtWidgets.QLabel(parent=SimData)
        self.label__trishowunint.setGeometry(QtCore.QRect(320, 140, 70, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label__trishowunint.setFont(font)
        self.label__trishowunint.setObjectName("label__trishowunint")
        self.lineEdit_trishowinput = QtWidgets.QLineEdit(parent=SimData)
        self.lineEdit_trishowinput.setGeometry(QtCore.QRect(190, 140, 121, 20))
        self.lineEdit_trishowinput.setInputMask("")
        self.lineEdit_trishowinput.setText("")
        self.lineEdit_trishowinput.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_trishowinput.setDragEnabled(False)
        self.lineEdit_trishowinput.setObjectName("lineEdit_trishowinput")
        self.label_trishowinput = QtWidgets.QLabel(parent=SimData)
        self.label_trishowinput.setGeometry(QtCore.QRect(50, 140, 111, 20))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label_trishowinput.setFont(font)
        self.label_trishowinput.setObjectName("label_trishowinput")

        self.retranslateUi(SimData)
        self.buttonBox_BaseDataCtro.accepted.connect(SimData.accept)  # type: ignore
        self.buttonBox_BaseDataCtro.rejected.connect(SimData.reject)  # type: ignore
        # 绑定槽函数
        self.buttonBox_BaseDataCtro.clicked.connect(self.reSetting)

        QtCore.QMetaObject.connectSlotsByName(SimData)

    def retranslateUi(self, SimData):
        _translate = QtCore.QCoreApplication.translate
        SimData.setWindowTitle(_translate("SimData", "仿真数据"))
        self.label_Seedinterval.setText(_translate("SimData", "随机种子区间"))
        self.lineEdit_Seedinterval.setPlaceholderText(_translate("SimData", "示例：[10, 100]"))
        self.lineEdit_Dertaseed.setPlaceholderText(_translate("SimData", "示例：10"))
        self.label_Dertaseed.setText(_translate("SimData", "随机种子增量"))
        self.label_Bottime.setText(_translate("SimData", "仿真预热时间"))
        self.lineEdit_Bottime.setPlaceholderText(_translate("SimData", "示例：600"))
        self.label_Simperiod.setText(_translate("SimData", "单次仿真时间"))
        self.label_limspeedunint_3.setText(_translate("SimData", "s"))
        self.lineEdit_Simperiod.setPlaceholderText(_translate("SimData", "示例：3600"))
        # self.label_greenspeedunint.setText(_translate("SimData", "s"))
        self.label__trishowunint.setText(_translate("SimData", "s"))
        self.lineEdit_trishowinput.setPlaceholderText(_translate("SimData", "示例：[1800, 2500]"))
        self.label_trishowinput.setText(_translate("SimData", "轨迹图显示区间"))

    def reSetting(self, button):
        # 判断点击的是哪个btn

        if button == self.buttonBox_BaseDataCtro.button(QDialogButtonBox.StandardButton.Apply):
            """
            判断输入值是否为空
            :return:
            """
            # 获取输入框数据
            simData = [self.lineEdit_Simperiod.text(), self.lineEdit_Bottime.text(), self.lineEdit_trishowinput.text(),
                       self.lineEdit_Dertaseed.text(), self.lineEdit_Seedinterval.text()]

            res = any(not element.strip() for element in simData)  # 判断是否非空
            if res:
                QMessageBox.warning(self, "系统提示", "输入不能为空")
            else:
                are_all_lists = all(isinstance(eval(simData[i], {"__builtins__": {}}, {}), list) for i in [2, 4])
                # 如果非空则关闭窗口并更新配置数据
                # print(are_all_lists)
                # print(simData[3])
                # print(simData[4])
                if are_all_lists:
                    time = QDateTime.currentDateTime()  # 获取当前时间，并存储在self.qpp_data
                    self.app_data.setValue('time', time.toString())  # 数据0：time.toString()为字符串类型
                    # 读取默认数据并存储
                    self.app_data.setValue('LESimperiod', simData[0])
                    self.app_data.setValue('LEBottime', simData[1])
                    self.app_data.setValue('LEtrishowinput', simData[2])
                    self.app_data.setValue('LEDertaseed', simData[3])
                    self.app_data.setValue('LESeedinterval', simData[4])
                    self.close()
                else:
                    QMessageBox.warning(self, "系统提示", "数据格式有误！")
        else:
            self.close()

    # 存在配时文件则读取并设置
    def save_simData(self):
        time = self.app_data.value('time')
        print(time)

        simData = [self.app_data.value('LESimperiod'),
                   self.app_data.value('LEBottime'),
                   self.app_data.value('LEtrishowinput'),
                   self.app_data.value('LEDertaseed'),
                   self.app_data.value('LESeedinterval')]
        # 读取并设置
        simDataType = [self.lineEdit_Simperiod.placeholderText(),
                       self.lineEdit_Bottime.placeholderText(),
                       self.lineEdit_trishowinput.placeholderText(),
                       self.lineEdit_Dertaseed.placeholderText(),
                       self.lineEdit_Seedinterval.placeholderText()]
        if simData != simDataType:
            self.lineEdit_Simperiod.setText(simData[0])
            self.lineEdit_Bottime.setText(simData[1])
            self.lineEdit_trishowinput.setText(simData[2])
            self.lineEdit_Dertaseed.setText(simData[3])
            self.lineEdit_Seedinterval.setText(simData[4])

    # 若第一次打开则初始化
    def init_simData(self):
        time = QDateTime.currentDateTime()  # 获取当前时间，并存储在self.qpp_data
        self.app_data.setValue('time', time.toString())  # 数据0：time.toString()为字符串类型
        # 读取默认数据并存储
        self.LESimperiod = self.lineEdit_Simperiod.placeholderText()
        self.app_data.setValue('LESimperiod', self.LESimperiod)

        self.LEBottime = self.lineEdit_Bottime.placeholderText()
        self.app_data.setValue('LEBottime', self.LEBottime)

        self.LEtrishowinput = self.lineEdit_trishowinput.placeholderText()
        self.app_data.setValue('LEtrishowinput', self.LEtrishowinput)

        self.LEDertaseed = self.lineEdit_Dertaseed.placeholderText()
        self.app_data.setValue('LEDertaseed', self.LEDertaseed)

        self.LESeedinterval = self.lineEdit_Seedinterval.placeholderText()
        self.app_data.setValue('LESeedinterval', self.LESeedinterval)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = SimDataWindow()

    ui.show()

    sys.exit(app.exec())
