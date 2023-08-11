# ///////////////////////////////////////////////////////////////
# LUCAS MENDONCA
# MADE WITH Qt Designer and PySide6
# V: 1.0.0
# ///////////////////////////////////////////////////////////////

# IMPORT MODULES
import sys
import os
from typing import Optional

import PySide6.QtCore
import PySide6.QtWidgets 

# IMPORT QT CORE
from qt_core import *

# IMPORT MAIN WINDOW
from gui import UI_MainWindow

# MAIN WINDOW
class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        
        self.setWindowTitle("Cadmium MVS")
        
        # SET UP MAIN WINDOW
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)
        
        # Toggle Button
        self.ui.toggle_button.clicked.connect(self.toggle_button)
        
         # Btn home
        self.ui.btn_1.clicked.connect(self.show_page_1)

        # Btn widgets
        self.ui.btn_2.clicked.connect(self.show_page_2)

        # Btn settings
        self.ui.settings_btn.clicked.connect(self.show_page_3)
        
        # Show app        
        self.show()
            
    # Reset BTN Selection
    def reset_selection(self):
        for btn in self.ui.left_menu.findChildren(QPushButton):
            try:
                btn.set_active(False)
            except:
                pass
    
    # Btn home function
    def show_page_1(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_1)
        self.ui.btn_1.set_active(True)

    # Btn widgets function
    def show_page_2(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_2)
        self.ui.btn_2.set_active(True)

    # Btn pase gettings
    def show_page_3(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_3)
        self.ui.settings_btn.set_active(True)

    def toggle_button(self):
        # Get menu width
        menu_width = self.ui.left_menu.width()
        
        # Check width
        width = 50
        if menu_width == 50:
            width = 240
        
        # animation
        self.animation = QPropertyAnimation(self.ui.left_menu, b"minimumWidth")
        self.animation.setStartValue(menu_width)
        self.animation.setEndValue(width)
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.InOutCubic)
        self.animation.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())