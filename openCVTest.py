import cv2
from PyQt4 import QtCore, QtGui, uic
import sys


class HSVWidget(QtGui.QWidget):

    def __init__(self):
        super(HSVWidget, self).__init__()

        self.ui = uic.loadUi("display2.ui")
        
        self.ui.show()

        self.cam = cv2.VideoCapture(0) # sets up video capture object
        
        self.ui.addButton.clicked.connect(lambda: self.add())
        self.ui.clearButton.clicked.connect(lambda: self.clearList())

        self.timer = QtCore.QTimer()  # sets timer to call update when it runs out
        self.timer.timeout.connect(self.update) # when timeout call update
        self.timer.start(1)

    def update(self):
        madeIt, frame = self.cam.read()

        ### implement slider values
        hsvMin = (self.ui.hueMin.value(), self.ui.satMin.value(), self.ui.valMin.value())
        hsvMax = (self.ui.hueMax.value(), self.ui.satMax.value(), self.ui.valMax.value())
  
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        mask = cv2.inRange(frame, hsvMin, hsvMax)
        frame = cv2.bitwise_and(frame, frame, mask=mask)

        frame = cv2.cvtColor(frame, cv2.COLOR_HSV2RGB) #converts color
       
        height, width, channel = frame.shape #separates image into its 3 axes
        bytesPerLine = 3 * width
        qImg = QtGui.QImage(frame.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888) # creates image in format PyQt likes

        self.ui.pictureLocation.setPixmap(QtGui.QPixmap(qImg))
        
    def add(self):
        self.text = self.ui.filterEntry.text()
        self.ui.filterEntry.clear()
        self.ui.filterList.addItem(self.text)
    
    def clearList(self):
        self.ui.filterList.clear()
        


app = QtGui.QApplication(sys.argv)
widget = HSVWidget()
sys.exit(app.exec_())

