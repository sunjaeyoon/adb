"""
SIMPLE SCRIPT that screenshots and scrolls down the screen


"""

"""
from ppadb.client import Client as AdbClient
# Default is "127.0.0.1" and 5037
client = AdbClient(host="127.0.0.1", port=5037)
print(client.version())
device = client.device("emulator-5554")
"""

from ppadb.client import Client as AdbClient
import time
import numpy as np
import cv2

def getDevice(ip="127.0.0.1", p=5037, name="RZ8N223B6RM"):
    # Default is "127.0.0.1" and 5037
    client = AdbClient(host=ip, port=p)
    device = client.device(name)
    return device

def ADBtest():
    """PROTOTYPYING FOR MAIN FUNCTION"""
    device = getDevice()
    #while True:
    #device.shell('input touchscreen swipe 530 1420 530 1120')
    result = device.screencap()
    print(type(result))
    #print(result)
    decoded = cv2.imdecode(np.frombuffer(result, np.uint8), -1)
    print(decoded.shape)
    cv2.imwrite("test.png", decoded)

    #Save image from bytearray
    with open("screen.png", "wb") as fp:
        fp.write(result)
    
    reopen = cv2.imread("screen.png")
    reopen2 = cv2.imread("test.png")

    #ARE BOTH approaches the same value
    print(reopen.shape)
    print(reopen2.shape)
    print(np.array_equal(reopen, reopen2))
    
    #Test template finding
    template = cv2.imread("camera.png", 0)
    
    
    time.sleep(5)

def CVtest():
    device = getDevice()
    #Template Finding
    template = cv2.imread("continue.png", 0)
    screen = cv2.imread("screen.png")
    img_gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)

    print(template.shape)
    print(screen.shape)

    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.85
    loc = np.where( res >= threshold)

    print(loc[0].shape[0])
    for pt in zip(*loc[::-1]):
        print(pt)
        cv2.rectangle(screen, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
        device.shell(f'input touchscreen tap {pt[0]} {pt[1]}')
    
    cv2.imwrite('res.png', screen)

def main():
    rounds = 1
    while True:
    #for _ in range(20):
        #Get Device and Screen
        device = getDevice()
        #device.shell('input touchscreen swipe 530 1420 530 1120')
        time.sleep(2)
        result = device.screencap()
        
        print(f"Round {rounds}")
        #print(result)
        result = cv2.imdecode(np.frombuffer(result, np.uint8), -1)
        #print(result.shape)
        cv2.imwrite("screen.png", result)

        #Template Finding
        template = cv2.imread("continue.png", 0)
        screen = cv2.imread("screen.png")
        img_gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)

        w, h = template.shape[::-1]
        res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
        threshold = 0.90
        loc = np.where( res >= threshold)

        print("Found:", loc[0].shape[0])
        for pt in zip(*loc[::-1]):
            rounds += 1
            print(pt)
            cv2.rectangle(screen, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
            device.shell(f'input touchscreen tap {pt[0]+10} {pt[1]+10}') 
            break
        if rounds == 20:
            break 

        time.sleep(60*6)


if __name__ == "__main__":
    #ADBtest()
    #CVtest()
    main()
