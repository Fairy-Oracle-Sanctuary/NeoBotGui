# coding:utf-8
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QVBoxLayout, QWidget
from qfluentwidgets import ScrollArea

from ..components.info_card import FairyKekkaiWorkshopInfoCard
from ..components.sample_card import SampleCardView


class HomeInterface(ScrollArea):
    """Home interface"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.view = QWidget(self)
        self.loadProgressInfoBar = None
        self.installProgressInfoBar = None

        self.fairyKekkaiWorkshopInfoCard = FairyKekkaiWorkshopInfoCard(self.view)

        self.vBoxLayout = QVBoxLayout(self.view)

        self._initWidget()
        self.loadSamples()
        # self._connectSignalToSlot()

    def _initWidget(self):
        self.setWidget(self.view)
        self.setAcceptDrops(True)
        self.setWidgetResizable(True)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.vBoxLayout.setSpacing(10)
        self.vBoxLayout.setContentsMargins(0, 0, 10, 10)
        self.vBoxLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.vBoxLayout.addWidget(
            self.fairyKekkaiWorkshopInfoCard, 0, Qt.AlignmentFlag.AlignTop
        )

        self.resize(780, 800)
        self.setObjectName("HomeInterface")
        self.enableTransparentBackground()

        # self._connectSignalToSlot()

    def loadSamples(self):
        """load samples"""
        # basic input samples
        basicInputView = SampleCardView(self.tr("指令一览"), self.view)
        basicInputView.addSampleCard(
            icon=QIcon(":/app/images/logo/bilibili.svg"),
            title="bili_parser:",
            content=self.tr(
                "功能: 自动解析B站分享卡片，提取视频封面和播放量等信息。\n用法: （自动触发）当检测到B站小程序分享卡片时，自动发送视频信息。"
            ),
            routeKey="ProjectStackedInterface",
            index=1,
        )
        basicInputView.addSampleCard(
            icon=QIcon(":/app/images/logo/thpic.svg"),
            title="thpic:",
            content=self.tr(
                "功能: 来看看东方Project的图片吧！\n用法: /thpic [nums](1~10)"
            ),
            routeKey="ProjectStackedInterface",
            index=2,
        )
        basicInputView.addSampleCard(
            icon=QIcon(":/app/images/logo/jrcd.svg"),
            title="jrcd:",
            content=self.tr("功能: 来看看你的长度吧！\n用法: /jrcd\n/bbcd [@某人]"),
            routeKey="ProjectStackedInterface",
            index=3,
        )
        basicInputView.addSampleCard(
            icon=QIcon(":/app/images/logo/furry.svg"),
            title="furry:",
            content=self.tr(
                "功能: 处理 /furry 指令，发送furry图片\n用法: /furry - 发送一条furry图"
            ),
            routeKey="ProjectStackedInterface",
            index=4,
        )
        basicInputView.addSampleCard(
            icon=QIcon(":/app/images/logo/echo.svg"),
            title="echo:",
            content=self.tr(
                "功能: 提供 echo 和 赞我 功能\n用法: /echo [内容] - 复读内容\n/赞我 - 让机器人给你点赞"
            ),
            routeKey="ProjectStackedInterface",
            index=5,
        )
        basicInputView.addSampleCard(
            icon=QIcon(":/app/images/logo/python.svg"),
            title="Python 代码执行:",
            content=self.tr(
                "功能: 在安全的沙箱环境中执行 Python 代码片段，支持单行、多行和转发回复。\n用法: /py <单行代码>\n/code_py <单行代码>\n/py (进入多行输入模式)"
            ),
            routeKey="ProjectStackedInterface",
            index=6,
        )

        self.vBoxLayout.addWidget(basicInputView)
