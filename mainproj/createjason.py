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

def append_statistics(filepath, num_of_posts, followers, following):

    with open(filepath, 'r') as fp:
        information = json.load(fp)

    information["Alumno"].append({
        "matricula": 153168,
        "nombre": "Arturo",
        "apellidos": "Padilla Rodriguez",
        "tel_contacto": 1526562810246
    })

    with open(filepath, 'w') as fp:
        json.dump(information, fp, indent=2)


def delobject(name):
    obj = json.load(open('asistencia.json'))

    # Iterate through the objects in the JSON and pop (remove)
    # the obj once we find it.
    for i in range(len(obj)):
        # if obj[i]["nombre"] == "Jose":
        print(obj[i])
        # obj.pop(i)
        # break


delobject('Jose')
append_statistics('asistencia.json', 100, 90, 15)
