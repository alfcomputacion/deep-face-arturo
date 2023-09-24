import cv2
import os
import imutils
from datetime import datetime
import random
import string
import time


def random_string(numchars=10):
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(numchars))


now = datetime.now()
personName = 'Lista'
# ruta donde hayas almacenado folder del alumno
dataPath = '../pics/PROYECT_2023'
personPath = dataPath + '/' + personName

if not os.path.exists(personPath):
    print('Carpeta creada: ', personPath)
    os.makedirs(personPath)

# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# cap = cv2.VideoCapture('entrada_1.mp4')
cap = cv2.VideoCapture('./VIDEO/entrada.mp4')

faceClassif = cv2.CascadeClassifier(
    cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
count = 0
skip = 0
while True:

    ret, frame = cap.read()
    if ret == False:
        break
    frame = imutils.resize(frame, width=840)

    if skip > 4:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        auxFrame = frame.copy()
        faces = faceClassif.detectMultiScale(gray, 1.3, 10)
        skip = 0
        for (x, y, w, h) in faces:
            file = random_string()
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 3)
            rostro = auxFrame[y:y+h, x:x+w]
            rostro = cv2.resize(rostro, (300, 300),
                                interpolation=cv2.INTER_CUBIC)
            cv2.imwrite(personPath + '/al{}{}.jpg'.format(count, file), rostro)
            count = count + 1
        cv2.imshow('frame', frame)
    skip += 1

    k = cv2.waitKey(1)
    if k == 0:
        break

cap.release()
cv2.destroyAllWindows()
