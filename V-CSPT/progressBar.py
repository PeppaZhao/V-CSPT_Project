import sys
import threading
import time
from PyQt6.QtCore import pyqtSignal, QObject, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QProgressBar, \
    QMessageBox, QLineEdit, QStyleFactory


class PercentageWorker(QObject):
    percentageChanged = pyqtSignal(int)

    def __init__(self, fake_flag=False, parent=None):
        super().__init__(parent)
        self._percentage = 0
        self.fake_flag = fake_flag

    @property
    def percentage(self):
        return self._percentage

    @percentage.setter
    def percentage(self, value):
        if self.fake_flag:
            return
        if self._percentage == value:
            return
        self._percentage = value
        self.percentageChanged.emit(self.percentage)


def user_defined_function(a=1, b=2, worker=None):
    """
    自定义函数
    """
    if worker is None:
        worker = PercentageWorker(fake_flag=True)

    # part1
    v1 = a * 10
    time.sleep(2)
    print('part1_end')
    worker.percentage = 1

    # part2
    v2 = b * 10
    time.sleep(2)
    print('part2_end')
    worker.percentage = 2

    # part3
    time.sleep(2)
    print('part3_end')
    worker.percentage = 3


class MyUi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(700, 700)

        self.button1 = QPushButton(self)
        self.button1.setText('点击运行程序')
        self.button1.move(20, 20)
        self.button1.resize(200, 40)

        self.progressbar = QProgressBar(self)
        self.progressbar.move(20, 100)
        self.progressbar.resize(400, 30)

        print(f'minimum: {self.progressbar.minimum()}, maximum: {self.progressbar.maximum()}')

        self.button1.clicked.connect(self.run_all)
        # self.progressbar.hide()

        self.pushbutton1 = QPushButton(self)
        self.pushbutton2 = QPushButton(self)
        self.pushbutton3 = QPushButton(self)
        self.pushbutton4 = QPushButton(self)
        self.pushbutton5 = QPushButton(self)
        self.pushbutton6 = QPushButton(self)
        self.lineedit1 = QLineEdit(self)
        self.lineedit2 = QLineEdit(self)
        self._init_prepare()

    def _init_prepare(self):
        self.lineedit1.move(120, 200)
        self.lineedit2.move(350, 200)
        self.lineedit1.resize(200, 30)
        self.lineedit2.resize(200, 30)

        self.pushbutton1.move(120, 250)
        self.pushbutton2.move(350, 250)
        self.pushbutton3.move(120, 300)
        self.pushbutton4.move(350, 300)
        self.pushbutton5.move(120, 350)
        self.pushbutton6.move(350, 350)

        self.pushbutton1.resize(200, 30)
        self.pushbutton2.resize(200, 30)
        self.pushbutton3.resize(200, 30)
        self.pushbutton4.resize(200, 30)
        self.pushbutton5.resize(200, 30)
        self.pushbutton6.resize(200, 30)

        self.lineedit1.setText(str(self.progressbar.alignment()))
        self.lineedit2.setText(str(self.progressbar.format()))
        self.pushbutton1.setText('设置为垂直进度条')
        self.pushbutton1.clicked.connect(self.vertical_progressbar)
        self.pushbutton2.setText('设置为水平进度条')
        self.pushbutton2.clicked.connect(self.horizontal_progressbar)
        self.pushbutton3.setText('水平进度条清空格式')
        self.pushbutton3.clicked.connect(self.about_resetformat)
        self.pushbutton4.setText('水平进度条不显示文本')
        self.pushbutton4.clicked.connect(self.about_notext)
        self.pushbutton5.setText('水平进度条清空值')
        self.pushbutton5.clicked.connect(self.about_reset)
        self.pushbutton6.setText('水平进度条 min=max=0')
        self.pushbutton6.clicked.connect(self.about_zero)

        self.progressbar.setRange(0, 100)
        self.progressbar.setValue(30)

    def vertical_progressbar(self):
        self.progressbar.show()
        self.progressbar.setOrientation(Qt.Orientation.Vertical)
        self.progressbar.resize(30, 400)
        self.progressbar.setStyle(QStyleFactory.create('windows'))
        self.progressbar.setAlignment(Qt.AlignmentFlag.AlignCenter)  # 无变化，windows样式下 垂直进度条不显示文本
        self.progressbar.setTextDirection(QProgressBar.Direction.TopToBottom)  # 无变化，windows样式下 垂直进度条不显示文本
        self.progressbar.setTextVisible(True)  # 无变化，windows样式下 垂直进度条不显示文本
        self.progressbar.setRange(0, 100)
        self.progressbar.setValue(50)
        self.lineedit1.setText(str(self.progressbar.text()))
        self.lineedit2.setText(str(self.progressbar.value()))
        print(f'text: {self.progressbar.text()}, value: {self.progressbar.value()}')

    def horizontal_progressbar(self):
        self.progressbar.show()
        self.progressbar.setOrientation(Qt.Orientation.Horizontal)
        self.progressbar.resize(400, 30)
        self.progressbar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.progressbar.setTextVisible(True)
        self.progressbar.setFormat('运行进度: %p%')
        print(self.progressbar.format())
        # self.progressbar.setStyle(QStyleFactory.create('windowsvista'))
        self.progressbar.setStyle(QStyleFactory.create('Windows'))
        # self.progressbar.setStyle(QStyleFactory.create('Fusion'))
        self.progressbar.setRange(0, 100)
        self.progressbar.setValue(60)
        self.lineedit1.setText(str(self.progressbar.text()))
        self.lineedit2.setText(str(self.progressbar.value()))
        print(f'text: {self.progressbar.text()}, value: {self.progressbar.value()}')

    def about_resetformat(self):
        self.horizontal_progressbar()
        self.progressbar.resetFormat()

    def about_notext(self):
        print(self.progressbar.isTextVisible())
        self.horizontal_progressbar()
        self.progressbar.setTextVisible(False)
        print(self.progressbar.isTextVisible())

    def about_reset(self):
        self.horizontal_progressbar()
        self.progressbar.reset()

    def about_zero(self):
        self.horizontal_progressbar()
        self.progressbar.setRange(0, 0)

    def update_progress(self, value):
        self.progressbar.setValue(value)
        if self.progressbar.value() == self.progressbar.maximum():
            self.progressbar.hide()
            QMessageBox.information(self, '通知', '程序运行结束')

    def run_all(self):
        self.progressbar.setMinimum(0)
        self.progressbar.setMaximum(3)
        self.progressbar.show()
        worker = PercentageWorker(fake_flag=False)
        worker.percentageChanged.connect(self.update_progress)
        threading.Thread(
            target=user_defined_function,
            args=(2,),
            kwargs=dict(b=4, worker=worker),
            daemon=True,
        ).start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    print(QStyleFactory.keys())
    app.setStyle(QStyleFactory.create('Fusion'))
    w = MyUi()
    w.show()
    sys.exit(app.exec())
