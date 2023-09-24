from deepface import DeepFace
import matplotlib.pyplot as plt
import cv2


def verify(img1_path, img2_path):
    img1 = cv2.imread(img1_path)
    img2 = cv2.imread(img2_path)

    # plt.imshow(img1[:, :, ::-1])
    # plt.show()
    # plt.imshow(img2[:, :, ::-1])
    # plt.show()

  # models = ["VGG-Face", "Facenet", "OpenFace", "DeepFace", "DeepID", "Dlib", "ArcFace"]
    result = DeepFace.verify(img1_path, img2_path)
    print('result:', result)

    verification = result
    print(result)
    if verification:
        print('NO son la misma persona')
    else:
        print('Son la misma persona')

# verify('Luis1.jpg', 'img20.jpg')
