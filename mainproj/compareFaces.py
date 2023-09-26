from deepface import DeepFace
import cv2
import mediapipe as mp
import imutils
import time
import os
import json
import asyncio
from utils.vericar_DeepFace import verify


def get_dfs(rostro, frame, lista):
    print('face started')


# cv2.imwrite(personPath + '/al153168_{}.jpg'.format(count), rostro)
# cv2.imwrite('test.jpg', rostro)

    dfs = DeepFace.find(img_path=rostro, db_path='../pics',
                        enforce_detection=False, silent=True)

    #! **************EXTRACT as FUNCTION****************************************
    if dfs[0]['VGG-Face_cosine'][0] < 0.11:
        jsonpath = dfs[0]['identity'][0].split('/')[1]
        # print(jsonpath)
        # currentPath = os.path.abspath(os.getcwd())
        filepath = os.path.join('../' + jsonpath + '/data.json')
        with open(filepath, 'r') as fp:
            information = json.load(fp)
            if str(information['Alumno'][0]['matricula']) not in lista:
                # print('alumno ya entro a la escuela')
                # print(rostro)
                print('matricula:' +
                      str(information['Alumno'][0]['matricula']))
                print('nombre:' + information['Alumno'][0]['nombre'])
                print('telefono:' +
                      str(information['Alumno'][0]['tel_contacto']))

                lista.append(
                    str(information['Alumno'][0]['matricula']))
    #! ******************************************************
    # image2 = frame.copy()
    # cv2.namedWindow("Image")
    # cv2.imshow('frame', image2)
