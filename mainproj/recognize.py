from deepface import DeepFace
from deepface.commons.realtime import analysis

import asyncio
import threading
# print('hello world')
# DeepFace.stream(db_path='../pics')
DeepFace.stream(db_path='../pics', enable_face_analysis=False,
                time_threshold=5, frame_threshold=5)

# data =
# threading.Thread(target=analysis, daemon=True).start


# async def startCamera():
#     await analysis(db_path='../pics')
#     # await DeepFace.verify(db_path='../pics')
# # print(data)


# async def main():
#     await startCamera()


# if __name__ == "__main__":
#     asyncio.run(main())
