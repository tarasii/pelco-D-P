import serial
import sys
import ptz.pelco
import ptz.common



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

  #cnt = ptz.common.default.process(data, cnt) #16 by 8
  #cnt = ptz.common.default.process(data, cnt, 7, 14) #14 by 7 for pelco-d

  #cnt = ptz.ad2200.process(data, cnt)
  #cnt = ptz.pelco.p.process(data, cnt)
  cnt = ptz.pelco.d.process(data, cnt)
  #cnt = ptz.yaan.process(data, cnt)
  #cnt = ptz.panasonic.process(data, cnt)
  #cnt = ptz.samsung.process(data, cnt)


ser.close()
