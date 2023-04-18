import pyautogui  # pip install pyautogui helps in automation
from PIL import Image, ImageGrab  # pip install pillow
from numpy import asarray
import time


def takeScreenshot():
    # converts to gray scale image. (as processing gray scale image is easier than processing colored images)
    image = ImageGrab.grab().convert('L')
    # image.show()
    return image


def hit(key):
    pyautogui.keyDown(key)
    return


def isCollide(data):
    for i in range(300, 470):
        for j in range(560, 650):
            if data[i, j] < 100:
                hit('up')
                return 
    for i in range(250, 300):
            for j in range(410, 550):
               if data[i, j] < 100:
                hit('down')
                return 

if __name__ == "__main__":
    print("Hey Dino game is about to start in 3 seconds")
    time.sleep(3)
    hit('up')
    while(True):
        image = takeScreenshot()
        data = image.load()
        # print(asarray(image))
        isCollide(data)
        
        # draw rectangle for cactus i.e, to check jump or not
        # for i in range(300, 450):
        #     for j in range(560, 650):
        #         data[i, j] = 0
                
        # draw rectangle for birds i.e, to check down or not
        # for i in range(250, 300):
        #     for j in range(410, 550):
        #         data[i, j] = 120

        # image.show()
