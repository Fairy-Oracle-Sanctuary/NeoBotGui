import sys

from PySide6.QtWidgets import QApplication

from app.view.main_window import MainWindow


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("NeoBotGui")

    # 创建并显示主窗口
    window = MainWindow()
    window.show()

    # 运行应用程序
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())

# Fairy-Kekkai-Workshop
