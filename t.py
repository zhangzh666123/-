# -*- coding: utf-8 -*-
from PyQt6 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)
test_window = QtWidgets.QWidget()
test_window.resize(500,500)
test_window.setWindowTitle("测试窗口")
test_window.show()
sys.exit(app.exec())
