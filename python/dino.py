import pyautogui
from PIL import Image, ImageGrab
import time


def hit(key):
    pyautogui.keyDown(key)
    return

def isColloide(data):
    # rectangle for birds
    for i in range(190, 295):
        for j in range(320, 418):
            if data[i, j] < 100:
                hit("down")
                return 
    # rectangle for cactus
    for i in range(220, 265):
        for j in range(418, 490):
            if data[i, j] < 100:
                hit("up") 
                return 
    return 
    
if __name__ == "__main__":
    print("game is starting in 3 seconds")
    time.sleep(3)
    hit('up')

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isColloide(data)
        

        # # rectangle for cactus
        # for i in range(220, 265):
        #     for j in range(418, 490):
        #         data[i, j] = 0
        # # rectangle for birds
        # for i in range(190, 250):
        #     for j in range(320, 418):
        #         data[i, j] = 171
    
        # image.show()
        # break    