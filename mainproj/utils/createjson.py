import json
import datetime
import os

print(os.path.abspath(os.getcwd()))
path = os.path.abspath(os.getcwdb())
# JSON data:
# x = '''{
#     "Alumno":
# }'''

# # python object to be appended
# # y = {"pin": 110096}
# y = {
#     "matricula": 131321,
#     "nombre": "Jose",
#     "apellidos": "Rosas Sanchez",
#     "tel_contacto": 1512328123246
# }

# # parsing JSON string:
# z = json.loads(x)

# # appending the data
# z.update(y)

# # the result is a JSON string:
# print(json.dumps(z))


# """
# {
#     "Alumno": [
#         {
#             "matricula": 153168,
#             "nombre": "Arturo",
#             "apellidos": "Padilla Rodriguez",
#             "tel_contacto": 1526562810246
#         }
#     ]
# }
# """
alumno = {
    "Alumno": [
        {
            "matricula": 1512345,
            "nombre": "Angelina",
            "apellidos": "Jolie",
            "tel_contacto": 13234233555
        }
    ]
}


def create_json(file, data):
    with open(file, 'w') as f:
        json.dump(data, f)


def append_json(filepath, matricula, nombre, apellidos, tel):
    now = str(datetime.datetime.now())
    with open(filepath, 'r') as fp:
        information = json.load(fp)

        information["Alumno"].append({
            "matricula": matricula,
            "nombre": nombre,
            "apellidos": apellidos,
            "tel_contacto": tel,
            "hora": now,
        })

    with open(filepath, 'w') as fp:
        json.dump(information, fp, indent=2)


def delobject(name="jose"):
    obj = json.load(open('asistencia.json'))

    # Iterate through the objects in the JSON and pop (remove)
    # the obj once we find it.
    for i in range(len(obj)):
        if obj[i]["nombre"] == name:
            print(obj[i])
            obj.pop(i)
        break


# delobject('Jose')
# append_statistics('asistencia.json', 100, 90, 15)
# create_json("lista223.json", alumno)
print(datetime.date.today())
print(str(datetime.date.today().year))
