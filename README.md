#ADB, RASPI, AND OTHER COOL STUFF I tried to do

Step 1: installing raspbian headless on RASPI 4
  Basically flashed and sd card
  added a file called ssh (no extension) into the boot [activates ssh]
  added a file called wpa_supplicant.conf [connects to wifi]
  Boot the pi and wait for the pi to load
  On another computer open ssh and connect to pi@raspberry.local
  Done
 
Step 2: ADB on raspbian
  sudo apt-get install android-tools-adb android-tools-fastboot
  test the installation using command using "adb" and "adb start-server"

Step 3: Android Phone
  Go to system info, tap on the IMEI serial until it activates developer mode
  Go to developer menu and activate adb through usb debugging

Step 2 Part 2: 
  For python library, I used pure-python-adb
  pip install pure-python-adb
  Start server using "adb start-server" first, python will not work without this 
  
  
  
