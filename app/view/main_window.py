# coding: utf-8
import sys

from PySide6.QtGui import QIcon  # noqa
from PySide6.QtWidgets import QApplication
from qfluentwidgets import FluentIcon as FIF
from qfluentwidgets import FluentWindow, NavigationItemPosition

from .home_interface import HomeInterface
from .setting_interface import SettingInterface


class MainWindow(FluentWindow):
    def __init__(self):
        super().__init__()

        self._initWindow()

        # 创建页面
        self.homeInterface = HomeInterface(self)
        self.settingInterface = SettingInterface(self)

        self.initNavigation()

    def _initWindow(self):
        self.resize(960, 754 if sys.platform == "win32" else 773)
        self.setMinimumWidth(760)
        self.setWindowIcon(QIcon(":/app/images/logo.png"))
        self.setWindowTitle("NeoBotGui")

        desktop = QApplication.primaryScreen().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)

    def initNavigation(self):
        self.addSubInterface(self.homeInterface, FIF.HOME, "主页")

        self.addSubInterface(
            self.settingInterface,
            FIF.SETTING,
            "设置",
            NavigationItemPosition.BOTTOM,
        )
