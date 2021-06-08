"""
from ppadb.client import Client as AdbClient
# Default is "127.0.0.1" and 5037
client = AdbClient(host="127.0.0.1", port=5037)
print(client.version())

device = client.device("emulator-5554")
"""

from ppadb.client import Client as AdbClient
import time

def getDevice(ip="127.0.0.1", p=5037, name="RZ8N223B6RM"):
    # Default is "127.0.0.1" and 5037
    client = AdbClient(host=ip, port=p)
    device = client.device(name)
    return device

def main():
    device = getDevice()
    while True:
        device.shell('input touchscreen swipe 530 1420 530 1120')
        result = device.screencap()
        with open("screen.png", "wb") as fp:
            fp.write(result)
        time.sleep(10)

if __name__ == "__main__":
    main()
