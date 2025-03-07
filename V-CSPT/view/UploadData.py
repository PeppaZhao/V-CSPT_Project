# Form implementation generated from reading ui file 'UploadData.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
import os
import sys

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QSettings, QDateTime
from PyQt6.QtWidgets import QDialog, QApplication, QMessageBox

from order_set import order


class UpLoadData(QDialog):

    def __init__(self):
        super(UpLoadData, self).__init__()
        self.data_loc_file = None
        self.setupUi(self)
        # 储存数据以供修改
        self.app_data = QSettings('./.inif/loaddataconfig.ini', QSettings.Format.IniFormat)
        # 检查是否有数据进行初始化
        if os.path.exists('./.inif/loaddataconfig.ini'):
            # 直接读取数据
            self.save_loadData()
        else:
            # 没有配置文件就创建配时文件进行数据初始化
            self.init_loadData()

    def setupUi(self, Dialog):
        # 检查是否有数据进行初始化
        self.data_loc_file = ["no trajectory_data.csv", "no trajectory_data.csv"]
        self.color_font = ['#d81e06', '#d81e06']  # 默认初始化字体颜色

        if os.path.exists('./.inif/loaddataconfig.ini'):
            app_loaddata = QSettings('.inif/loaddataconfig.ini', QSettings.Format.IniFormat)
            self.data_loc_file = [
                os.path.basename(app_loaddata.value('inbound_trajectory_file_loc', "")),
                os.path.basename(app_loaddata.value('outbound_trajectory_file_loc', ""))
            ]
            self.color_font = ['#d81e06', '#d81e06']  # 初始化字体颜色

            for i in range(2):
                if not self.data_loc_file[i]:  # 如果文件名为空
                    self.data_loc_file[i] = "no trajectory_data.csv"
                    self.color_font[i] = '#d81e06'

        Dialog.setObjectName("Dialog")
        Dialog.resize(1046, 646)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icon_main/upload_data.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(5, 0, 5, 3)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_5 = QtWidgets.QFrame(parent=Dialog)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 130))
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout.setContentsMargins(0, 9, 0, 9)
        self.gridLayout.setHorizontalSpacing(9)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(f"QLabel {{\n"
                                   "  font-size: 20px;\n"
                                   f"  color: {self.color_font[1]};\n"  # 使用变量
                                   "  background-color: #f9f9f9;\n"
                                   "  border: 2px solid #ccc;\n"
                                   "  padding: 10px;\n"
                                   "  border-radius: 5px;\n"
                                   "  transition: background-color 0.3s ease, color 0.3s ease; /* 平滑过渡 */\n"
                                   "}}")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.frame_5)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setStyleSheet(f"QLabel {{\n"
                                 "  font-size: 20px;\n"
                                 f"  color: {self.color_font[0]};\n"  # 使用变量
                                 "  background-color: #f9f9f9;\n"
                                 "  border: 2px solid #ccc;\n"
                                 "  padding: 10px;\n"
                                 "  border-radius: 5px;\n"
                                 "  transition: background-color 0.3s ease, color 0.3s ease; /* 平滑过渡 */\n"
                                 "}}")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.upload_outbound = QtWidgets.QPushButton(parent=self.frame_5)
        self.upload_outbound.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.upload_outbound.setFont(font)
        self.upload_outbound.setStyleSheet("QPushButton {\n"
                                           "  background-color: transparent; /* 透明背景 */\n"
                                           "  border: 2px solid #13227a; /* 边框颜色 */\n"
                                           "  color: #13227a; /* 文字颜色 */\n"
                                           "  border-radius: 8px;\n"
                                           "  padding: 10px 20px;\n"
                                           "  font-size: 18px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:hover {\n"
                                           "  background-color: #87a7d6; /* 悬停时的背景颜色 */\n"
                                           "  color:  #13227a; /* 悬停时的文字颜色 */\n"
                                           "}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../icon_main/upload.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.upload_outbound.setIcon(icon1)
        self.upload_outbound.setIconSize(QtCore.QSize(22, 22))
        self.upload_outbound.setObjectName("upload_outbound")

        # 绑定槽函数
        self.upload_outbound.clicked.connect(self.open_file_out)

        self.gridLayout.addWidget(self.upload_outbound, 0, 1, 1, 1)
        self.upload_inbound = QtWidgets.QPushButton(parent=self.frame_5)
        self.upload_inbound.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.upload_inbound.setFont(font)
        self.upload_inbound.setStyleSheet("QPushButton {\n"
                                          "  background-color: transparent; /* 透明背景 */\n"
                                          "  border: 2px solid #13227a; /* 边框颜色 */\n"
                                          "  color: #13227a; /* 文字颜色 */\n"
                                          "  border-radius: 8px;\n"
                                          "  padding: 10px 20px;\n"
                                          "  font-size: 18px;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover {\n"
                                          "  background-color: #87a7d6; /* 悬停时的背景颜色 */\n"
                                          "  color:  #13227a; /* 悬停时的文字颜色 */\n"
                                          "}")
        self.upload_inbound.setIcon(icon1)
        self.upload_inbound.setIconSize(QtCore.QSize(22, 22))
        self.upload_inbound.setObjectName("upload_inbound")

        # 绑定槽函数
        self.upload_inbound.clicked.connect(self.open_file_in)

        self.gridLayout.addWidget(self.upload_inbound, 0, 0, 1, 1)
        self.label.raise_()
        self.upload_outbound.raise_()
        self.label_2.raise_()
        self.upload_inbound.raise_()
        self.verticalLayout.addWidget(self.frame_5)
        self.frame_3 = QtWidgets.QFrame(parent=Dialog)
        self.frame_3.setStyleSheet("")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(parent=self.frame_3)
        self.frame.setStyleSheet("QFrame {\n"
                                 "  border: 2px solid #ccc;\n"
                                 "  padding: 10px;\n"
                                 "  border-radius: 5px;\n"
                                 "}\n"
                                 "\n"
                                 "")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(parent=self.frame)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_2.setStyleSheet("QFrame {\n"
                                   "  border: 0px ;\n"
                                   "}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 11, 0, 1, 1)
        self.signal_RG1_input = QtWidgets.QLineEdit(parent=self.frame_2)
        self.signal_RG1_input.setMinimumSize(QtCore.QSize(0, 25))
        self.signal_RG1_input.setObjectName("signal_RG1_input")
        self.gridLayout_3.addWidget(self.signal_RG1_input, 12, 1, 1, 1)
        self.inbound_phase_input = QtWidgets.QLineEdit(parent=self.frame_2)
        self.inbound_phase_input.setMinimumSize(QtCore.QSize(0, 25))
        self.inbound_phase_input.setObjectName("inbound_phase_input")
        self.gridLayout_3.addWidget(self.inbound_phase_input, 8, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 5, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 6, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 13, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(parent=self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.gridLayout_3.addWidget(self.label_17, 2, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_3.addItem(spacerItem3, 7, 0, 1, 1)
        self.signal_RG2_input = QtWidgets.QLineEdit(parent=self.frame_2)
        self.signal_RG2_input.setMinimumSize(QtCore.QSize(0, 25))
        self.signal_RG2_input.setObjectName("signal_RG2_input")
        self.gridLayout_3.addWidget(self.signal_RG2_input, 14, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(parent=self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 12, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(parent=self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 10, 0, 1, 1)
        self.offset_input = QtWidgets.QLineEdit(parent=self.frame_2)
        self.offset_input.setMinimumSize(QtCore.QSize(0, 25))
        self.offset_input.setObjectName("offset_input")
        self.gridLayout_3.addWidget(self.offset_input, 6, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 2)
        self.label_9 = QtWidgets.QLabel(parent=self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 14, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(parent=self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 8, 0, 1, 1)
        self.outbound_phase_input = QtWidgets.QLineEdit(parent=self.frame_2)
        self.outbound_phase_input.setMinimumSize(QtCore.QSize(0, 25))
        self.outbound_phase_input.setObjectName("outbound_phase_input")
        self.gridLayout_3.addWidget(self.outbound_phase_input, 10, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_3.addItem(spacerItem4, 9, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_3.addItem(spacerItem5, 1, 0, 1, 1)
        self.cycle_input = QtWidgets.QLineEdit(parent=self.frame_2)
        self.cycle_input.setMinimumSize(QtCore.QSize(0, 25))
        self.cycle_input.setInputMask("")
        self.cycle_input.setReadOnly(False)
        self.cycle_input.setObjectName("cycle_input")
        self.gridLayout_3.addWidget(self.cycle_input, 2, 1, 1, 1)
        self.horizontalLayout.addWidget(self.frame_2)
        self.line = QtWidgets.QFrame(parent=self.frame)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.frame_4 = QtWidgets.QFrame(parent=self.frame)
        self.frame_4.setMaximumSize(QtCore.QSize(505, 16777215))
        self.frame_4.setStyleSheet("QFrame {\n"
                                   "  border: 0px solid #ccc;\n"
                                   "}\n"
                                   "\n"
                                   "")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_11 = QtWidgets.QLabel(parent=self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_4.addWidget(self.label_11, 10, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(parent=self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout_4.addWidget(self.label_12, 12, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_4.addItem(spacerItem6, 11, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=self.frame_4)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 3, 0, 1, 7)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_4.addItem(spacerItem7, 8, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_4.addItem(spacerItem8, 4, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_4.addItem(spacerItem9, 17, 0, 1, 1)
        self.outboundinter_loc_input = QtWidgets.QLineEdit(parent=self.frame_4)
        self.outboundinter_loc_input.setMinimumSize(QtCore.QSize(0, 25))
        self.outboundinter_loc_input.setObjectName("outboundinter_loc_input")
        self.gridLayout_4.addWidget(self.outboundinter_loc_input, 19, 1, 1, 6)
        self.arterial_length_input = QtWidgets.QLineEdit(parent=self.frame_4)
        self.arterial_length_input.setMinimumSize(QtCore.QSize(0, 25))
        self.arterial_length_input.setObjectName("arterial_length_input")
        self.gridLayout_4.addWidget(self.arterial_length_input, 5, 6, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                             QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_4.addItem(spacerItem10, 15, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(parent=self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout_4.addWidget(self.label_14, 5, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(parent=self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.gridLayout_4.addWidget(self.label_15, 7, 0, 1, 1)
        self.veh_volumes_input = QtWidgets.QLineEdit(parent=self.frame_4)
        self.veh_volumes_input.setMinimumSize(QtCore.QSize(0, 25))
        self.veh_volumes_input.setObjectName("veh_volumes_input")
        self.gridLayout_4.addWidget(self.veh_volumes_input, 12, 1, 1, 6)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                             QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_4.addItem(spacerItem11, 6, 0, 1, 1)
        self.arterial_lanenum_input = QtWidgets.QLineEdit(parent=self.frame_4)
        self.arterial_lanenum_input.setMinimumSize(QtCore.QSize(0, 25))
        self.arterial_lanenum_input.setObjectName("arterial_lanenum_input")
        self.gridLayout_4.addWidget(self.arterial_lanenum_input, 10, 1, 1, 6)
        self.label_16 = QtWidgets.QLabel(parent=self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.gridLayout_4.addWidget(self.label_16, 5, 2, 1, 1)
        self.green_speed_input = QtWidgets.QLineEdit(parent=self.frame_4)
        self.green_speed_input.setMinimumSize(QtCore.QSize(0, 25))
        self.green_speed_input.setObjectName("green_speed_input")
        self.gridLayout_4.addWidget(self.green_speed_input, 5, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(parent=self.frame_4)
        self.label_10.setObjectName("label_10")
        self.gridLayout_4.addWidget(self.label_10, 5, 4, 1, 1)
        self.inboundinter_loc_input = QtWidgets.QLineEdit(parent=self.frame_4)
        self.inboundinter_loc_input.setMinimumSize(QtCore.QSize(0, 25))
        self.inboundinter_loc_input.setObjectName("inboundinter_loc_input")
        self.gridLayout_4.addWidget(self.inboundinter_loc_input, 16, 1, 1, 6)
        self.side_lanenum_input = QtWidgets.QLineEdit(parent=self.frame_4)
        self.side_lanenum_input.setMinimumSize(QtCore.QSize(0, 25))
        self.side_lanenum_input.setObjectName("side_lanenum_input")
        self.gridLayout_4.addWidget(self.side_lanenum_input, 7, 1, 1, 6)
        self.label_13 = QtWidgets.QLabel(parent=self.frame_4)
        self.label_13.setMaximumSize(QtCore.QSize(140, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout_4.addWidget(self.label_13, 16, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(parent=self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.gridLayout_4.addWidget(self.label_18, 19, 0, 1, 1)
        self.collect_data_period_input = QtWidgets.QLineEdit(parent=self.frame_4)
        self.collect_data_period_input.setMinimumSize(QtCore.QSize(0, 25))
        self.collect_data_period_input.setObjectName("collect_data_period_input")
        self.gridLayout_4.addWidget(self.collect_data_period_input, 5, 3, 1, 1)
        self.horizontalLayout.addWidget(self.frame_4)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_3)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.StandardButton.Cancel | QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        # 获取 Apply 按钮并设置中文文本
        self.buttonBox.button(QtWidgets.QDialogButtonBox.StandardButton.Ok).setText("确定")
        self.buttonBox.button(QtWidgets.QDialogButtonBox.StandardButton.Ok).setDefault(True)
        # 获取 Cancel 按钮并设置中文文本
        self.buttonBox.button(QtWidgets.QDialogButtonBox.StandardButton.Cancel).setText("取消")

        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        # self.buttonBox.accepted.connect(Dialog.accept)  # type: ignore
        # self.buttonBox.rejected.connect(Dialog.reject)  # type: ignore

        # 绑定槽函数
        self.buttonBox.clicked.connect(self.reSetting)

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "上传数据"))
        self.label_2.setText(_translate("Dialog", "no trajectory_data.csv"))
        self.label.setText(_translate("Dialog", "no trajectory_data.csv"))
        self.upload_outbound.setText(_translate("Dialog", "上传下行方向轨迹数据"))
        self.upload_inbound.setText(_translate("Dialog", "上传上行方向轨迹数据"))
        self.signal_RG1_input.setPlaceholderText(_translate("Dialog",
                                                            "示例：{\'yr1\': [...], \'green1\': [...], \'yr2\': [...], "
                                                            "\'green2\': [...], \'red\': ...]}"))
        self.inbound_phase_input.setPlaceholderText(_translate("Dialog", "示例：[\'lead\', \'lead\', \'lead\']"))
        self.label_5.setText(_translate("Dialog", "相位差"))
        self.label_17.setText(_translate("Dialog", "周期"))
        self.signal_RG2_input.setPlaceholderText(_translate("Dialog",
                                                            "示例：{\'yr1\': [...], \'green1\': [...], \'yr2\': [...], "
                                                            "\'green2\': [...], \'red\': ...]}"))
        self.label_8.setText(_translate("Dialog", "配时方案RG1"))
        self.label_7.setText(_translate("Dialog", "下行相序"))
        self.offset_input.setPlaceholderText(_translate("Dialog", "示例：[0, 56, 15]"))
        self.label_3.setText(_translate("Dialog",
                                        "<html><head/><body><p><span style=\" font-size:16pt; "
                                        "font-weight:700;\">配时数据</span></p></body></html>"))
        self.label_9.setText(_translate("Dialog", "配时方案RG2"))
        self.label_6.setText(_translate("Dialog", "上行相序"))
        self.outbound_phase_input.setPlaceholderText(_translate("Dialog", "示例：[\'lag\', \'lead\', \'lag\']"))
        self.cycle_input.setPlaceholderText(_translate("Dialog", "示例：[148, 148, 148]"))
        self.label_11.setText(_translate("Dialog", "干线车道数"))
        self.label_12.setText(_translate("Dialog", "入口流量"))
        self.label_4.setText(_translate("Dialog",
                                        "<html><head/><body><p><span style=\" font-size:16pt; "
                                        "font-weight:700;\">干线数据</span></p></body></html>"))
        self.outboundinter_loc_input.setPlaceholderText(_translate("Dialog", "示例：[202.49, 1347.52, 2083.13]"))
        self.arterial_length_input.setPlaceholderText(_translate("Dialog", "示例：2500"))
        self.label_14.setText(_translate("Dialog", "绿波速度"))
        self.label_15.setText(_translate("Dialog", "侧街车道数"))
        self.veh_volumes_input.setPlaceholderText(_translate("Dialog", "示例：([1311, 866, 1430], [1480, 1788, 1012])"))
        self.arterial_lanenum_input.setPlaceholderText(_translate("Dialog", "示例：([3, 6, 8], [3, 7, 7])"))
        self.label_16.setText(_translate("Dialog", "采集周期"))
        self.green_speed_input.setPlaceholderText(_translate("Dialog", "示例：50"))
        self.label_10.setText(_translate("Dialog", "干线长度"))
        self.inboundinter_loc_input.setPlaceholderText(_translate("Dialog", "示例：[154.42, 1271.24, 1998.41]"))
        self.side_lanenum_input.setPlaceholderText(_translate("Dialog", "示例：[6, 10, 10]"))
        self.label_13.setText(_translate("Dialog", "上行交叉口位置"))
        self.label_18.setText(_translate("Dialog", "下行交叉口位置"))
        self.collect_data_period_input.setPlaceholderText(_translate("Dialog", "示例：3600"))

    # 存在配时文件则读取并设置
    def save_loadData(self):
        time = self.app_data.value('time')
        print(time)

        loadData = [self.app_data.value('cycle_input'),
                    self.app_data.value('offset_input'),
                    self.app_data.value('inbound_phase_input'),
                    self.app_data.value('outbound_phase_input'),
                    self.app_data.value('signal_RG1_input'),
                    self.app_data.value('signal_RG2_input'),
                    self.app_data.value('green_speed_input'),
                    self.app_data.value('collect_data_period_input'),
                    self.app_data.value('arterial_length_input'),
                    self.app_data.value('side_lanenum_input'),
                    self.app_data.value('arterial_lanenum_input'),
                    self.app_data.value('veh_volumes_input'),
                    self.app_data.value('inboundinter_loc_input'),
                    self.app_data.value('outboundinter_loc_input')]
        # 读取并设置
        loadDataType = [self.cycle_input.placeholderText(),
                        self.offset_input.placeholderText(),
                        self.inbound_phase_input.placeholderText(),
                        self.outbound_phase_input.placeholderText(),
                        self.signal_RG1_input.placeholderText(),
                        self.signal_RG2_input.placeholderText(),
                        self.green_speed_input.placeholderText(),
                        self.collect_data_period_input.placeholderText(),
                        self.arterial_length_input.placeholderText(),
                        self.side_lanenum_input.placeholderText(),
                        self.arterial_lanenum_input.placeholderText(),
                        self.veh_volumes_input.placeholderText(),
                        self.inboundinter_loc_input.placeholderText(),
                        self.outboundinter_loc_input.placeholderText()]

        if loadData != loadDataType:
            self.cycle_input.setText(loadData[0])
            self.offset_input.setText(loadData[1])
            self.inbound_phase_input.setText(loadData[2])
            self.outbound_phase_input.setText(loadData[3])
            self.signal_RG1_input.setText(loadData[4])
            self.signal_RG2_input.setText(loadData[5])
            self.green_speed_input.setText(loadData[6])
            self.collect_data_period_input.setText(loadData[7])
            self.arterial_length_input.setText(loadData[8])
            self.side_lanenum_input.setText(loadData[9])
            self.arterial_lanenum_input.setText(loadData[10])
            self.veh_volumes_input.setText(loadData[11])
            self.inboundinter_loc_input.setText(loadData[12])
            self.outboundinter_loc_input.setText(loadData[13])

    # 若第一次打开则初始化
    def init_loadData(self):
        time = QDateTime.currentDateTime()  # 获取当前时间，并存储在self.qpp_data
        self.app_data.setValue('time', time.toString())  # 数据0：time.toString()为字符串类型
        # 读取默认数据并存储
        # 数据地址
        self.app_data.setValue('inbound_trajectory_file_loc', '')
        self.app_data.setValue('outbound_trajectory_file_loc', '')

        # 配时数据
        self.cycle = self.cycle_input.placeholderText()
        self.app_data.setValue('cycle_input', self.cycle)

        self.offset = self.offset_input.placeholderText()
        self.app_data.setValue('offset_input', self.offset)

        self.inbound_phase = self.inbound_phase_input.placeholderText()
        self.app_data.setValue('inbound_phase_input', self.inbound_phase)

        self.outbound_phase = self.outbound_phase_input.placeholderText()
        self.app_data.setValue('outbound_phase_input', self.outbound_phase)

        self.signal_RG1 = self.signal_RG1_input.placeholderText()
        self.app_data.setValue('signal_RG1_input', self.signal_RG1)

        self.signal_RG2 = self.signal_RG2_input.placeholderText()
        self.app_data.setValue('signal_RG2_input', self.signal_RG2)

        # 干线数据
        self.green_speed = self.green_speed_input.placeholderText()
        self.app_data.setValue('green_speed_input', self.green_speed)

        self.collect_data_period = self.collect_data_period_input.placeholderText()
        self.app_data.setValue('collect_data_period_input', self.collect_data_period)

        self.arterial_length = self.arterial_length_input.placeholderText()
        self.app_data.setValue('arterial_length_input', self.arterial_length)

        self.side_lanenum = self.side_lanenum_input.placeholderText()
        self.app_data.setValue('side_lanenum_input', self.side_lanenum)

        self.arterial_lanenum = self.arterial_lanenum_input.placeholderText()
        self.app_data.setValue('arterial_lanenum_input', self.arterial_lanenum)

        self.veh_volume = self.veh_volumes_input.placeholderText()
        self.app_data.setValue('veh_volumes_input', self.veh_volume)

        self.inboundinter_loc = self.inboundinter_loc_input.placeholderText()
        self.app_data.setValue('inboundinter_loc_input', self.inboundinter_loc)

        self.outboundinter_loc = self.outboundinter_loc_input.placeholderText()
        self.app_data.setValue('outboundinter_loc_input', self.outboundinter_loc)

    @staticmethod
    def extract_file_name(path):
        return os.path.basename(path)

    # 设置读取文件位置槽函数
    def open_file_in(self):
        self.inbound_trajectory = order.selectFile("CSV文件 (*.csv)")  # 文件位置
        # 数据地址
        if self.inbound_trajectory is not None:
            # 显示文件名称
            _translate = QtCore.QCoreApplication.translate
            self.label.setText(_translate("Dialog", os.path.basename(self.inbound_trajectory[0])))
            self.label.setStyleSheet("QLabel {\n"
                                     "  font-size: 20px;\n"
                                     "  color: #2aa515;\n"
                                     "  background-color: #f9f9f9;\n"
                                     "  border: 2px solid #ccc;\n"
                                     "  padding: 10px;\n"
                                     "  border-radius: 5px;\n"
                                     "  transition: background-color 0.3s ease, color 0.3s ease; /* 平滑过渡 */\n"
                                     "}\n"
                                     "\n"
                                     "")
        print(self.inbound_trajectory)

    def open_file_out(self):
        self.outbound_trajectory = order.selectFile("CSV文件 (*.csv)")  # 文件位置
        if self.outbound_trajectory is not None:
            # 显示文件名称
            _translate = QtCore.QCoreApplication.translate
            self.label_2.setText(_translate("Dialog", os.path.basename(self.outbound_trajectory[0])))
            self.label_2.setStyleSheet("QLabel {\n"
                                       "  font-size: 20px;\n"
                                       "  color: #2aa515;\n"
                                       "  background-color: #f9f9f9;\n"
                                       "  border: 2px solid #ccc;\n"
                                       "  padding: 10px;\n"
                                       "  border-radius: 5px;\n"
                                       "  transition: background-color 0.3s ease, color 0.3s ease; /* 平滑过渡 */\n"
                                       "}\n"
                                       "\n"
                                       "")
        print(self.outbound_trajectory)

    # 判断点击的是哪个btn
    def reSetting(self, button):

        if button == self.buttonBox.button(QtWidgets.QDialogButtonBox.StandardButton.Ok):
            """
            判断输入值是否为空
            :return:
            """
            # 获取输入框数据
            loadData = [self.signal_RG1_input.text(), self.inbound_phase_input.text(), self.signal_RG2_input.text(),
                        self.offset_input.text(), self.outbound_phase_input.text(),
                        self.cycle_input.text(), self.veh_volumes_input.text(),
                        self.inboundinter_loc_input.text(), self.collect_data_period_input.text(),
                        self.arterial_length_input.text(),
                        self.side_lanenum_input.text(), self.outboundinter_loc_input.text(),
                        self.arterial_lanenum_input.text(), self.green_speed_input.text()]

            res = any(not element.strip() for element in loadData)  # 判断是否非空
            if res:
                QMessageBox.warning(self, "系统提示", "输入不能为空")
            elif self.label.text() == "no trajectory_data.csv":
                QMessageBox.warning(self, "系统提示", "数据文件不能为空")
            elif self.label_2.text() == "no trajectory_data.csv":
                QMessageBox.warning(self, "系统提示", "数据文件不能为空")
            else:
                # 判断格式
                # 写入配置文件
                if self.inbound_trajectory is not None:
                    self.app_data.setValue('inbound_trajectory_file_loc', self.inbound_trajectory[0])

                if self.outbound_trajectory is not None:
                    self.app_data.setValue('outbound_trajectory_file_loc', self.outbound_trajectory[0])

                are_all_lists = all(
                    isinstance(eval(loadData[i], {"__builtins__": {}}, {}), list) for i in [1, 3, 4, 5, 7, 10, 11])
                are_all_dir = all(
                    isinstance(eval(loadData[i], {"__builtins__": {}}, {}), dict) for i in [0, 2])
                are_all_int = all(
                    isinstance(eval(loadData[i], {"__builtins__": {}}, {}), int) for i in [8, 9, 13])
                are_all_tuple = all(
                    isinstance(eval(loadData[i], {"__builtins__": {}}, {}), tuple) for i in [6, 12])
                # 如果非空则关闭窗口并更新配置数据
                if are_all_lists and are_all_dir and are_all_int and are_all_tuple:
                    time = QDateTime.currentDateTime()  # 获取当前时间，并存储在self.qpp_data
                    self.app_data.setValue('time', time.toString())  # 数据0：time.toString()为字符串类型
                    # 读取默认数据并存储
                    loadDataStr = ['signal_RG1_input', 'inbound_phase_input', 'signal_RG2_input',
                                   'offset_input', 'outbound_phase_input', 'cycle_input', 'veh_volumes_input',
                                   'inboundinter_loc_input', 'collect_data_period_input', 'arterial_length_input'
                                                                                          'side_lanenum_input',
                                   'outboundinter_loc_input', 'arterial_lanenum_input',
                                   'green_speed_input']
                    for i in range(13):
                        self.app_data.setValue(loadDataStr[i], loadData[i])
                    self.close()
                else:
                    QMessageBox.warning(self, "系统提示", "数据格式有误！")


        else:
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = UpLoadData()
    ui.show()
    sys.exit(app.exec())
