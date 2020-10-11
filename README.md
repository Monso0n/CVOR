# CVOR (Computer Vision Object Recognition)
**CVOR** is a **Python** application which highlights select objects (such as cats, smiles, and faces) from image files. The graphical user interface is built using **Tkinter** toolkit, and the object recognition is done by the amazing and capable **OpenCV** library.
---

# How to run CVOR
To run CVOR, the following must be installed: 
* Python
* OpenCV for Python. Click [here](https://docs.opencv.org/master/d5/de5/tutorial_py_setup_in_windows.html) for detailed information.
* The CVOR repository.

## Next:
1. To run CVOR, open GUI2.py from the CVOR repo. This will launch the user interface for the program. 
2. From here, check the boxes for the objects that you would like to detect. 
3. Click the 'Select File' button and select a valid image file from your computer.
4. Click 'Run' and a new window will pop up, highlighting the detected objects alongside the name of the cascade. 

## CVOR can detect the following objects: ##
* Eyes (left eye, right eye, can detect eyes on faces with glasses)
* Frontal Human Faces
* Frontal Cat Faces
* Profile Faces
* Upper Bodies
* Lower Bodies

CVOR is built in Python. The GUI is built upon Tkinter. The object recognition is processed by the OpenCV library. The cascades utilized are [haarcascades](https://github.com/opencv/opencv/tree/master/data/haarcascades).
