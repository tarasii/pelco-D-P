import plt.pelco

#data = list("\xa0\x07\x00\x00\x00\x00\xaf\x08")

data = plt.pelco.p.cmd_encode(7,"left",[1,0])
print data.encode('hex')
#print plt.pelco.p.cmd_decode(data)
plt.pelco.p.printf(data)