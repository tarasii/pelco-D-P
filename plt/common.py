import sys

class protocol():
  start = ""
  end = ""
  length = 0
  crc_start = 0
  crc_end = 0
  crc_operator = int.__add__

  cmd_dt  = {"\x00\x00":"stop", 
             "\x00\x02":"right",
             "\x00\x04":"left",
             "\x00\x08":"up",
             "\x00\x10":"down",
             "\x00\x20":"wide",
             "\x00\x40":"tele",
             "\x00\x80":"far",
             "\x01\x00":"near",
             "\x02\x00":"open",
             "\x04\x00":"close"
             }
  cmd_lst = ["\x00\x02", "\x00\x04", "\x00\x08", "\x00\x10"]


  @classmethod
  def process(cls, data, cnt):

    print data.encode('hex') 
    cnt = cnt + 1

    return cnt


class default(protocol):

  @classmethod
  def process(cls, data, cnt, sp=8, nl=16):

    print data.encode('hex'), 
    sys.stdout.softspace=False

    #if (cnt > 0)and(((cnt-7)  % sp) == 0):
    if (((cnt-sp+1)  % sp) == 0):
      print ' ',

    if cnt >= nl - 1:
      print ''
      cnt = 0
    else:
      cnt = cnt + 1

    return cnt
