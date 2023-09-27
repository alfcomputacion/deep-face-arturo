import json
import pywhatkit
import time
alumnos_list = []

with open('../Lista_alumnos_25_9_2023_.json', 'r') as lista:
    alumnos_list = json.load(lista)
    # print(alumnos_list)


for i in range(0, len(alumnos_list['Alumno'])):
    print(alumnos_list['Alumno'][i]['matricula'])

    number = str(alumnos_list['Alumno'][i]['tel_contacto'])
    nombre = alumnos_list['Alumno'][i]['nombre']
    pywhatkit.sendwhatmsg_instantly(
        "+" + number, 'Hi, ' + nombre + ' was in today.')
    time.sleep(5)
