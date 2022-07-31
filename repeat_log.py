from ppadb.client import Client as AdbClient
import time
import cv2

def getDevice(ip="127.0.0.1", p=5037, name="RZ8N223B6RM"):
    # Default is "127.0.0.1" and 5037
    client = AdbClient(host=ip, port=p)
    device = client.device(name)
    return device

def main():
    device = getDevice()

    with open('./commission.txt', 'r') as f:
        for line in f:
            x, y = line.split(' ')
            x = int(x)
            y = int(y)
            print(y ,x)
            device.shell(f'input touchscreen tap {1560-y} {x}')
            time.sleep(5)

main()

#screen = cv2.imread('screen.png')
#print(screen.shape)