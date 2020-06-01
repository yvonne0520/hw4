import serial
import time
import numpy as np
import matplotlib.pyplot as plt

# XBee setting
serdev = '/dev/ttyUSB0'
s = serial.Serial(serdev, 9600)
num = []
times = 20

s.write("+++".encode())
ch = s.read(2)
s.write("ATMY <0x205>\r\n".encode())
ch = s.read(3)
s.write("ATDL <0x305>\r\n".encode())
ch = s.read(3)
s.write("ATID <0x1>\r\n".encode())
ch = s.read(3)
s.write("ATWR\r\n".encode())
ch = s.read(4)
s.write("ATMY\r\n".encode())
ch = s.read(4)
s.write("ATDL\r\n".encode())
ch = s.read(4)
s.write("ATCN\r\n".encode())
ch = s.read(3)

print("start sending RPC")

for i in range(0, times):
    s.write("/getNum/run\r".encode())
    tmp = int(s.readline())
    print(tmp)
    num.append(tmp)
    time.sleep(1)
s.close()

x = np.array(range(1,len(num)+1))
plt.plot(x,num)
plt.show()