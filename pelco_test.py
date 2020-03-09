import serial
import sys
import plt
import plt.pelco
import plt.common



ser = serial.Serial ('/dev/ttyUSB0')
ser.baudrate = 9600

if not ser.is_open:
  quit()

#print plt.pelco.d.printd()

cnt = 0
cq = ord('q')
while True:
  try:
    data = ser.read(1)
  except:
    break

  #cnt = plt.common.default.process(data, cnt) #16 by 8
  #cnt = plt.common.default.process(data, cnt, 7, 14) #14 by 7 for pelco-d

  #cnt = plt.ad2200.process(data, cnt)
  #cnt = plt.pelco.p.process(data, cnt)
  cnt = plt.pelco.d.process(data, cnt)
  #cnt = plt.yaan.process(data, cnt)
  #cnt = plt.panasonic.process(data, cnt)
  #cnt = plt.samsung.process(data, cnt)


ser.close()
