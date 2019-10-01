from PyQt5 import QtCore, QtGui, QtWidgets, uic
# import some PyQt5 modules
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
import dlib
import numpy as np

import time
import os
from PIL import Image
import cv2
class MyWinDow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWinDow,self).__init__()
        self.ui=uic.loadUi('FaceFilter.ui',self)
        self.ui.setFixedSize(self.ui.size())
        self.videoOriginBtn = self.ui.pushButton
        self.gaoBtn = self.ui.pushButton_2
        self.thuglifeBtn = self.ui.pushButton_3
        self.dogBtn = self.ui.pushButton_4 
        self.portraitBtn = self.ui.pushButton_5 
        self.sepiaBtn = self.ui.pushButton_6 
        self.invertBtn = self.ui.pushButton_8 
        self.camView = self.ui.label_4
        self.writeImg = self.ui.pushButton_7

         # create a timer
        self.timer = QTimer()
        self.Gaotimer = QTimer()
        self.Dogtimer = QTimer()
        self.Thuglifetimer =QTimer()
        self.applyinvertTimmer = QTimer()
        self.sepiaTimmer = QTimer()
        self.portraitTimer = QTimer()
        # set timer timeout callback function
        self.Gaotimer.timeout.connect(self.GaoFilter)
        self.timer.timeout.connect(self.viewCam)
        self.Dogtimer.timeout.connect(self.DogFilter)
        self.Thuglifetimer.timeout.connect(self.ThuglifeFilter)
        self.applyinvertTimmer.timeout.connect(self.apply_invert)
        self.sepiaTimmer.timeout.connect(self.apply_sepia)
        self.portraitTimer.timeout.connect(self.apply_portrait_mode)


        self.videoOriginBtn.clicked.connect(self.controlTimer)
        self.gaoBtn.clicked.connect(self.GaocontrolTimer)
        self.dogBtn.clicked.connect(self.DogcontrolTimer)
        self.thuglifeBtn.clicked.connect(self.ThugLifecontrolTimer)
        self.invertBtn.clicked.connect(self.ApplyinvertTimmer)
        self.sepiaBtn.clicked.connect(self.SepiaTimmer)
        self.portraitBtn.clicked.connect(self.PortraitTimmer)
        self.cap=cv2.VideoCapture(0)
    
    def PrintImg(self,frame):
        cv2.imwrite('output.jpg',frame)

    def viewCam(self):
        # read image in BGR format
        ret, image = self.cap.read()
        image = cv2.flip(image,1)
        # convert image to RGB format
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # get image infos
        height, width, channel = image.shape
        step = channel * width
        # create QImage from image
        qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
        # show image in img_label
        self.writeImg.clicked.connect(lambda:self.PrintImg(image))    
        self.ui.camView.setPixmap(QPixmap.fromImage(qImg))

    # start/stop timer
    def PortraitTimmer(self):
        # if timer is stopped
            # create video capture
        self.Gaotimer.stop()
        self.Dogtimer.stop() 
        self.Thuglifetimer.stop()
        self.timer.stop()
        self.applyinvertTimmer.stop()
        self.sepiaTimmer.stop()
        self.cap.release()

        if not self.portraitTimer.isActive():
            # start timer
            self.cap = cv2.VideoCapture(0)
            self.portraitTimer.start(20)
            # update control_bt text
        # if timer is started
        else:
            # stop timer
            self.portraitTimer.stop()
            # release video capture
            self.cap.release()
            # update control_bt text

    
    
    def SepiaTimmer(self):
        # if timer is stopped
            # create video capture
        self.Gaotimer.stop()
        self.Dogtimer.stop() 
        self.Thuglifetimer.stop()
        self.timer.stop()
        self.applyinvertTimmer.stop()
        self.portraitTimer.stop()
        self.cap.release()

        if not self.sepiaTimmer.isActive():
            # start timer
            self.cap = cv2.VideoCapture(0)
            self.sepiaTimmer.start(20)
            # update control_bt text
        # if timer is started
        else:
            # stop timer
            self.sepiaTimmer.stop()
            # release video capture
            self.cap.release()
            # update control_bt text


    def ApplyinvertTimmer(self):
        # if timer is stopped
            # create video capture
        self.Gaotimer.stop()
        self.Dogtimer.stop() 
        self.Thuglifetimer.stop()
        self.timer.stop()
        self.portraitTimer.stop()
        self.sepiaTimmer.stop()
        self.cap.release()

        if not self.applyinvertTimmer.isActive():
            # start timer
            self.cap = cv2.VideoCapture(0)
            self.applyinvertTimmer.start(20)
            # update control_bt text
        # if timer is started
        else:
            # stop timer
            self.applyinvertTimmer.stop()
            # release video capture
            self.cap.release()
            # update control_bt text

    def controlTimer(self):
        # if timer is stopped
            # creframeate video capture
        self.Gaotimer.stop()
        self.Dogtimer.stop() 
        self.Thuglifetimer.stop()
        self.Gaotimer.stop()
        self.Dogtimer.stop() 
        self.Thuglifetimer.stop()
        self.applyinvertTimmer.stop()
        self.sepiaTimmer.stop()
        self.portraitTimer.stop()
        self.cap.release()

        if not self.timer.isActive():
            # start timer
            self.cap = cv2.VideoCapture(0)
            self.timer.start(20)
            # update control_bt text
        # if timer is started
        else:
            # stop timer
            self.timer.stop()
            # release video capture
            self.cap.release()
            # update control_bt text
    
    def GaocontrolTimer(self):
        # if timer is stopped
        self.timer.stop()
        self.Dogtimer.stop() 
        self.Thuglifetimer.stop()
        self.applyinvertTimmer.stop()
        self.sepiaTimmer.stop()
        self.portraitTimer.stop()
        self.cap.release()
        if not self.Gaotimer.isActive():
            # create video capture
            self.cap = cv2.VideoCapture(0)
            # start timer
            self.Gaotimer.start(20)
            # update control_bt text
        # if timer is started
        else:
            # stop timer
            self.Gaotimer.stop()
            # release video capture
            self.cap.release()
            # update control_bt text

    def DogcontrolTimer(self):
        # if timer is stopped
        self.Gaotimer.stop()
        self.timer.stop() 
        self.Thuglifetimer.stop()
        self.applyinvertTimmer.stop()
        self.sepiaTimmer.stop()
        self.portraitTimer.stop()
        self.cap.release()
        if not self.Dogtimer.isActive():
            # create video capture
            self.cap = cv2.VideoCapture(0)
            # start timer
            self.Dogtimer.start(20)
            # update control_bt text
        # if timer is started
        else:
            # stop timer
            self.Dogtimer.stop()
            # release video capture
            self.cap.release()
            # update control_bt text
        
    def ThugLifecontrolTimer(self):
        # if timer is stopped
        self.Gaotimer.stop()
        self.Dogtimer.stop() 
        self.timer.stop()
        self.applyinvertTimmer.stop()
        self.sepiaTimmer.stop()
        self.portraitTimer.stop()
        self.cap.release()
        if not self.Thuglifetimer.isActive():
            # create video capture
            self.cap = cv2.VideoCapture(0)
            # start timer
            self.Thuglifetimer.start(20)
            # update control_bt text
        # if timer is started
        else:
            # stop timer
            self.Thuglifetimer.stop()
            # release video capture
            self.cap.release()
            # update control_bt text

    def shape_to_list(self,shape, dtype="int"):
        coords = [[shape.part(i).x, shape.part(i).y]for i in range(0, 68)]
        return coords

    def ganMask(self,frame,shape):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        background = Image.fromarray(frame)
        w = shape[16][0]-shape[0][0]
        h = shape[9][1] - shape[20][1] + 100
        resized_mask = mask.resize((int(w),int(h)),Image.ANTIALIAS)
        offset = [shape[16][0]-int(w),shape[9][1] - int(h)]
        background.paste(resized_mask, offset, mask=resized_mask)
        background = np.asarray(background)
        background = cv2.cvtColor(background, cv2.COLOR_RGB2BGR)
        return np.asarray(background)


    def ganthuoc(self,frame, shape):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        background = Image.fromarray(frame)

        resized_mask = thuoc.resize((60,60), Image.ANTIALIAS)
        offset = [shape[66][0] - resized_mask.size[0], shape[66][1]]
        background.paste(resized_mask, offset, mask=resized_mask)
        background = np.asarray(background)
        background = cv2.cvtColor(background, cv2.COLOR_RGB2BGR)
        return np.asarray(background)

    def gannon(self,frame, shape):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        background = Image.fromarray(frame)
        w = shape[16][0] - shape[0][0]
        h = shape[66][1] - shape[21][1]
        resized_mask = non.resize((int(1.4*w),int(1.3*h)), Image.ANTIALIAS)
    
        offset = [shape[20][0] - int(w /1.5), shape[20][1] - int(1.3*h)]
        background.paste(resized_mask, offset, mask=resized_mask)
        background = np.asarray(background)
        background = cv2.cvtColor(background, cv2.COLOR_RGB2BGR)
        return np.asarray(background)

    def ganKieng(self,frame,shape):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        background = Image.fromarray(frame)
        w = shape[45][0]-shape[36][0]
        h = shape[30][1] - shape[28][1]
        resized_mask = kieng.resize((int(w*1.5),int(h*1.3)),Image.ANTIALIAS)
        offset = [shape[42][0]-int(w),shape[42][1] - int(h/1.3)]
        background.paste(resized_mask, offset, mask=resized_mask)
        background = np.asarray(background)
        background = cv2.cvtColor(background, cv2.COLOR_RGB2BGR)
        return np.asarray(background)
    

    def DogEarLeft(self,frame,shape): #tach ra ben trai ben phai
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        background = Image.fromarray(frame)
        w = shape[21][0] - shape[17][0]
        h = shape[41][1] - shape[19][1]
        resized_mask = dogEarLeft.resize((int(w),int(h)),Image.ANTIALIAS)
        offset = [shape[19][0]-int(w),shape[19][1] - int(h)]
        background.paste(resized_mask, offset, mask=resized_mask)
        background = np.asarray(background)
        background = cv2.cvtColor(background, cv2.COLOR_RGB2BGR)
        return np.asarray(background)

    def DogEarRight(self,frame,shape): #tach ra ben trai ben phai
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        background = Image.fromarray(frame)
        w = shape[21][0] - shape[17][0]
        h = shape[41][1] - shape[19][1]
        resized_mask = dogEarRight.resize((int(w),int(h)),Image.ANTIALIAS)
        offset = [shape[26][0]-int(w)+30,shape[24][1] - int(h)]
        background.paste(resized_mask, offset, mask=resized_mask)
        background = np.asarray(background)
        background = cv2.cvtColor(background, cv2.COLOR_RGB2BGR)
        return np.asarray(background)

    def DogNose(self,frame,shape):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        background = Image.fromarray(frame)
        w = shape[35][0]-shape[31][0]
        h = shape[33][1] - shape[27][1]
        resized_mask = dogNose.resize((int(w+20),int(h)),Image.ANTIALIAS)
        offset = [shape[31][0]-10,shape[35][1]-int(h/1.3)]
        background.paste(resized_mask, offset, mask=resized_mask)
        background = np.asarray(background)
        background = cv2.cvtColor(background, cv2.COLOR_RGB2BGR)
        return np.asarray(background)

    def DogMouth(self,frame,shape):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        background = Image.fromarray(frame)
        w = shape[64][0]-shape[60][0]
        h = shape[57][1]-shape[62][1]+20
        resized_mask = dogMouth.resize((int(w),int(h)),Image.ANTIALIAS)
        offset = [shape[64][0]-int(w),shape[62][1]]
        distance = shape[66][1]-shape[62][1]
        if distance > 10:
            background.paste(resized_mask, offset, mask=resized_mask)    
            # print(distance)
        background = np.asarray(background)
        background = cv2.cvtColor(background, cv2.COLOR_RGB2BGR)
        return np.asarray(background)
    
    def GaoFilter(self):
        ret, frame = self.cap.read()
        # convert image to RGB format
        frame = cv2.flip(frame,1)

        frame_grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame_resized = cv2.resize(frame_grey, None, fx=ratio, fy=ratio)
        dets = detector(frame_resized, 2)   
        for k, d in enumerate(dets):
            shape = predictor(frame_resized,d)
            shape = self.shape_to_list(shape)
        #print(shape)
            shape = [[int(x/ratio), int(y/ratio)] for x, y in shape]
            try:
                frame = self.ganMask(frame,shape)
            except:
                print("can't detection")
        # get image infos
        height, width, channel = frame.shape
        step = channel * width
        # create QImage from image
        qImg = QImage(frame.data, width, height, step, QImage.Format_RGB888)
        qImg = qImg.rgbSwapped()
        # show image in img_label
        self.writeImg.clicked.connect(lambda:self.PrintImg(frame))    

        self.ui.camView.setPixmap(QPixmap.fromImage(qImg))


    def ThuglifeFilter(self):
        ret, frame = self.cap.read()
        frame = cv2.flip(frame,1)

        # convert image to RGB format
        frame_grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame_resized = cv2.resize(frame_grey, None, fx=ratio, fy=ratio)
        dets = detector(frame_resized, 2)   
        for k, d in enumerate(dets):
            shape = predictor(frame_resized,d)
            shape = self.shape_to_list(shape)
        #print(shape)
            shape = [[int(x/ratio), int(y/ratio)] for x, y in shape]
            try:
                frame = self.ganKieng(frame,shape)
                frame = self.gannon(frame,shape)
                frame = self.ganthuoc(frame,shape)
            except:
                print("can't detection")
        # get image infos
        height, width, channel = frame.shape
        step = channel * width
        # create QImage from image
        qImg = QImage(frame.data, width, height, step, QImage.Format_RGB888)
        qImg = qImg.rgbSwapped()
        # show image in img_label
        self.writeImg.clicked.connect(lambda:self.PrintImg(frame))    
        
        self.ui.camView.setPixmap(QPixmap.fromImage(qImg))

    def DogFilter(self):
        ret, frame = self.cap.read()
        frame = cv2.flip(frame,1)

       # convert image to RGB format
        frame_grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame_resized = cv2.resize(frame_grey, None, fx=ratio, fy=ratio)
        dets = detector(frame_resized, 2)   
        for k, d in enumerate(dets):
            shape = predictor(frame_resized,d)
            shape = self.shape_to_list(shape)
            shape = [[int(x/ratio), int(y/ratio)] for x, y in shape]
            try:
                frame = self.DogEarLeft(frame,shape)
                frame = self.DogEarRight(frame,shape)
                frame = self.DogMouth(frame,shape)
                frame = self.DogNose(frame,shape)
            except:
                print("can't detection")
        # get image infos
        height, width, channel = frame.shape
        step = channel * width
        # create QImage from image
        qImg = QImage(frame.data, width, height, step, QImage.Format_RGB888)
        qImg = qImg.rgbSwapped()
        # show image in img_label
        self.writeImg.clicked.connect(lambda:self.PrintImg(frame))    

        self.ui.camView.setPixmap(QPixmap.fromImage(qImg))        

    def apply_invert(self):
        ret, frame = self.cap.read()
        frame = cv2.flip(frame,1)
        
        frame = cv2.bitwise_not(frame)
        height, width, channel = frame.shape
        step = channel * width
        # create QImage from image
        qImg = QImage(frame.data, width, height, step, QImage.Format_RGB888)
        qImg = qImg.rgbSwapped()
        # show image in img_label
        self.writeImg.clicked.connect(lambda:self.PrintImg(frame))    

        self.ui.camView.setPixmap(QPixmap.fromImage(qImg)) 

    def verify_alpha_channel(self,frame):
        try:
            frame.shape[3] # 4th position
        except IndexError:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
        return frame


    def apply_color_overlay(self,frame, 
                intensity=0.2, 
                blue = 0,
                green = 0,
                red = 0):
        frame = self.verify_alpha_channel(frame)
        frame_h, frame_w, frame_c = frame.shape
        color_bgra = (blue, green, red, 1)
        overlay = np.full((frame_h, frame_w, 4), color_bgra, dtype='uint8')
        cv2.addWeighted(overlay, intensity, frame, 1.0, 0, frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
        return frame

    def apply_sepia(self,intensity=0.5):
        blue = 20
        green = 66 
        red = 112
        ret, frame = self.cap.read()
        frame = cv2.flip(frame,1)

        frame = self.apply_color_overlay(frame, 
                intensity=intensity, 
                blue=blue, green=green, red=red)
        
        height, width, channel = frame.shape
        step = channel * width
        # create QImage from image
        qImg = QImage(frame.data, width, height, step, QImage.Format_RGB888)
        qImg = qImg.rgbSwapped()
        # show image in img_label
        self.writeImg.clicked.connect(lambda:self.PrintImg(frame))    

        self.ui.camView.setPixmap(QPixmap.fromImage(qImg)) 


    def alpha_blend(self,frame_1, frame_2, mask):
        alpha = mask/255.0 
        blended = cv2.convertScaleAbs(frame_1*(1-alpha) + frame_2*alpha)
        return blended


    def apply_circle_focus_blur(self, intensity=0.2):
        ret, frame = self.cap.read()
        frame           = self.verify_alpha_channel(frame)
        frame_h, frame_w, frame_c = frame.shape
        y = int(frame_h/2)
        x = int(frame_w/2)
        radius = int(x/2) # int(x/2)
        center = (x,y)
        mask    = np.zeros((frame_h, frame_w, 4), dtype='uint8')
        cv2.circle(mask, center, radius, (255,255,255), -1, cv2.LINE_AA)
        mask    = cv2.GaussianBlur(mask, (21,21),11 )
        blured  = cv2.GaussianBlur(frame, (21,21), 11)
        blended = self.alpha_blend(frame, blured, 255-mask)
        frame   = cv2.cvtColor(blended, cv2.COLOR_BGRA2BGR)
        height, width, channel = frame.shape
        step = channel * width
        # create QImage from image
        qImg = QImage(frame.data, width, height, step, QImage.Format_RGB888)
        qImg = qImg.rgbSwapped()
        # show image in img_label
        self.ui.camView.setPixmap(QPixmap.fromImage(qImg)) 

    def apply_portrait_mode(self):
        ret, frame = self.cap.read()
        frame = cv2.flip(frame,1)
        
        frame = self.verify_alpha_channel(frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, mask = cv2.threshold(gray, 120,255,cv2.THRESH_BINARY)
        mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGRA)
        blured = cv2.GaussianBlur(frame, (21,21), 11)
        blended = self.alpha_blend(frame, blured, mask)
        frame = cv2.cvtColor(blended, cv2.COLOR_BGRA2BGR)
        height, width, channel = frame.shape
        step = channel * width
        # create QImage from image
        qImg = QImage(frame.data, width, height, step, QImage.Format_RGB888)
        qImg = qImg.rgbSwapped()
        # show image in img_label
        self.writeImg.clicked.connect(lambda:self.PrintImg(frame))    

        self.ui.camView.setPixmap(QPixmap.fromImage(qImg)) 

if __name__ == "__main__":
    import sys
    tmp = 0
    ratio = 0.4
    predictor_path = './Data/shape_predictor_68_face_landmarks.dat'
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(predictor_path)
    thuoc = Image.open('./Data/oke.png')
    non = Image.open('./Data/hat.png')
    kieng = Image.open('./Data/glasses.png')
    mask = Image.open('./Data/gaoMask2.png')

    #dog
    dogEarLeft = Image.open('./Data/earLeft.png')
    dogEarRight = Image.open('./Data/earRight.png')
    dogNose = Image.open('./Data/nose.png')
    dogMouth = Image.open('./Data/mouth.png')
    app = QtWidgets.QApplication(sys.argv)
    win = MyWinDow()
    win.show()
    sys.exit(app.exec_())
