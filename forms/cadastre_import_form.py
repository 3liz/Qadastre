# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/cadastre_import_form.ui'
#
# Created: Wed Oct 30 17:26:24 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_cadastre_import_form(object):
    def setupUi(self, cadastre_import_form):
        cadastre_import_form.setObjectName(_fromUtf8("cadastre_import_form"))
        cadastre_import_form.resize(525, 642)
        self.verticalLayout = QtGui.QVBoxLayout(cadastre_import_form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.scrollArea = QtGui.QScrollArea(cadastre_import_form)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 489, 686))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.groupBox = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.liDbType = QtGui.QComboBox(self.groupBox)
        self.liDbType.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.liDbType.setObjectName(_fromUtf8("liDbType"))
        self.liDbType.addItem(_fromUtf8(""))
        self.liDbType.addItem(_fromUtf8(""))
        self.liDbType.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.liDbType, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.liDbConnection = QtGui.QComboBox(self.groupBox)
        self.liDbConnection.setObjectName(_fromUtf8("liDbConnection"))
        self.gridLayout.addWidget(self.liDbConnection, 0, 3, 1, 1)
        self.verticalLayout_7.addLayout(self.gridLayout)
        self.databaseSpecificOptions = QtGui.QToolBox(self.groupBox)
        self.databaseSpecificOptions.setObjectName(_fromUtf8("databaseSpecificOptions"))
        self.tabPostgis = QtGui.QWidget()
        self.tabPostgis.setGeometry(QtCore.QRect(0, 0, 445, 73))
        self.tabPostgis.setObjectName(_fromUtf8("tabPostgis"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tabPostgis)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(self.tabPostgis)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.liDbSchema = QtGui.QComboBox(self.tabPostgis)
        self.liDbSchema.setEnabled(False)
        self.liDbSchema.setObjectName(_fromUtf8("liDbSchema"))
        self.horizontalLayout_3.addWidget(self.liDbSchema)
        self.inDbCreateSchema = QtGui.QLineEdit(self.tabPostgis)
        self.inDbCreateSchema.setEnabled(False)
        self.inDbCreateSchema.setMaximumSize(QtCore.QSize(100, 16777215))
        self.inDbCreateSchema.setObjectName(_fromUtf8("inDbCreateSchema"))
        self.horizontalLayout_3.addWidget(self.inDbCreateSchema)
        self.btDbCreateSchema = QtGui.QPushButton(self.tabPostgis)
        self.btDbCreateSchema.setEnabled(False)
        self.btDbCreateSchema.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btDbCreateSchema.setObjectName(_fromUtf8("btDbCreateSchema"))
        self.horizontalLayout_3.addWidget(self.btDbCreateSchema)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.databaseSpecificOptions.addItem(self.tabPostgis, _fromUtf8(""))
        self.tabSpatialite = QtGui.QWidget()
        self.tabSpatialite.setGeometry(QtCore.QRect(0, 0, 445, 73))
        self.tabSpatialite.setObjectName(_fromUtf8("tabSpatialite"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tabSpatialite)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_7 = QtGui.QLabel(self.tabSpatialite)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_2.addWidget(self.label_7)
        self.btCreateNewSpatialiteDb = QtGui.QPushButton(self.tabSpatialite)
        self.btCreateNewSpatialiteDb.setObjectName(_fromUtf8("btCreateNewSpatialiteDb"))
        self.verticalLayout_2.addWidget(self.btCreateNewSpatialiteDb)
        self.databaseSpecificOptions.addItem(self.tabSpatialite, _fromUtf8(""))
        self.verticalLayout_7.addWidget(self.databaseSpecificOptions)
        self.verticalLayout_6.addWidget(self.groupBox)
        self.groupBox_5 = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.verticalLayout_13 = QtGui.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_11 = QtGui.QLabel(self.groupBox_5)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_8.addWidget(self.label_11)
        self.inEdigeoSourceDir = QtGui.QLineEdit(self.groupBox_5)
        self.inEdigeoSourceDir.setObjectName(_fromUtf8("inEdigeoSourceDir"))
        self.horizontalLayout_8.addWidget(self.inEdigeoSourceDir)
        self.btEdigeoSourceDir = QtGui.QToolButton(self.groupBox_5)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/cadastre/icons/open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btEdigeoSourceDir.setIcon(icon)
        self.btEdigeoSourceDir.setObjectName(_fromUtf8("btEdigeoSourceDir"))
        self.horizontalLayout_8.addWidget(self.btEdigeoSourceDir)
        self.verticalLayout_13.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_12 = QtGui.QLabel(self.groupBox_5)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_9.addWidget(self.label_12)
        self.inEdigeoSourceProj = QtGui.QLineEdit(self.groupBox_5)
        self.inEdigeoSourceProj.setObjectName(_fromUtf8("inEdigeoSourceProj"))
        self.horizontalLayout_9.addWidget(self.inEdigeoSourceProj)
        self.btEdigeoSourceProj = QtGui.QPushButton(self.groupBox_5)
        self.btEdigeoSourceProj.setMaximumSize(QtCore.QSize(30, 16777215))
        self.btEdigeoSourceProj.setObjectName(_fromUtf8("btEdigeoSourceProj"))
        self.horizontalLayout_9.addWidget(self.btEdigeoSourceProj)
        self.label_13 = QtGui.QLabel(self.groupBox_5)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_9.addWidget(self.label_13)
        self.inEdigeoTargetProj = QtGui.QLineEdit(self.groupBox_5)
        self.inEdigeoTargetProj.setObjectName(_fromUtf8("inEdigeoTargetProj"))
        self.horizontalLayout_9.addWidget(self.inEdigeoTargetProj)
        self.btEdigeoTargetProj = QtGui.QPushButton(self.groupBox_5)
        self.btEdigeoTargetProj.setMaximumSize(QtCore.QSize(30, 16777215))
        self.btEdigeoTargetProj.setObjectName(_fromUtf8("btEdigeoTargetProj"))
        self.horizontalLayout_9.addWidget(self.btEdigeoTargetProj)
        self.verticalLayout_13.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_4 = QtGui.QLabel(self.groupBox_5)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_10.addWidget(self.label_4)
        self.inEdigeoDepartement = QtGui.QLineEdit(self.groupBox_5)
        self.inEdigeoDepartement.setInputMask(_fromUtf8(""))
        self.inEdigeoDepartement.setMaxLength(2)
        self.inEdigeoDepartement.setObjectName(_fromUtf8("inEdigeoDepartement"))
        self.horizontalLayout_10.addWidget(self.inEdigeoDepartement)
        self.label_5 = QtGui.QLabel(self.groupBox_5)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_10.addWidget(self.label_5)
        self.inEdigeoDirection = QtGui.QLineEdit(self.groupBox_5)
        self.inEdigeoDirection.setInputMask(_fromUtf8(""))
        self.inEdigeoDirection.setMaxLength(32767)
        self.inEdigeoDirection.setObjectName(_fromUtf8("inEdigeoDirection"))
        self.horizontalLayout_10.addWidget(self.inEdigeoDirection)
        self.verticalLayout_13.addLayout(self.horizontalLayout_10)
        self.verticalLayout_6.addWidget(self.groupBox_5)
        self.groupBox_6 = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.verticalLayout_14 = QtGui.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_14.setObjectName(_fromUtf8("verticalLayout_14"))
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label_14 = QtGui.QLabel(self.groupBox_6)
        self.label_14.setEnabled(True)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.horizontalLayout_11.addWidget(self.label_14)
        self.inMajicSourceDir = QtGui.QLineEdit(self.groupBox_6)
        self.inMajicSourceDir.setEnabled(True)
        self.inMajicSourceDir.setObjectName(_fromUtf8("inMajicSourceDir"))
        self.horizontalLayout_11.addWidget(self.inMajicSourceDir)
        self.btMajicSourceDir = QtGui.QToolButton(self.groupBox_6)
        self.btMajicSourceDir.setIcon(icon)
        self.btMajicSourceDir.setObjectName(_fromUtf8("btMajicSourceDir"))
        self.horizontalLayout_11.addWidget(self.btMajicSourceDir)
        self.verticalLayout_14.addLayout(self.horizontalLayout_11)
        self.verticalLayout_6.addWidget(self.groupBox_6)
        self.groupBox_7 = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.verticalLayout_15 = QtGui.QVBoxLayout(self.groupBox_7)
        self.verticalLayout_15.setObjectName(_fromUtf8("verticalLayout_15"))
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.label_15 = QtGui.QLabel(self.groupBox_7)
        self.label_15.setEnabled(True)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.horizontalLayout_12.addWidget(self.label_15)
        self.inDataVersion = QtGui.QSpinBox(self.groupBox_7)
        self.inDataVersion.setMinimum(2011)
        self.inDataVersion.setMaximum(2013)
        self.inDataVersion.setProperty("value", 2013)
        self.inDataVersion.setObjectName(_fromUtf8("inDataVersion"))
        self.horizontalLayout_12.addWidget(self.inDataVersion)
        self.label_16 = QtGui.QLabel(self.groupBox_7)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.horizontalLayout_12.addWidget(self.label_16)
        self.inDataYear = QtGui.QSpinBox(self.groupBox_7)
        self.inDataYear.setEnabled(True)
        self.inDataYear.setMinimum(2010)
        self.inDataYear.setMaximum(2020)
        self.inDataYear.setProperty("value", 2013)
        self.inDataYear.setObjectName(_fromUtf8("inDataYear"))
        self.horizontalLayout_12.addWidget(self.inDataYear)
        self.label_6 = QtGui.QLabel(self.groupBox_7)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_12.addWidget(self.label_6)
        self.inEdigeoLot = QtGui.QLineEdit(self.groupBox_7)
        self.inEdigeoLot.setMaxLength(3)
        self.inEdigeoLot.setObjectName(_fromUtf8("inEdigeoLot"))
        self.horizontalLayout_12.addWidget(self.inEdigeoLot)
        self.verticalLayout_15.addLayout(self.horizontalLayout_12)
        self.verticalLayout_6.addWidget(self.groupBox_7)
        self.btProcessImport = QtGui.QPushButton(self.scrollAreaWidgetContents_2)
        self.btProcessImport.setObjectName(_fromUtf8("btProcessImport"))
        self.verticalLayout_6.addWidget(self.btProcessImport)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.stepLabel = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.stepLabel.setText(_fromUtf8(""))
        self.stepLabel.setObjectName(_fromUtf8("stepLabel"))
        self.horizontalLayout.addWidget(self.stepLabel)
        self.subStepLabel = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.subStepLabel.setText(_fromUtf8(""))
        self.subStepLabel.setObjectName(_fromUtf8("subStepLabel"))
        self.horizontalLayout.addWidget(self.subStepLabel)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.pbProcess = QtGui.QProgressBar(self.scrollAreaWidgetContents_2)
        self.pbProcess.setProperty("value", 0)
        self.pbProcess.setObjectName(_fromUtf8("pbProcess"))
        self.verticalLayout_6.addWidget(self.pbProcess)
        self.txtLog = QtGui.QTextEdit(self.scrollAreaWidgetContents_2)
        self.txtLog.setObjectName(_fromUtf8("txtLog"))
        self.verticalLayout_6.addWidget(self.txtLog)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout.addWidget(self.scrollArea)
        self.buttonBox = QtGui.QDialogButtonBox(cadastre_import_form)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(cadastre_import_form)
        self.databaseSpecificOptions.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(cadastre_import_form)

    def retranslateUi(self, cadastre_import_form):
        cadastre_import_form.setWindowTitle(_translate("cadastre_import_form", "Cadastre", None))
        self.groupBox.setTitle(_translate("cadastre_import_form", "Base de données de travail", None))
        self.label.setText(_translate("cadastre_import_form", "Type de base", None))
        self.liDbType.setItemText(0, _translate("cadastre_import_form", "-- Choisir --", None))
        self.liDbType.setItemText(1, _translate("cadastre_import_form", "Postgis", None))
        self.liDbType.setItemText(2, _translate("cadastre_import_form", "Spatialite", None))
        self.label_2.setText(_translate("cadastre_import_form", "Connexions", None))
        self.label_3.setText(_translate("cadastre_import_form", "Schémas", None))
        self.btDbCreateSchema.setText(_translate("cadastre_import_form", "créer", None))
        self.databaseSpecificOptions.setItemText(self.databaseSpecificOptions.indexOf(self.tabPostgis), _translate("cadastre_import_form", "PostGIS", None))
        self.label_7.setText(_translate("cadastre_import_form", "Choisissez une connexion dans la liste ci-dessus, ou", None))
        self.btCreateNewSpatialiteDb.setText(_translate("cadastre_import_form", "Créer une base Spatialite", None))
        self.databaseSpecificOptions.setItemText(self.databaseSpecificOptions.indexOf(self.tabSpatialite), _translate("cadastre_import_form", "Spatialite", None))
        self.groupBox_5.setTitle(_translate("cadastre_import_form", "Fichiers EDIGEO", None))
        self.label_11.setText(_translate("cadastre_import_form", "Répertoire", None))
        self.btEdigeoSourceDir.setText(_translate("cadastre_import_form", "...", None))
        self.label_12.setText(_translate("cadastre_import_form", "Projections: source", None))
        self.btEdigeoSourceProj.setText(_translate("cadastre_import_form", "...", None))
        self.label_13.setText(_translate("cadastre_import_form", "Cible", None))
        self.btEdigeoTargetProj.setText(_translate("cadastre_import_form", "...", None))
        self.label_4.setText(_translate("cadastre_import_form", "Département", None))
        self.label_5.setText(_translate("cadastre_import_form", "Direction", None))
        self.groupBox_6.setTitle(_translate("cadastre_import_form", "Fichiers MAJIC", None))
        self.label_14.setText(_translate("cadastre_import_form", "Répertoire", None))
        self.btMajicSourceDir.setText(_translate("cadastre_import_form", "...", None))
        self.groupBox_7.setTitle(_translate("cadastre_import_form", "Paramètres", None))
        self.label_15.setText(_translate("cadastre_import_form", "Version du format", None))
        self.label_16.setText(_translate("cadastre_import_form", "Année", None))
        self.label_6.setText(_translate("cadastre_import_form", "Lot", None))
        self.btProcessImport.setText(_translate("cadastre_import_form", "Lancer l\'import", None))
        self.txtLog.setHtml(_translate("cadastre_import_form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))

import resource_rc
