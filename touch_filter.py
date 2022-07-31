import subprocess

def get_xy():
    cmd = r'adb shell getevent'
    w = 0
    h = 0
    try:
        p1=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
        for line in p1.stdout:
            #print(line)
            line = line.decode(encoding="utf-8", errors="ignore")
            #print(line)
            line = line.strip()
            
            """
            if ' 0002 ' in line:
                e = line.split(" ")
                w = e[3]
                #w = int(w, 32)
                print(w)
            """
            if ' 0035 ' in line:
                #print(line)
                e = line.split(" ")
                w = e[3]
                w = int(w, 16)
                
            if  ' 0036 ' in line:
                #print(line)
                e = line.split(" ")
                h = e[3]
                h = int(h, 16)
                if h >0:
                    #p = (w, h)
                    print(w, h) 
        p1.wait()
        

    except Exception as e:
        print(e)

size = get_xy()
print(size)