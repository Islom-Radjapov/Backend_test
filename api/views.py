# from .apps import ApiConfig
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import TemplateView
# import cv2
# import cvlib as cv
# import numpy as np
from . import models



class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class GamePageView(TemplateView):
    template_name = 'game.html'

    # def get(self, request):
    #
    #     serializer = SnippetSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     print(request.method)
    #     print(request.data)
    #     return Response('HOME PAGE')
    #
    # def post(self, request):
    #     serializer = SnippetSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class GenderPradict(APIView):
#     def post(self, request):
#         data = request.FILES
#         data = data['foto']
#
#         img = cv2.VideoCapture( data )
#
#         classes = ['man', 'woman']
#
#         # read frame from webcam
#         status, frame = img.read()  # frame bu videoni numpy array shakli,  status bu agar camera ishlavotgan bosa True boladi
#
#         # apply face detection
#         face, confidence = cv.detect_face(frame)
#
#         # loop through detected faces
#         for _, y in enumerate(face):
#             f = y
#
#         # get corner points of face rectangle
#         (startX, startY) = f[0], f[1]
#         (endX, endY) = f[2], f[3]
#
#         # crop the detected face region
#         face_crop = np.copy(frame[startY:endY, startX:endX])
#
#         if (face_crop.shape[0]) < 10 or (face_crop.shape[1]) < 10:
#             return Response( "Inson suratni to'liq jonating!", status=200 )
#
#         # preprocessing for gender detection model
#         face_crop = cv2.resize(face_crop, (96, 96))
#         face_crop = face_crop.astype("float") / 255.0
#         face_crop = np.expand_dims(face_crop, axis=0)
#
#         # apply gender detection on face
#         conf = ApiConfig.model.predict(face_crop)[0]  # model.predict return a 2D matrix, ex: [[9.9993384e-01 7.4850512e-05]]
#
#         # get label with max accuracy
#         idx = np.argmax(conf)
#         label = classes[idx]
#
#         response = {"Gender": label}
#
#         return Response( response, status=200 )

