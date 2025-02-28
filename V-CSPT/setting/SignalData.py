"""
        主界面信号控制数据获取模块
        copyright ： CheneyZhao
        版本号 ： 1.0


"""
import os
import sys

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QSettings, QDateTime
from PyQt6.QtWidgets import QApplication, QDialog, QDialogButtonBox, QMessageBox


class SingalDataWindow(QDialog):

    def __init__(self):
        super(SingalDataWindow, self).__init__()
        self.setupUi(self)
        # 储存数据以供修改
        self.app_data = QSettings('./.inif/signalconfig.ini', QSettings.Format.IniFormat)
        # 检查是否有数据进行初始化
        if os.path.exists('./.inif/signalconfig.ini'):
            # 直接读取数据
            self.save_signalData()
        else:
            # 没有配置文件就创建配时文件进行数据初始化
            self.init_signalData()

    def setupUi(self, SingalData):
        SingalData.setObjectName("SingalData")
        SingalData.resize(791, 423)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icon_sub/singaldata.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        SingalData.setWindowIcon(icon)
        self.buttonBoxSingaldataCtro = QtWidgets.QDialogButtonBox(parent=SingalData)
        self.buttonBoxSingaldataCtro.setGeometry(QtCore.QRect(610, 380, 171, 32))
        self.buttonBoxSingaldataCtro.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBoxSingaldataCtro.setStandardButtons(
            QtWidgets.QDialogButtonBox.StandardButton.Apply | QtWidgets.QDialogButtonBox.StandardButton.Cancel)
        # 获取 Apply 按钮并设置中文文本
        self.buttonBoxSingaldataCtro.button(QtWidgets.QDialogButtonBox.StandardButton.Apply).setText("应用")
        self.buttonBoxSingaldataCtro.button(QtWidgets.QDialogButtonBox.StandardButton.Apply).setDefault(True)
        # 获取 Cancel 按钮并设置中文文本
        self.buttonBoxSingaldataCtro.button(QtWidgets.QDialogButtonBox.StandardButton.Cancel).setText("取消")
        self.buttonBoxSingaldataCtro.setObjectName("buttonBoxSingaldataCtro")
        self.label_singalnumOut = QtWidgets.QLabel(parent=SingalData)
        self.label_singalnumOut.setGeometry(QtCore.QRect(30, 130, 70, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_singalnumOut.setFont(font)
        self.label_singalnumOut.setObjectName("label_singalnumOut")
        self.lineEdit_singalnumOutinput = QtWidgets.QLineEdit(parent=SingalData)
        self.lineEdit_singalnumOutinput.setGeometry(QtCore.QRect(100, 130, 671, 20))
        self.lineEdit_singalnumOutinput.setText("")
        self.lineEdit_singalnumOutinput.setMaxLength(50000)
        self.lineEdit_singalnumOutinput.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_singalnumOutinput.setObjectName("lineEdit_singalnumOutinput")
        self.label_singalnum = QtWidgets.QLabel(parent=SingalData)
        self.label_singalnum.setGeometry(QtCore.QRect(30, 20, 141, 20))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label_singalnum.setFont(font)
        self.label_singalnum.setObjectName("label_singalnum")
        self.lineEdit_singalnumIninput = QtWidgets.QLineEdit(parent=SingalData)
        self.lineEdit_singalnumIninput.setGeometry(QtCore.QRect(100, 70, 671, 21))
        self.lineEdit_singalnumIninput.setText("")
        self.lineEdit_singalnumIninput.setMaxLength(50000)
        self.lineEdit_singalnumIninput.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_singalnumIninput.setObjectName("lineEdit_singalnumIninput")
        self.label_singalnumIn = QtWidgets.QLabel(parent=SingalData)
        self.label_singalnumIn.setGeometry(QtCore.QRect(30, 70, 70, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_singalnumIn.setFont(font)
        self.label_singalnumIn.setObjectName("label_singalnumIn")
        self.line_6 = QtWidgets.QFrame(parent=SingalData)
        self.line_6.setGeometry(QtCore.QRect(30, 180, 721, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_6.setObjectName("line_6")
        self.lineEdit_singalnumLIninput = QtWidgets.QLineEdit(parent=SingalData)
        self.lineEdit_singalnumLIninput.setGeometry(QtCore.QRect(100, 270, 671, 21))
        self.lineEdit_singalnumLIninput.setText("")
        self.lineEdit_singalnumLIninput.setMaxLength(50000)
        self.lineEdit_singalnumLIninput.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_singalnumLIninput.setObjectName("lineEdit_singalnumLIninput")
        self.label_singalnumLIn = QtWidgets.QLabel(parent=SingalData)
        self.label_singalnumLIn.setGeometry(QtCore.QRect(30, 270, 70, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_singalnumLIn.setFont(font)
        self.label_singalnumLIn.setObjectName("label_singalnumLIn")
        self.label_singalnumLOut = QtWidgets.QLabel(parent=SingalData)
        self.label_singalnumLOut.setGeometry(QtCore.QRect(30, 330, 70, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_singalnumLOut.setFont(font)
        self.label_singalnumLOut.setObjectName("label_singalnumLOut")
        self.lineEdit_singalnumLOutinput = QtWidgets.QLineEdit(parent=SingalData)
        self.lineEdit_singalnumLOutinput.setGeometry(QtCore.QRect(100, 330, 671, 20))
        self.lineEdit_singalnumLOutinput.setText("")
        self.lineEdit_singalnumLOutinput.setMaxLength(50000)
        self.lineEdit_singalnumLOutinput.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_singalnumLOutinput.setObjectName("lineEdit_singalnumLOutinput")
        self.label_singalnumL = QtWidgets.QLabel(parent=SingalData)
        self.label_singalnumL.setGeometry(QtCore.QRect(30, 220, 141, 20))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label_singalnumL.setFont(font)
        self.label_singalnumL.setObjectName("label_singalnumL")

        self.retranslateUi(SingalData)
        self.buttonBoxSingaldataCtro.accepted.connect(SingalData.accept)  # type: ignore
        self.buttonBoxSingaldataCtro.rejected.connect(SingalData.reject)  # type: ignore
        # 绑定槽函数
        self.buttonBoxSingaldataCtro.clicked.connect(self.reSetting)

        QtCore.QMetaObject.connectSlotsByName(SingalData)

    def retranslateUi(self, SingalData):
        _translate = QtCore.QCoreApplication.translate
        SingalData.setWindowTitle(_translate("SingalData", "配时数据"))
        self.label_singalnumOut.setText(_translate("SingalData", "下行"))
        self.lineEdit_singalnumOutinput.setPlaceholderText(
            _translate("SingalData", "示例：[[2, 57], [1, 27], [1, 1], [2, 4]]"))
        self.label_singalnum.setText(_translate("SingalData", "干线直行灯头编号"))
        self.lineEdit_singalnumIninput.setPlaceholderText(
            _translate("SingalData", "示例：[[5, 2], [5, 18], [5, 46], [4, 65]]"))
        self.label_singalnumIn.setText(_translate("SingalData", "上行"))
        self.lineEdit_singalnumLIninput.setPlaceholderText(
            _translate("SingalData", "示例：[[1, 1], [2, 220], [2, 33], [1, 54]]"))
        self.label_singalnumLIn.setText(_translate("SingalData", "上行"))
        self.label_singalnumLOut.setText(_translate("SingalData", "下行"))
        self.lineEdit_singalnumLOutinput.setPlaceholderText(
            _translate("SingalData", "示例：[[5, 67], [6, 47], [6, 20], [6, 6]]"))
        self.label_singalnumL.setText(_translate("SingalData", "干线左转灯头编号"))

    def reSetting(self, button):
        # 判断点击的是哪个btn
        # 获取输入框数据
        signalData = [self.lineEdit_singalnumIninput.text(), self.lineEdit_singalnumOutinput.text(),
                      self.lineEdit_singalnumLIninput.text(), self.lineEdit_singalnumLOutinput.text()]

        if button == self.buttonBoxSingaldataCtro.button(QDialogButtonBox.StandardButton.Apply):
            """
            判断输入值是否为空
            :return:
            """

            res = any(not element.strip() for element in signalData)  # 判断是否非空
            if res:
                QMessageBox.warning(self, "系统提示", "输入不能为空")
            else:
                Res = []
                for item in signalData:
                    if eval(item, {"__builtins__": {}}, {}):
                        for item_i in eval(item, {"__builtins__": {}}, {}):
                            result = isinstance(item_i, list)
                            Res.append(result)
                    else:
                        Res.append(False)
                # are_all_lists = all(isinstance(eval(item, {"__builtins__": {}}, {}), list) for item in signalData)
                # 如果非空且格式正确则关闭窗口并更新配置数据
                if all(Res):
                    time = QDateTime.currentDateTime()  # 获取当前时间，并存储在self.qpp_data
                    self.app_data.setValue('time', time.toString())  # 数据0：time.toString()为字符串类型
                    # 读取默认数据并存储
                    self.app_data.setValue('LEsingalnumIninput', signalData[0])
                    self.app_data.setValue('LEsingalnumOutinput', signalData[1])
                    self.app_data.setValue('LEsingalnumLIninput', signalData[2])
                    self.app_data.setValue('LEsingalnumLOutinput', signalData[3])
                    self.close()
                else:
                    QMessageBox.warning(self, "系统提示", "数据格式有误！")
        else:
            self.close()

    # 存在配时文件则读取并设置
    def save_signalData(self):
        time = self.app_data.value('time')
        print(time)

        signalData = [self.app_data.value('LEsingalnumIninput'),
                      self.app_data.value('LEsingalnumOutinput'),
                      self.app_data.value('LEsingalnumLIninput'),
                      self.app_data.value('LEsingalnumLOutinput')]
        signalDataTepy = [self.lineEdit_singalnumIninput.placeholderText(),
                          self.lineEdit_singalnumOutinput.placeholderText(),
                          self.lineEdit_singalnumLIninput.placeholderText(),
                          self.lineEdit_singalnumLOutinput.placeholderText()]
        if signalData != signalDataTepy:
            self.lineEdit_singalnumIninput.setText(signalData[0])
            self.lineEdit_singalnumOutinput.setText(signalData[1])
            self.lineEdit_singalnumLIninput.setText(signalData[2])
            self.lineEdit_singalnumLOutinput.setText(signalData[3])

    # 若第一次打开则初始化
    def init_signalData(self):
        time = QDateTime.currentDateTime()  # 获取当前时间，并存储在self.qpp_data
        self.app_data.setValue('time', time.toString())  # 数据0：time.toString()为字符串类型
        # 读取默认数据并存储
        self.LEsingalnumIninput = self.lineEdit_singalnumIninput.placeholderText()
        self.app_data.setValue('LEsingalnumIninput', self.LEsingalnumIninput)

        self.LEsingalnumOutinput = self.lineEdit_singalnumOutinput.placeholderText()
        self.app_data.setValue('LEsingalnumOutinput', self.LEsingalnumOutinput)

        self.LEsingalnumLIninput = self.lineEdit_singalnumLIninput.placeholderText()
        self.app_data.setValue('LEsingalnumLIninput', self.LEsingalnumLIninput)

        self.LEsingalnumLOutinput = self.lineEdit_singalnumLOutinput.placeholderText()
        self.app_data.setValue('LEsingalnumLOutinput', self.LEsingalnumLOutinput)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = SingalDataWindow()

    ui.show()

    sys.exit(app.exec())
