from deepface import DeepFace
from deepface.commons.realtime import analysis

print('hello world')
DeepFace.stream(db_path='../pics', enable_face_analysis=False)

# data = analysis(db_path='../pics')
# print(data)
