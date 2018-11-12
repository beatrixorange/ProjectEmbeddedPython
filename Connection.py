import serial
import threading
import queue
import Controller

ports = ['COM%s' % (i + 1) for i in range(256)]

queue = queue.Queue(1000)
connections = []
threads = []

light_list = {}        # key = id, value = list with lightsensor info
temperature_list = {}         # key = id, value = list with temperature sensor info
i = 0


def sum_array_elements(list):
    result = 0
    count = 0
    for i in list:
        temp = pow(10, len(list) - count - 1);
        result += int(list[count]) * temp
        count = count + 1
    return result

def inlezen(s):
    while True:
        x = s.read()
        if (ord(x) < 128):
            if(x != None and x != '' and x.hex != None and x.hex != ''):
                x = bytes(x).decode()
                if x == '#':
                    checker = False
                    id = 0
                    distance = []
                    count = 0
                    running = 1
                    while running == 1 and x != '&' and x != '$' and x != '%':
                        x = s.read()
                        if (ord(x) < 128):
                            x = bytes(x).decode()
                            if x != '.' and checker is False:       # fetch ID
                                id = x
                            elif x == '.' and checker is False:     # switch to number
                                checker = True
                            elif x != "." and x != '#' and checker is True:       # save number as distance
                                distance.append(int(x))
                                count = count + 1
                            elif x == '#' and checker is True:
                                running = 0
                    result = sum_array_elements (distance)
                    print("Distance: " + str(result) + ", ID: " + id)
                    Controller.frames["Arduino"+id].get_uitrol_afstand()['text'] = "Het rolluik is " + str(result) + " cm uitgerold";

                if x == '$':
                    checker = 0
                    id = 0
                    brightness = []
                    running = 1
                    while running == 1  and x != '&' and x != '#' and x != '%':
                        x = s.read()
                        if (ord(x) < 128):
                            x = bytes(x).decode()
                            if x != '.' and checker == 0:  # fetch ID
                                id = x
                            elif x == '.' and checker == 0:  # switch to number
                                checker = 1
                            elif x != "." and x != '$' and checker == 1:  # save number as distance
                                brightness.append(x)
                            elif x == '$' and checker == 1:
                                running = 0
                    result = sum_array_elements(brightness)
                    print("Light: " + str(result) + ", ID: " + id)
                    if (light_list.keys().__contains__(id)):
                        light_list[id].append(int(result))
                    else:
                        light_list[id] = []
                        light_list[id].append(int(result))

                if x == '%':
                    checker = False
                    id = 0
                    temperatures = []
                    running = 1
                    while running == 1 and x != '&' and x != '$' and x != '#':
                        x = s.read()
                        if (ord(x) < 128):
                            x = bytes(x).decode()
                            if x != '.' and checker is False:  # fetch ID
                                id = x
                            elif x == '.' and checker is False:  # switch to number
                                checker = True
                            elif x != "." and x != '%' and checker is True:  # save number as distance
                                temperatures.append(x)
                            elif x == '%' and checker is True:
                                running = 0
                    result = sum_array_elements(temperatures)
                    print("Temperature: " + str(result) + ", ID: " + id)
                    if (temperature_list.keys().__contains__(id)):
                        temperature_list[id].append(int(result))
                    else:
                        temperature_list[id] = []
                        temperature_list[id].append(int(result))

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

