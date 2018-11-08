import serial

ports = ['COM%s' % (i + 1) for i in range(256)]

result = []

i = 0
for port in ports:
    try:
        globals()["s" + str(i)] = serial.Serial(port = port, baudrate= 19200)
        result.append(port)
        print("Connected")
    except(OSError, serial.SerialException):
        print("t")
        pass