import sys
import random
from time import sleep
from choujiang import Ui_MainWindow
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox,QGraphicsOpacityEffect
from PyQt5.QtCore import QThread,QTimer,pyqtSignal
from PyQt5.QtGui import QIcon

class WorkThread(QThread):
    # 初始化线程
    sinout = pyqtSignal(str)
    def __int__(self,x=10):
        super(WorkThread, self).__init__()
        self.working = False
        self.n = x
    #线程运行函数
    def run(self):
        global num_1
        if isinstance(num_1,int) is False:
            num_1 = 10
        while self.working == True:
            T_value = random.randint(1, num_1)
            self.sinout.emit(str(T_value))
            sleep(0.05)


class WorkThread2(QThread):
    # 初始化线程
    sinout = pyqtSignal(str)
    def __int__(self,x=30):
        super(WorkThread, self).__init__()
        self.working = True
        self.n = x
    #线程运行函数
    def run(self):
        global num_2
        if isinstance(num_2,int) is False:
            num_2 = 30

        while self.working == True:
            T_value = random.randint(1,num_2)
            self.sinout.emit(str(T_value))
            sleep(0.05)




class MyMainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.textBrowser.setPlainText('-')
        self.textBrowser_2.setPlainText('-')
        # self.textBrowser_3.setPlainText('')
        self.flag = -1
        self.b1 = -1
        self.b2 = -1
        self.pushButton_4.clicked.connect(self.button)
        self.pushButton.clicked.connect(self.button1_start)
        # self.Mytimer()
        self.pushButton_2.clicked.connect(self.button2_start)
        self.lineEdit.setPlaceholderText('10')
        self.lineEdit_2.setPlaceholderText('30')

    def button(self):
        num1 = self.lineEdit.text()
        num2 = self.lineEdit.text()
        global num_1
        try:
            num_1 = int(num1)
        except:
            num_1 = 10
        global num_2
        try:
            num_2 = int(num2)
        except:
            num_2 = 30
        self.workThread = WorkThread()
        self.workThread2 = WorkThread2()
        self.workThread.working = True
        self.workThread.start()
        self.workThread.sinout.connect(self.update)
        self.workThread2.working = True
        self.workThread2.start()
        self.workThread2.sinout.connect(self.update2)

    def button1_start(self):
        self.workThread.working = False
        self.workThread.wait()
        # print(self.num1)

    def update(self,num):
        self.textBrowser.setPlainText(num)

    def button2_start(self):
        # self.pushButton.setText("开始")
        self.workThread2.working = False
        self.workThread.wait()
        ss = self.textBrowser.toPlainText() + '桌，' + self.textBrowser_2.toPlainText() + '号'
        self.listWidget.addItem(ss)



    def update2(self,num):
        self.textBrowser_2.setPlainText(num)


if __name__=="__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())