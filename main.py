import GlobalData
#软件头文件先初始化全局数据
GlobalData.Init()

#软件程序逻辑
import sys
from PyQt5.QtWidgets import QApplication
from PY_MenuWidget import MenuWidget

if __name__ == '__main__':
    # 测试Github
    App = QApplication(sys.argv)
    MainWindow = MenuWidget()
    MainWindow.show()
    sys.exit(App.exec_())