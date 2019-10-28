from cmu_112_graphics import *
from tkinter import *
import cv2
import time
from threading import Thread
from PIL import Image


def appStarted(app):
    pass
    
def cameraFired(app):
    """
    -In cameraFired, you can use app.frame 
    -app.frame is a numpy array
    -openCV images are all numpy arrays
    """
    pass

def keyPressed(app, event):
    if event.key == "q":
        App._theRoot.app.quit()

def redrawAll(app, canvas):
    canvas.create_rectangle(0,0, app.width/2, app.height/2)

def timerFired(app):
    pass
        
if __name__ == "__main__":
    runApp(width=1080, height=720)