'''
Created on May 2019

@author: Jane
'''

import sys
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PySide2.QtGui import QIcon, QPixmap
from PySide2 import QtCore, QtGui, QtWidgets

class GUI(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.grid_layout()
        self.controller_layout()
        
        mainLayout = QtWidgets.QVBoxLayout()   
        mainLayout.addWidget(self.gridGroupBox)
        mainLayout.addWidget(self.horizontalGroupBox)
        
        self.setLayout(mainLayout)
        self.setGeometry(300, 300, 350, 300) #window size
        
        
    def initUI(self):
        self.setWindowTitle("Controls") 
   
        label = QLabel(self)
        bkgrnd = QPixmap('background.png')
        scale = bkgrnd.scaled(1920, 1050, QtCore.Qt.IgnoreAspectRatio)   
        label.setPixmap(scale)
        self.resize(bkgrnd.width(),bkgrnd.height())
        self.show()

  
        
    def grid_layout(self):
        self.gridGroupBox = QtWidgets.QGroupBox()
        self.gridGroupBox.setStyleSheet(".QGroupBox {border: 0px;}")
        self.setStyleSheet(".QPushButton{background: transparent;}")
        layout = QtWidgets.QGridLayout()       
         
        home = QPushButton('', self)
        home_image = QPixmap('home.png')
        home.setIcon(QIcon(home_image))
        home.setIconSize(QtCore.QSize(90,90))
        home.clicked.connect(self.on_click_home)
        layout.addWidget(home, 0,0)
 
 
        info = QPushButton('', self)
        info_image = QPixmap('info.png')
        info.setIcon(QIcon(info_image))
        info.setIconSize(QtCore.QSize(90,90))
        info.clicked.connect(self.on_click_info)
        layout.addWidget(info, 0,1)
         
         
        help = QPushButton('', self)
        help_image = QPixmap('help.png')
        help.setIcon(QIcon(help_image))
        help.setIconSize(QtCore.QSize(90,90))
        help.clicked.connect(self.on_click_help)
        layout.addWidget(help, 0,2)
        
        #add empty column 
        layout.addWidget(QLabel(self),0,3)
        layout.setColumnStretch(3,1)
        
        logo_image = QPixmap('logo.png')
        logo_scaled = logo_image.scaled(450,80, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        logo = QLabel(self)
        logo.setPixmap(logo_scaled)
        layout.addWidget(logo, 0,4)
        
        #add empty column 
        layout.addWidget(QLabel(''),0,5)
        layout.setColumnStretch(5,1)

        horizon = QPushButton('',self)
        horizon_image = QPixmap('horizon.png')
        horizon.setIcon(QIcon(horizon_image))
        horizon.setIconSize(QtCore.QSize(310, 160))
        horizon.clicked.connect(self.on_click_horizon)
        layout.addWidget(horizon, 0,6)
         
         
        camera2 = QPushButton('',self)
        camera2_image = QPixmap('camera2.png')
        camera2.setIcon(QIcon(camera2_image))
        camera2.setIconSize(QtCore.QSize(230,130)) 
        layout.addWidget(camera2, 0,7)
         
        camera3 = QPushButton('',self)
        camera3_image = QPixmap('camera3.png')
        camera3.setIcon(QIcon(camera3_image))
        camera3.setIconSize(QtCore.QSize(230,130))
        layout.addWidget(camera3, 0,8)    
 
        self.gridGroupBox.setLayout(layout)  
        


    def controller_layout(self):
        self.horizontalGroupBox = QtWidgets.QGroupBox()
        self.horizontalGroupBox.setStyleSheet(".QGroupBox { border: 0px;}")
        layout = QtWidgets.QHBoxLayout()
        
        joystick_image = QPixmap('joystick.png')
        joystick_scaled = joystick_image.scaled(1600,1000, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        joystick = QLabel(self)
        joystick.setPixmap(joystick_scaled)
        joystick.resize(joystick_scaled.width(), joystick_scaled.height())
        joystick.setScaledContents(True) #scalable when resizing window
        layout.addWidget(joystick)
        
        self.horizontalGroupBox.setLayout(layout)   
        
        
        
    def on_click_home(self):
        print('testHome')
        self.show()        
        
    def on_click_info(self):
        print('testInfo')
        self.show()
            
    def on_click_help(self):
        print('testHelp')
        self.show()
        
    def on_click_horizon(self):
        print('testHorizon')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = GUI()
    sys.exit(app.exec_())
