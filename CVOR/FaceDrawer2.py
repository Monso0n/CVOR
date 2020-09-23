import cv2
import os
from random import randrange

class FaceDrawer():
    def __init__(self, path, stack):
        self.path = path #this is the path of the image
        self.dirname = os.path.dirname(__file__)

        directory = {  #this dictionary points to the path of the cascade files
            "Eye": r"\haarcascades\haarcascade_eye.xml",
            "Eye Tree Glasses": r"\haarcascades\haarcascade_eye_tree_eyeglasses.xml",
            "Frontal Cat Face": r"\haarcascades\haarcascade_frontalcatface.xml",
            "Frontal Cat Face Extended": r"\haarcascades\haarcascade_frontalcatface_extended.xml",
            "Frontal Face Alt": r"\haarcascades\haarcascade_frontalface_alt.xml",
            "Frontal Face Alt Tree": r"\haarcascades\haarcascade_frontalface_alt_tree.xml",
            "Frontal Face Alt 2": r"\haarcascades\haarcascade_frontalface_alt2.xml",
            "Frontal Face Default": r"\haarcascades\haarcascade_frontalface_default.xml",
            "Full Body": r"\haarcascades\haarcascade_fullbody.xml",
            "Left Eye (2 Splits)": r"\haarcascades\haarcascade_lefteye_2splits.xml",
            "Right Eye (2 Splits)": r"\haarcascades\haarcascade_righteye_2splits.xml",
            "Lower Body": r"\haarcascades\haarcascade_lowerbody.xml",
            "Upper Body": r"\haarcascades\haarcascade_upperbody.xml",
            "Profile Face": r"\haarcascades\haarcascade_profileface.xml",
            "Smiles": r"\haarcascades\haarcascade_smile.xml"
        }

        self.paths = []
        for i in stack:
            if i != "0":
                self.paths.append((i,directory[i]))


        self.faces = cv2.CascadeClassifier(r"D:\University\OpenCV Python\opencv-master\data\haarcascades\haarcascade_frontalface_alt.xml")

    def drawFace(self):

        self.image = cv2.imread(self.path)
        self.grayimg = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)


        for i in self.paths:
            self.faces = cv2.CascadeClassifier(self.dirname + i[1])

            print(f"trying {self.dirname + i[1]}")
            detected = self.faces.detectMultiScale(self.grayimg, scaleFactor=1.1, minNeighbors=6)

            color = (randrange(256), randrange(256), randrange(256))

            for(x, y, width, height) in detected:
                cv2.rectangle(self.image, (x, y), (x+width, y+height), color, 2)
                cv2.putText(self.image, i[0], (x, y), cv2.FONT_HERSHEY_PLAIN, 1, color, 1, cv2.LINE_AA)


        cv2.imshow("FaceDrawer", self.image)
        cv2.waitKey(0)
