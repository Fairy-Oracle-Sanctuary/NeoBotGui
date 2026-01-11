# coding:utf-8
# from ..common.signal_bus import signalBus
# from ..common.icon import Logo

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget
from qfluentwidgets import (
    BodyLabel,
    CaptionLabel,
    CardWidget,
    ComboBoxSettingCard,
    ExpandLayout,
    IconWidget,
    PrimaryPushSettingCard,
    PushButton,
    ScrollArea,
    TitleLabel,
    setFont,
    setTheme,
    setThemeColor,
)
from qfluentwidgets import FluentIcon as FIF
from qfluentwidgets import SettingCardGroup as CardGroup
from qframelesswindow.utils import getSystemAccentColor

from ..common.config import cfg
from ..common.setting import TEAM, VERSION, YEAR


class DetectionCard(CardWidget):
    def __init__(self, icon, title, content, parent=None):
        super().__init__(parent)
        self.iconWidget = IconWidget(icon)
        self.titleLabel = BodyLabel(title, self)
        self.contentLabel = CaptionLabel(content, self)
        self.openButton = PushButton("检测", self)

        self.hBoxLayout = QHBoxLayout(self)
        self.vBoxLayout = QVBoxLayout()

        self.setFixedHeight(73)
        self.iconWidget.setFixedSize(16, 16)
        self.contentLabel.setTextColor("#606060", "#d2d2d2")
        self.openButton.setFixedWidth(130)

        self.hBoxLayout.setContentsMargins(20, 11, 11, 11)
        self.hBoxLayout.setSpacing(15)
        self.hBoxLayout.addWidget(self.iconWidget)

        self.vBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.vBoxLayout.setSpacing(0)
        self.vBoxLayout.addWidget(self.titleLabel, 0, Qt.AlignVCenter)
        self.vBoxLayout.addWidget(self.contentLabel, 0, Qt.AlignVCenter)
        self.vBoxLayout.setAlignment(Qt.AlignVCenter)
        self.hBoxLayout.addLayout(self.vBoxLayout)

        self.hBoxLayout.addStretch(1)
        self.hBoxLayout.addWidget(self.openButton, 0, Qt.AlignRight)
        self.hBoxLayout.addSpacing(5)

        self.setClickEnabled(False)


class SettingCardGroup(CardGroup):
    def __init__(self, title: str, parent=None):
        super().__init__(title, parent)
        setFont(self.titleLabel, 14, QFont.Weight.DemiBold)


class SettingInterface(ScrollArea):
    """Setting interface"""

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.scrollWidget = QWidget()
        self.expandLayout = ExpandLayout(self.scrollWidget)

        # setting label
        self.settingLabel = TitleLabel(self.tr("设置"), self)

        # 个性化
        self.personalGroup = SettingCardGroup(self.tr("个性化"), self.scrollWidget)
        self.themeCard = ComboBoxSettingCard(
            cfg.themeMode,
            FIF.BRUSH,
            self.tr("应用主题"),
            self.tr("调整应用的外观"),
            texts=[self.tr("浅色"), self.tr("深色"), self.tr("跟随系统设置")],
            parent=self.personalGroup,
        )
        self.accentColorCard = ComboBoxSettingCard(
            cfg.accentColor,
            FIF.PALETTE,
            self.tr("主题色"),
            self.tr("调整应用的主题颜色"),
            texts=[self.tr("海沫绿"), self.tr("跟随系统设置")],
            parent=self.personalGroup,
        )
        self.zoomCard = ComboBoxSettingCard(
            cfg.dpiScale,
            FIF.ZOOM,
            self.tr("界面缩放"),
            self.tr("调整组件和字体的大小"),
            texts=["100%", "125%", "150%", "175%", "200%", self.tr("跟随系统设置")],
            parent=self.personalGroup,
        )

        # 关于
        self.aboutGroup = SettingCardGroup(self.tr("关于"), self.scrollWidget)
        self.aboutCard = PrimaryPushSettingCard(
            self.tr("检查更新"),
            ":/app/images/logo.png",
            self.tr("关于"),
            "🄯 "
            + self.tr("Copyleft")
            + f" {YEAR}, {TEAM}. "
            + self.tr("当前版本")
            + " v"
            + VERSION,
            self.aboutGroup,
        )

        self.__initWidget()

    def __initWidget(self):
        self.resize(1000, 800)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setViewportMargins(0, 90, 0, 20)
        self.setWidget(self.scrollWidget)
        self.setWidgetResizable(True)
        self.setObjectName("settingInterface")

        # initialize style sheet
        setFont(self.settingLabel, 23, QFont.Weight.DemiBold)
        self.enableTransparentBackground()

        # initialize layout
        self.__initLayout()
        self._connectSignalToSlot()

    def __initLayout(self):
        self.settingLabel.move(36, 40)

        self.personalGroup.addSettingCard(self.themeCard)
        self.personalGroup.addSettingCard(self.zoomCard)
        self.personalGroup.addSettingCard(self.accentColorCard)

        self.aboutGroup.addSettingCard(self.aboutCard)

        # add setting card group to layout
        self.expandLayout.setSpacing(26)
        self.expandLayout.setContentsMargins(36, 10, 36, 0)
        self.expandLayout.addWidget(self.personalGroup)
        self.expandLayout.addWidget(self.aboutGroup)

    def _onAccentColorChanged(self):
        color = cfg.get(cfg.accentColor)
        if color != "Auto":
            setThemeColor(color, save=False)
        else:
            sysColor = getSystemAccentColor()
            if sysColor.isValid():
                setThemeColor(sysColor, save=False)
            else:
                setThemeColor(color, save=False)

    def _connectSignalToSlot(self):
        """绑定信号"""
        # 个性化
        cfg.themeChanged.connect(setTheme)
        cfg.accentColor.valueChanged.connect(self._onAccentColorChanged)

        # 检查更新
        # self.aboutCard.clicked.connect(event_bus.checkUpdateSig)
