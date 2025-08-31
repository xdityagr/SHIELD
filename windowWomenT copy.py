from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtWidgets import QDialog

from PySide2 import QtCore, QtGui, QtWidgets

from ui_newUIShield import Ui_MainWindow
import sys, time

from sckt_recv import recv_data
import threading
from IrisScanning.recognition.iris_recognition_algorithm import RecognitionAlgorithm, generates_binary_template, generates_vector_template
from IrisScanning.utils.recognition_definitions import *
from IrisScanning.utils.error_utils import *
from threading import Timer

import serial
import time

from PIL import Image
import os, cv2

class ShieldConsole(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.ui = Ui_MainWindow()
		self.setWindowTitle("SHIELD WSN Cluster Head Console")
		self.ui.setupUi(self)
		
		self.recieved=None
		self.Running = True
		self.ui.tabWidget.setCurrentIndex(0)
		self.ui.loadOriginalIris.clicked.connect(self.loadOriginalIris)
		self.ui.addPhoto.clicked.connect(self.addPhoto)
		self.ui.loadQueryIris.clicked.connect(self.loadQueryIris)
		self.ui.goButton.clicked.connect(self.runIrisScan)

		self.BothChosen = False
		self.curr_iris_arr = None
		self.curr_irisq_arr = None

		self.ui.matchThresholdSpinBox.setValue(0.50)
		self.ui.found.setText("Searching ...")

		self.ui.match_found_frame.hide()
		
		self.t1 = threading.Thread(target=self.listenLoopFC).start()
		self.t2 = threading.Thread(target=self.listenLoopRFID).start()


		self.ui.found_content.hide()

		self.ui.startSearch.clicked.connect(self.searchingStarted)

		self.show()

	def searchingStarted (self):
		self.ui.tabWidget.setCurrentIndex(3)
		
	def loadOriginalIris(self):
		image_path, _ = QtWidgets.QFileDialog.getOpenFileName(
			self,
			"Open Image",
			"./iris-images",
			"bmp files (*.bmp)\njpg files (*.jpg)\nAll files (*.*)",
			"All files (*.*)",
			QtWidgets.QFileDialog.DontUseNativeDialog
		)
	
		self.curr_iris_arr = cv2.imread(str(image_path), cv2.IMREAD_GRAYSCALE)	
		
		qim = QImage(image_path)
		image_qpix = QPixmap.fromImage(qim)
		self.ui.irisImageO.setPixmap(image_qpix)
		self.ui.originalIrisLabel.setText(f"Original Iris - {os.path.basename(image_path)}")

		if self.ui.IrisImageQ.pixmap() != None:
			self.BothChosen = True
		else: self.BothChosen = False

	def loadQueryIris(self):
		image_path, _ = QtWidgets.QFileDialog.getOpenFileName(
			self,
			"Open Image",
			"./iris-images",
			"bmp files (*.bmp)\njpg files (*.jpg)\nAll files (*.*)",
			"All files (*.*)",
			QtWidgets.QFileDialog.DontUseNativeDialog
		)
		self.curr_irisq_arr = cv2.imread(str(image_path), cv2.IMREAD_GRAYSCALE)
		
		qim = QImage(image_path)
		image_qpix = QPixmap.fromImage(qim)

		self.ui.IrisImageQ.setPixmap(image_qpix)
		self.ui.queryIrisLabel.setText(f"Query Iris - {os.path.basename(image_path)}")
		
		if self.ui.IrisImageQ.pixmap() != None:
			self.BothChosen = True

		else: self.BothChosen = False

	def runIrisScan(self):
		self.ui.goButton.setEnabled(False)
		rec_alg = RecognitionAlgorithm()

		segm_method = 1
		rec_alg.set_segmentation_method(segm_method)

		norm_method = 2
		rec_alg.set_normalization_method(norm_method)

		enc_method = 1
		rec_alg.set_encoding_method(enc_method)

		dist_method = None
	

		if generates_binary_template(enc_method):
			dist_method =  HAMMING_DISTANCE

		elif generates_vector_template(enc_method):
			dist_method =  EUCLIDEAN_DISTANCE
		rec_alg.set_template_matching_method(dist_method)

		# selecting threshold	
		thres = self.ui.matchThresholdSpinBox.value()
		# performing matching
		result, d = rec_alg.match(self.curr_iris_arr, self.curr_irisq_arr)
		
		print(result, d)
		dpercent = f'{round((1-d) * 100)}%' if d!= None else "0 %"

		if result != 0:
			QtWidgets.QMessageBox.about(self, "Error", "<h2>%s</h2>" % error_messages[result])
		else:
			if round((1-d) * 100) > thres*100:
				self.ui.match_found_frame.show()
				self.ui.matchFound.setText(f"Match Found, {dpercent} Sure")
				self.ui.match_found_frame.setStyleSheet("background-color: rgb(110, 255, 108);")
				self.ui.matchFound.setStyleSheet("color: rgb(255, 255, 255);")
				print('yuh at', thres)
			else:
				self.ui.match_found_frame.show()
				self.ui.matchFound.setText(f"Match Not Found, {dpercent} Sure")
				self.ui.match_found_frame.setStyleSheet("background-color: rgb(255, 135, 135);")
				self.ui.matchFound.setStyleSheet("color: rgb(255, 255, 255);")
				print('nuh at', thres)

		# # resetting the state of the result label in 1.5 sec
		reset_timer = Timer(5, self.reset_iris_scan)
		reset_timer.start()

	def reset_iris_scan(self):
		print("reset")
		self.ui.match_found_frame.setStyleSheet("background-color: rgb(212, 240, 255);")
		self.ui.matchFound.setStyleSheet("color: rgb(38, 172, 255);")
		self.ui.match_found_frame.hide()
		self.ui.goButton.setEnabled(True)
		pimnone = QPixmap(None)
		self.ui.goButton.setEnabled(True)

	def addPhoto(self):
		if self.ui.label_17.pixmap():
			pp = QPixmap(None)
			self.ui.label_17.setPixmap(pp)
			self.ui.label_17.update()
		else:
			photo_path, _ = QtWidgets.QFileDialog.getOpenFileName(
				self,
				"Open Image",
				"./iris-images",
				"bmp files (*.bmp)\njpg files (*.jpg)\nAll files (*.*)",
				"All files (*.*)",
				QtWidgets.QFileDialog.DontUseNativeDialog
			)
		
			qim = QImage(photo_path)
			image_qpix = QPixmap.fromImage(qim)
			self.ui.label_17.setPixmap(image_qpix)
		

	def restart(self):
		self.Running = False
		
		QtCore.QCoreApplication.quit()
		status = QtCore.QProcess.startDetached(sys.executable, sys.argv)
		print(status)
     
	def listenLoopFC(self):
		self.recieved=None
		while self.Running:
			self.startListening()
   
		if not self.Running:
			raise Exception('clse')
		
	def listenLoopRFID(self):
		z1baudrate = 9600
		z1port = 'COM6'  # set the correct port before run it

		z1serial = serial.Serial(port=z1port, baudrate=z1baudrate)
		z1serial.timeout = 2  # set read timeout
		# print z1serial  # debug serial.
		print(z1serial.is_open)  # True for opened
		if z1serial.is_open:
			while True:
				size = z1serial.inWaiting()
				if size:
					data = z1serial.read(size)
					data = str(data)
					dataL = data.replace("b", '').replace('\\n','').replace('\\r', '').replace("'", "")
					try:
						nameSIdx = dataL.index('Name')
						nameEIdx = dataL.index('Age')
						name = dataL[nameSIdx:nameEIdx] 
						
						PhoneSIdx = dataL.index('Phone') 
						PhoneEIdx = dataL.index('Aadhaar')
						
						age = dataL[nameEIdx:PhoneSIdx]
						phone = dataL[PhoneSIdx:PhoneEIdx]
						adhaar = dataL[PhoneEIdx:]
						
						if "Aditya" in name:
							self.switchTheme('3')
						elif "Aahan" in name:
							self.switchTheme('4')
					except ValueError as v:
						print(v)
						
				else:
					print('no data recieved from RFID.')

	
				time.sleep(1)
		else:
			print('z1serial not open')
		
	
	def switchTheme(self, val):
		if val == '1':
			self.ui.tabWidget.setCurrentIndex(3)
			self.ui.found_content.show()
			self.ui.found.setStyleSheet("color: rgb(38, 172, 255);")
			self.ui.found.setText('Found Missing Person : Aditya')
			self.ui.found_content.setText(u'<html><head/><body><p><span style=" font-size:10pt; font-weight:600;">Aadhaar :</span><span style=" font-size:10pt;"> 2015XXXXXX</span></p><p><span style=" font-size:10pt; font-weight:600;">Phone Number :</span><span style=" font-size:10pt;"> 9899XXXXX</span></p><p><span style=" font-size:10pt; font-weight:600;">Last Located at :</span><span style=" font-size:10pt;"> New Delhi, Rohini, Main Road [3:15 PM]</span></p><p><span style=" font-size:10pt; font-weight:600;">Via</span><span style=" font-size:10pt;"> : Facial Recoginiton (WSN)<br/></span></p></body></html>')
		
		elif val == '2':
			self.ui.tabWidget.setCurrentIndex(3)
			self.ui.found_content.show()
			self.ui.found.setStyleSheet("color: rgb(38, 172, 255);")
			self.ui.found.setText('Found Missing Person : Aahan')
			self.ui.found_content.setText(u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Aadhaar :</span><span style=\" font-size:10pt;\"> 1209XXXXXX</span></p><p><span style=\" font-size:10pt; font-weight:600;\">Phone Number :</span><span style=\" font-size:10pt;\"> 9781XXXX</span></p><p><span style=\" font-size:10pt; font-weight:600;\">Last Located at :</span><span style=\" font-size:10pt;\"> Bangalore, Karnataka [12:05 PM]</span></p><p><span style=\" font-size:10pt; font-weight:600;\">Via</span><span style=\" font-size:10pt;\"> : Facial Recoginiton (WSN)<br/></span></p></body></html>")
		elif val == '3':
			self.ui.tabWidget.setCurrentIndex(3)
			self.ui.found_content.show()
			self.ui.found.setStyleSheet("color: rgb(38, 172, 255);")
			self.ui.found.setText('Found Missing Person : Aditya')
			self.ui.found_content.setText(u'<html><head/><body><p><span style=" font-size:10pt; font-weight:600;">Aadhaar :</span><span style=" font-size:10pt;"> 2015XXXXXX</span></p><p><span style=" font-size:10pt; font-weight:600;">Phone Number :</span><span style=" font-size:10pt;"> 9899XXXXX</span></p><p><span style=" font-size:10pt; font-weight:600;">Last Located at :</span><span style=" font-size:10pt;"> New Delhi, Rohini, Main Road [3:15 PM]</span></p><p><span style=" font-size:10pt; font-weight:600;">Via</span><span style=" font-size:10pt;"> : Active RFID (WSN)<br/></span></p></body></html>')

		elif val == '4':
			self.ui.tabWidget.setCurrentIndex(3)
			self.ui.found_content.show()
			self.ui.found.setStyleSheet("color: rgb(38, 172, 255);")
			self.ui.found.setText('Found Missing Person : Aahan')
			self.ui.found_content.setText(u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Aadhaar :</span><span style=\" font-size:10pt;\"> 1209XXXXXX</span></p><p><span style=\" font-size:10pt; font-weight:600;\">Phone Number :</span><span style=\" font-size:10pt;\"> 9781XXXX</span></p><p><span style=\" font-size:10pt; font-weight:600;\">Last Located at :</span><span style=\" font-size:10pt;\"> Bangalore, Karnataka [12:05 PM]</span></p><p><span style=\" font-size:10pt; font-weight:600;\">Via</span><span style=\" font-size:10pt;\"> : Active RFID (WSN)<br/></span></p></body></html>")

		
		elif val == None:
			self.ui.found_content.hide()
			self.ui.found.setText("Searching ..")

		reset = Timer(5, self.reset_scanningPage)
		reset.start()

	def reset_scanningPage(self):
		print('reset -- scan page')
		self.ui.found_content.hide()
		self.ui.found.setText("Searching ..")



	def startListening(self):
		self.recieved = recv_data()
		print(f"Recieved : {self.recieved}")
		self.switchTheme(self.recieved)



app = QtWidgets.QApplication(sys.argv)
window = ShieldConsole()
sys.exit(app.exec_())
