import serial
import threading
import queue
import Pages
ports = ['COM%s' % (i + 1) for i in range(256)]

queue = queue.Queue(1000)
connections = []
threads = []

licht_list = []
temp_list = []
i = 0


def inlezen(s):
    # TODO Uitvinden wat we met het ID doen.
    while True:
        x = s.read()
        if(x != None and x != '' and x.hex != None and x.hex != ''):
            if x == "#":
                while True:
                    if x != ".":
                        x = s.read()
                        id = x
                    else:
                        if x != "#":
                            x = s.read()
                            afstand = str(afstand) + x
                        else:
                            Pages.afstand_list.append(int(afstand))
                            break
            if x == "$":
                while True:
                    if x != "$":
                        x = s.read()
                        licht = str(licht) + x
                    else:
                        licht_list.append(licht)
                        break
            if x == "%":
                while True:
                    if x != "%":
                        x = s.read()
                        temp = str(temp) + x
                    else:
                        temp_list.append(temp)
                        break


def stuur_id():
    i = 1
    for c in connections:
        char1 = "&".encode()
        id = str(i).encode()
        c.write(char1)
        c.write(id)
        c.write(char1)
        i = i + 1

for port in ports:
    try:
        s = serial.Serial(port=port, baudrate=19200)
        thread = threading.Thread(target=inlezen, args=(s,),).start()
        threads.append(thread)
        connections.append(s)
        stuur_id()
        print("Connected")
    except(OSError, serial.SerialException):
        pass

