import sys
import common

data_buf = []


class protocol(common.protocol):

  @classmethod
  def printd(cls):
    for k,v in cls.cmd_dt.items():
      print "{}:{}".format(v,k.encode('hex'))

  @classmethod
  def crc_calc(cls, data):
    s = 0
    if len(data) >= cls.length - 1:
	  for i in data[cls.crc_start:cls.crc_end]:
	    s = cls.crc_operator(s, ord(i))
    #print data, cls.start.encode('hex'), cls.start.encode('hex')
    s = s & 0xff
    return s

  @classmethod
  def crc_check(cls, data, crc):
    if len(data) >= cls.length:
      if crc == ord(data[cls.length-1]):
        return True

    return False

  @classmethod
  def cmd_decode(cls, data):
    cmd = ''.join(data[2:4])
    dat = [ord(data[4]), ord(data[5])]

    res = ""
    for x in cls.cmd_lst:
      dat_tmp = dat[0] if x in cls.cmd_lst[0:2] else dat[1]
      if  cmd[0] == x[0] and ord(cmd[1]) & ord(x[1]): res = res + "{} {} ".format(cls.cmd_dt[x], dat_tmp)

    if cmd in cls.cmd_dt and not cmd in cls.cmd_lst:
      res = cls.cmd_dt[cmd]

    return res
  
  @classmethod
  def cmd_encode(cls, addr, cmd, data):
    res = ''
    
    cmd = cmd.split(' ')

    cmd_lst = []
    for x in cmd:
      tmp = '\x00\x00'
      for k,v in cls.cmd_dt.items():
        if v == x:
          tmp = k

      cmd_lst.append(tmp)
        
    if len(cmd_lst)==2:  
      res = [chr(ord(cmd_lst[0][0]) | ord(cmd_lst[1][0])), chr(ord(cmd_lst[0][1]) | ord(cmd_lst[1][1]))] 
    else:
      res = cmd_lst[0]
    
    l = [cls.start, chr(addr & 0xff), res[0], res[1], chr(data[0] & 0xff), chr(data[1] & 0xff), cls.end]
    l.append(chr(cls.crc_calc(l)))
    res = ''.join(l)

    return res

  @classmethod
  def printf(cls, data):
    crc_tmp = cls.crc_calc(data)
    print ' addr:{} cmd:{} data:{}({}) crc:{}={:02x}({})'.format(data[1].encode('hex'),
      ''.join(data[2:4]).encode('hex'),
      ''.join(data[4:6]).encode('hex'), cls.cmd_decode(data), 
      data[cls.length-1].encode('hex'), crc_tmp,
      'OK' if cls.crc_check(data, crc_tmp) else 'Fail')

  @classmethod
  def process(cls, data, cnt):
    global data_buf
  
    if data == cls.start:
      if data_buf:
        cls.printf(data_buf)
        data_buf = []

      cnt = 0

    else:
      cnt = cnt + 1

    print data.encode('hex'), 
    sys.stdout.softspace=False
    data_buf.append(data)
    #print(data_buf)

    return cnt

#a00700000000af08 addr:07 cmd:0000 data:0000 crc:08=08(OK) stop
#a00700020100af0b addr:07 cmd:0002 data:0100 crc:0b=0b(OK) right
#a00700040100af0d addr:07 cmd:0004 data:0100 crc:0d=0d(OK) letf
#a00700080001af01 addr:07 cmd:0008 data:0001 crc:01=01(OK) up
#a00700100000af18 addr:07 cmd:0010 data:0000 crc:18=18(OK) down
#a00700000000af08 addr:07 cmd:0000 data:0000 crc:08=08(OK) wide
#a00700200000af28 addr:07 cmd:0020 data:0000 crc:28=28(OK)
#a00700000000af08 addr:07 cmd:0000 data:0000 crc:08=08(OK) tele
#a00700400000af48 addr:07 cmd:0040 data:0000 crc:48=48(OK)
#a00700000000af08 addr:07 cmd:0000 data:0000 crc:08=08(OK) near
#a00702000000af0a addr:07 cmd:0200 data:0000 crc:0a=0a(OK)
#a00700000000af08 addr:07 cmd:0000 data:0000 crc:08=08(OK) far
#a00701000000af09 addr:07 cmd:0100 data:0000 crc:09=09(OK)
#a00700000000af08 addr:07 cmd:0000 data:0000 crc:08=08(OK) close
#a00708000000af00 addr:07 cmd:0800 data:0000 crc:00=00(OK)
#a00700000000af08 addr:07 cmd:0000 data:0000 crc:08=08(OK) open
#a00704000000af0c addr:07 cmd:0400 data:0000 crc:0c=0c(OK)
class p(protocol):
  start = "\xa0"
  end = "\xaf"
  length = 8
  crc_end = length - 1
  crc_operator = int.__xor__
  
  #cmd_dt = protocol.cmd_dt.copy()
  #cmd_dt['\x01\x00'] = 'far'
  #cmd_dt['\x02\x00'] = 'near'
  #cmd_dt['\x04\x00'] = 'open'
  #cmd_dt['\x08\x00'] = 'close'
  cmd_dt  = {"\x00\x00":"stop", 
             "\x00\x02":"right",
             "\x00\x04":"left",
             "\x00\x08":"up",
             "\x00\x10":"down",
             "\x00\x20":"wide",
             "\x00\x40":"tele",
             "\x01\x00":"far",
             "\x02\x00":"near",
             "\x04\x00":"open",
             "\x08\x00":"close"
             }  


#ff010000000001 addr:01 cmd:0000 data:0000 crc:01=01(OK) stop
#ff010002020005 addr:01 cmd:0002 data:0200 crc:05=05(OK) right
#ff010004020007 addr:01 cmd:0004 data:0200 crc:07=07(OK) left
#ff010008000009 addr:01 cmd:0008 data:0000 crc:09=09(OK) up
#ff010010000011 addr:01 cmd:0010 data:0000 crc:11=11(OK) down
#ff010000000001 addr:01 cmd:0000 data:0000 crc:01=01(OK) wide 
#ff010020000021 addr:01 cmd:0020 data:0000 crc:21=21(OK)
#ff010000000001 addr:01 cmd:0000 data:0000 crc:01=01(OK) tele 
#ff010040000041 addr:01 cmd:0040 data:0000 crc:41=41(OK)
#ff010000000001 addr:01 cmd:0000 data:0000 crc:01=01(OK) near 
#ff010100000002 addr:01 cmd:0100 data:0000 crc:02=02(OK)
#ff010000000001 addr:01 cmd:0000 data:0000 crc:01=01(OK) far 
#ff010080000081 addr:01 cmd:0080 data:0000 crc:81=81(OK)
#ff010000000001 addr:01 cmd:0000 data:0000 crc:01=01(OK) close
#ff010400000005 addr:01 cmd:0400 data:0000 crc:05=05(OK)
#ff010000000001 addr:01 cmd:0000 data:0000 crc:01=01(OK) open
#ff010200000003 addr:01 cmd:0200 data:0000 crc:03=03(OK)
class d(protocol):
  start = "\xff"
  length = 7
  crc_start = 1
  crc_end = length - 1

  #cmd_dt = protocol.cmd_dt

if __name__ == '__main__':
  #data = list("\xa0\x07\x00\x00\x00\x00\xaf\x08")
  data = list("\xa0\x07\x00\x0a\x01\x02\xaf\x01")
  print p.printf(data)