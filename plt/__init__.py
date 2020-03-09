import pelco



#a00700000000af08 addr:07 cmd:0000 data:0000 crc:08=08(OK) stop
#a00700020100af0b addr:07 cmd:0002 data:0100 crc:0b=0b(OK) right
#a00700040100af0d addr:07 cmd:0004 data:0100 crc:0d=0d(OK) left
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
#a00700000000af08 addr:07 cmd:0000 data:0000 crc:08=08(OK)
class samsung(pelco.p):
  pass

#ff080000000008 addr:08 cmd:0000 data:0000 crc:08=08(OK) stop
#ff08000200000a addr:08 cmd:0002 data:0000 crc:0a=0a(OK) right
#ff080004090015 addr:08 cmd:0004 data:0900 crc:15=15(OK) left
#ff080008000212 addr:08 cmd:0008 data:0002 crc:12=12(OK) up
#ff08001000031b addr:08 cmd:0010 data:0003 crc:1b=1b(OK) down
#ff080000000008 addr:08 cmd:0000 data:0000 crc:08=08(OK) wide
#ff080020000028 addr:08 cmd:0020 data:0000 crc:28=28(OK)
#ff080000000008 addr:08 cmd:0000 data:0000 crc:08=08(OK) tele
#ff080040000048 addr:08 cmd:0040 data:0000 crc:48=48(OK)
#ff080000000008 addr:08 cmd:0000 data:0000 crc:08=08(OK) near
#ff080100000009 addr:08 cmd:0100 data:0000 crc:09=09(OK)
#ff080000000008 addr:08 cmd:0000 data:0000 crc:08=08(OK) far
#ff080080000088 addr:08 cmd:0080 data:0000 crc:88=88(OK)
#ff080000000008 addr:08 cmd:0000 data:0000 crc:08=08(OK) close
#ff08040000000c addr:08 cmd:0400 data:0000 crc:0c=0c(OK)
#ff080000000008 addr:08 cmd:0000 data:0000 crc:08=08(OK) open
#ff08020000000a addr:08 cmd:0200 data:0000 crc:0a=0a(OK)
class yaan(pelco.d):
  pass

#ff080000000008 addr:08 cmd:0000 data:0000 crc:08=08(OK) stop
#ff010002010004 addr:01 cmd:0002 data:0100 crc:04=04(OK) right
#ff010004010006 addr:01 cmd:0004 data:0100 crc:06=06(OK) left
#ff01000800010a addr:01 cmd:0008 data:0001 crc:0a=0a(OK) up
#ff010010000112 addr:01 cmd:0010 data:0001 crc:12=12(OK) down
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
class panasonic(pelco.d):
  pass

#fa0300010200a2a8 addr:03 cmd:0001 data:0200
#fa0300010800a2ae addr:03 cmd:0001 data:0800
#fa0300010800a2ae addr:03 cmd:0001 data:0800
#fa0300030000a2a8 addr:03 cmd:0003 data:0000
#fa0300020000a2a7 addr:03 cmd:0002 data:0000
#fa0300020a00a2b1 addr:03 cmd:0002 data:0a00
#fa0300021100a2b8 addr:03 cmd:0002 data:1100
#fa0300020e00a2b5 addr:03 cmd:0002 data:0e00
#fa0300030000a2a8 addr:03 cmd:0003 data:0000
#fa0300040002a2ab addr:03 cmd:0004 data:0002
#fa030004000da2b6 addr:03 cmd:0004 data:000d
#fa0300040011a2ba addr:03 cmd:0004 data:0011
#fa0300030000a2a8 addr:03 cmd:0003 data:0000
#fa0300080002a2af addr:03 cmd:0008 data:0002
#fa0300080010a2bd addr:03 cmd:0008 data:0010
#fa0300030000a2a8 addr:03 cmd:0003 data:0000
#fa0300080002a2af addr:03 cmd:0008 data:0002
#fa03000a020aa2bb addr:03 cmd:000a data:020a
#fa0300080009a2b6 addr:03 cmd:0008 data:0009

#fa0300030000a2a8 addr:03 cmd:0003 data:0000 close
#fa03000b0000a2b0 addr:03 cmd:000b data:0000 
#fa0300070000a2ac addr:03 cmd:0007 data:0000 open
#fa03000c0000a2b1 addr:03 cmd:000c data:0000
#fa0300070000a2ac addr:03 cmd:0007 data:0000 near
#fa03000d0000a2b2 addr:03 cmd:000d data:0000
#fa0300070000a2ac addr:03 cmd:0007 data:0000 far
#fa03000e0000a2b3 addr:03 cmd:000e data:0000

#fa0300030000a2a8 addr:03 cmd:0003 data:0000 wide after 1-a
#fa03000f0000a2b4 addr:03 cmd:000f data:0000
#fa0300070000a2ac addr:03 cmd:0007 data:0000 wide after wide
#fa03000f0000a2b4 addr:03 cmd:000f data:0000

#fa0300030000a2a8 addr:03 cmd:0003 data:0000 tele after 1-a
#fa0300100000a2b5 addr:03 cmd:0010 data:0000
#fa0300070000a2ac addr:03 cmd:0007 data:0000 tele after tele
#fa0300100000a2b5 addr:03 cmd:0010 data:0000
#fa0300070000a2ac addr:03 cmd:0007 data:0000 wide after tele
#fa03000f0000a2b4 addr:03 cmd:000f data:0000

#fa0300080044a2f1 addr:03 cmd:0008 data:0044 crc:f1=f1(OK)
#fa0300030000a2a8 addr:03 cmd:0003 data:0000 crc:a8=a8(OK) off after
#fa0000860100a229 addr:00 cmd:0086 data:0100 crc:29=29(OK) off after off
#fa0000860100a229 addr:00 cmd:0086 data:0100 crc:29=29(OK)
#fa0000860100a229 addr:00 cmd:0086 data:0100 crc:29=29(OK) on after off
#fa0000850100a228 addr:00 cmd:0085 data:0100 crc:28=28(OK) on after on
#fa0000850100a228 addr:00 cmd:0085 data:0100 crc:28=28(OK) on after on
#fa0300080044a2f1 addr:03 cmd:0008 data:0044 crc:f1=f1(OK)
#fa0300030000a2a8 addr:03 cmd:0003 data:0000 crc:a8=a8(OK) on after
#fa0000850100a228 addr:00 cmd:0085 data:0100 crc:28=28(OK) on after on
#fa0000850100a228 addr:00 cmd:0085 data:0100 crc:28=28(OK) off after on
#fa0000860100a229 addr:00 cmd:0086 data:0100 crc:29=29(OK) off after off

#fazz0001yy00a2qq: up    yy
#fazz0002yy00a2qq: down  yy
#fazz000400xxa2qq: left  xx
#fazz000800xxa2qq: right xx
class ad2200(pelco.protocol):
  start = "\xfa"
  end = "\xa2"
  length = 8
  crc_start = 1
  crc_end = length - 1

  cmd_dt  = {"\x00\x00":"stop", 
             "\x00\x08":"right",
             "\x00\x04":"left",
             "\x00\x01":"up",
             "\x00\x02":"down",
             "\x00\x0f":"wide",
             "\x00\x10":"tele",
             "\x00\x0e":"far",
             "\x00\x0d":"near",
             "\x00\x0c":"open",
             "\x00\x0b":"close",
             }
  cmd_lst = ["\x00\x02", "\x00\x01", "\x00\x08", "\x00\x04"]
