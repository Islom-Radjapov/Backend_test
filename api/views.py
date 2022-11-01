import time
from .apps import AppConfig
from rest_framework.views import APIView
from rest_framework.response import Response
import cv2
import cvlib as cv
from keras.utils import img_to_array
import numpy as np


class GenderPradict(APIView):
    def post(self, request):
        data = request.FILES
        data = data['foto']
        print( data )
        print( type(data) )

        # img = cv2.VideoCapture( data['foto'] )
        #
        # classes = ['man', 'woman']
        #
        # # read frame from webcam
        # status, frame = img.read()  # frame bu videoni numpy array shakli,  status bu agar camera ishlavotgan bosa True boladi
        #
        # # apply face detection
        # face, confidence = cv.detect_face(frame)
        #
        # # loop through detected faces
        # for x, y in enumerate(face):
        #     idx = x
        #     f = y
        #
        # # get corner points of face rectangle
        # (startX, startY) = f[0], f[1]
        # (endX, endY) = f[2], f[3]
        #
        # # draw rectangle over face
        # # cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 0, 0), 2)
        #
        # # crop the detected face region
        # face_crop = np.copy(frame[startY:endY, startX:endX])
        #
        # # if (face_crop.shape[0]) < 10 or (face_crop.shape[1]) < 10:
        # #     continue
        #
        # # preprocessing for gender detection model
        # face_crop = cv2.resize(face_crop, (96, 96))
        # face_crop = face_crop.astype("float") / 255.0
        # face_crop = img_to_array(face_crop)
        # face_crop = np.expand_dims(face_crop, axis=0)
        #
        # # apply gender detection on face
        # conf = ApiConfig.model.predict(face_crop)[0]  # model.predict return a 2D matrix, ex: [[9.9993384e-01 7.4850512e-05]]
        #
        # # get label with max accuracy
        # idx = np.argmax(conf)
        # label = classes[idx]
        #
        # # label = "{}: {:.2f}%".format(label, conf[idx] * 100)
        #
        # response = {"Gender": label}
        #
        return Response( "response", status=200 )