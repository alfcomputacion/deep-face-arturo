import json
import pywhatkit

alumnos_list = []

with open('../Lista_alumnos_25_9_2023_.json', 'r') as lista:
    alumnos_list = json.load(lista)
    # print(alumnos_list)

for i, v in alumnos_list.items():

    # print(i)
    print(v[0]['tel_contacto'])
    number = str(v[0]['tel_contacto'])
    pywhatkit.sendwhatmsg_instantly("+" + number, "Hi, from sendText")
