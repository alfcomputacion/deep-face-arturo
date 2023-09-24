# Importamos las librerias
from deepface import DeepFace
import cv2
import mediapipe as mp
import imutils
import time
import os
import json
# import pywhatkit

# Declaramos la deteccion de rostros

# Recortar el rostro
# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# cap = cv2.VideoCapture('entrada_1.mp4')
cap = cv2.VideoCapture('./VIDEO/entrada.mp4')

faceClassif = cv2.CascadeClassifier(
    cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
# count = 0
lista = []
while True:

    ret, frame = cap.read()
    if ret == False:
        break
    frame = imutils.resize(frame, width=840)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxFrame = frame.copy()

    faces = faceClassif.detectMultiScale(gray, 1.3, 10)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 3)
        rostro = auxFrame[y:y+h, x:x+w]
        rostro = cv2.resize(rostro, (150, 150), interpolation=cv2.INTER_CUBIC)
        # cv2.imwrite(personPath + '/al153168_{}.jpg'.format(count), rostro)
        dfs = DeepFace.find(
            img_path=rostro, db_path='../pics', enforce_detection=False, silent=True)
        source_x = dfs[0]['source_x']
        source_y = dfs[0]['source_y']
        # candidate = dfs.iloc[0]
        # label = candidate["identity"]
        # print(rostro)

        #! **************EXTRACT as FUNCTION****************************************
        if dfs and source_y.any() and source_x.any():
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
                    lista.append(str(information['Alumno'][0]['matricula']))
        #! ******************************************************

        # count = count + 1
    cv2.imshow('frame', frame)
    # time.sleep(1)
    # Identificar rostro (fs = DeepFace.find)
    # dfs = DeepFace.find(img_path="img1.jpg", db_path="C:/workspace/my_db")
    # Extraer de dfs la matricula y agregarla a lista_identificados si no lo está
    # Mando mensaje
    # Leer JSON y obtenere numero
    # pywhatkit.sendwhatmsg("+910123456789", "Hi", 13, 30)

    # Mostramos los fotogramas
    # cv2.imshow(" Deteccion ", faces)

    # Leemos el teclado
    t = cv2.waitKey(5)
    if t == 27:
        break

cv2.destroyAllWindows()
cap.release()
