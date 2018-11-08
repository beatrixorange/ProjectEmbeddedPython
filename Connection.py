import serial

ports = ['COM%s' % (i + 1) for i in range(256)]

result = []
connections = []
i = 0
for port in ports:
    try:
        s = serial.Serial(port=port, baudrate=19200)
        connections.append(s)
        result.append(port)
        print("Connected")
    except(OSError, serial.SerialException):
        print("t")
        pass