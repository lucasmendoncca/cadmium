# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pagesDxpWFC.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *

class Ui_AppPages(object):
    def setupUi(self, AppPages):
        if not AppPages.objectName():
            AppPages.setObjectName(u"AppPages")
        AppPages.resize(709, 593)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.verticalLayout = QVBoxLayout(self.page_1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.page_1)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(500, 300))
        self.frame.setMaximumSize(QSize(500, 300))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setSpacing(4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_dir_vid = QPushButton(self.frame)
        self.btn_dir_vid.setObjectName(u"btn_dir_vid")
        self.btn_dir_vid.setMinimumSize(QSize(50, 36))
        self.btn_dir_vid.setMaximumSize(QSize(16777215, 36))
        self.btn_dir_vid.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(73, 73, 109);\n"
"	padding: 8px;\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(76, 130, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(41, 83, 124);\n"
"}")

        self.gridLayout.addWidget(self.btn_dir_vid, 1, 1, 1, 1)

        self.line_dir_model = QLineEdit(self.frame)
        self.line_dir_model.setObjectName(u"line_dir_model")
        self.line_dir_model.setMinimumSize(QSize(0, 36))
        self.line_dir_model.setMaximumSize(QSize(16777215, 36))
        self.line_dir_model.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(68, 71, 90);\n"
"	padding: 8px;\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}")

        self.gridLayout.addWidget(self.line_dir_model, 0, 0, 1, 1)

        self.btn_dir_model = QPushButton(self.frame)
        self.btn_dir_model.setObjectName(u"btn_dir_model")
        self.btn_dir_model.setMinimumSize(QSize(50, 36))
        self.btn_dir_model.setMaximumSize(QSize(16777215, 36))
        self.btn_dir_model.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(73, 73, 109);\n"
"	padding: 8px;\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(76, 130, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(41, 83, 124);\n"
"}")

        self.gridLayout.addWidget(self.btn_dir_model, 0, 1, 1, 1)

        self.line_dir_video = QLineEdit(self.frame)
        self.line_dir_video.setObjectName(u"line_dir_video")
        self.line_dir_video.setMinimumSize(QSize(0, 36))
        self.line_dir_video.setMaximumSize(QSize(16777215, 36))
        self.line_dir_video.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(68, 71, 90);\n"
"	padding: 8px;\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}")

        self.gridLayout.addWidget(self.line_dir_video, 1, 0, 1, 1)

        self.btn_start = QPushButton(self.frame)
        self.btn_start.setObjectName(u"btn_start")
        self.btn_start.setMinimumSize(QSize(0, 36))
        self.btn_start.setMaximumSize(QSize(16777215, 36))
        self.btn_start.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(73, 73, 109);\n"
"	padding: 8px;\n"
"	border: 2px solid #c3ccdf;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(76, 130, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(41, 83, 124);\n"
"}")

        self.gridLayout.addWidget(self.btn_start, 2, 0, 1, 2)


        self.verticalLayout_4.addLayout(self.gridLayout)


        self.verticalLayout.addWidget(self.frame, 0, Qt.AlignHCenter)

        AppPages.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_2 = QVBoxLayout(self.page_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.page_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAutoFillBackground(False)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        AppPages.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_3 = QVBoxLayout(self.page_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.page_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_3)

        AppPages.addWidget(self.page_3)

        self.retranslateUi(AppPages)

        QMetaObject.connectSlotsByName(AppPages)
    # setupUi

    def retranslateUi(self, AppPages):
        AppPages.setWindowTitle(QCoreApplication.translate("AppPages", u"StackedWidget", None))
        self.btn_dir_vid.setText(QCoreApplication.translate("AppPages", u"Abrir", None))
        self.line_dir_model.setPlaceholderText(QCoreApplication.translate("AppPages", u"Diret\u00f3rio do modelo", None))
        self.btn_dir_model.setText(QCoreApplication.translate("AppPages", u"Abrir", None))
        self.line_dir_video.setPlaceholderText(QCoreApplication.translate("AppPages", u"Diret\u00f3rio do v\u00eddeo", None))
        self.btn_start.setText(QCoreApplication.translate("AppPages", u"Iniciar", None))
        self.label_2.setText(QCoreApplication.translate("AppPages", u"Treinamento", None))
        self.label_3.setText(QCoreApplication.translate("AppPages", u"Configura\u00e7\u00e3o", None))
    # retranslateUi

