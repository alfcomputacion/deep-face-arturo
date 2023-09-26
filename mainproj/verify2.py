# Importamos las librerias
from deepface import DeepFace
import cv2
import mediapipe as mp
import imutils
import time
import os
import json
import threading
import multiprocessing
from utils.vericar_DeepFace import verify
from compareFaces import get_dfs
# import pywhatkit

# Declaramos la deteccion de rostros
# Recortar el rostro
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# cap = cv2.VideoCapture('entrada_1.mp4')
# cap = cv2.VideoCapture('./VIDEO/entrada.mp4')

faceClassif = cv2.CascadeClassifier(
    cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
# count = 0
skip = 0
lista = []

while True:

    ret, frame = cap.read()
    if ret == False:
        break
    frame = imutils.resize(frame, width=840)
    # if skip > 5:
    #     print(skip)
    #     skip = 0
    # threading.Thread(target=get_dfs, daemon=True,
    #                  args=(frame, faceClassif, lista)).start()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxFrame = frame.copy()

    faces = faceClassif.detectMultiScale(gray, 1.3, 10)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 3)
        rostro = auxFrame[y:y+h, x:x+w]
        rostro = cv2.resize(rostro, (250, 250),
                            interpolation=cv2.INTER_CUBIC)
    # skip += 1
    cv2.imshow('frame', frame)
    p = multiprocessing.Process(target=get_dfs,
                                args=(rostro, frame, lista))
    p.start()

    # time.sleep(5)
    # Identificar rostro (fs = DeepFace.find)
    # dfs = DeepFace.find(img_path="img1.jpg", db_path="C:/workspace/my_db")
    # Extraer de dfs la matricula y agregarla a lista_identificados si no lo está
    # Mando mensaje
    # Leer JSON y obtenere numero
    # pywhatkit.sendwhatmsg("+910123456789", "Hi", 13, 30)

    # Mostramos los fotogramas
    # cv2.imshow(" Deteccion ", faces)

    # Leemos el teclado
    t = cv2.waitKey(1)
    if t == 27:
        break

cv2.destroyAllWindows()
cap.release()
