import Tkinter as tk
import ttk
import ptz.pelco
import serial

addr = 0
buf = 0

pos = 0

mouse = False  
x = 0
y = 0

ser = 0
connected = False
proto = ptz.pelco.d

def on_closing():
  global ser
  global connected

  if connected:
    ser.close()

  quit()

root = tk.Tk()
root.title("Pelco keyboard controller emulator")
root.protocol("WM_DELETE_WINDOW", on_closing)
frame = tk.Frame(root)
frame.pack()

frp = tk.Frame(frame)
frp.grid(column=0, row=0, columnspan=6)

lbl_port = tk.Label(frp, text="port:")
lbl_port.pack(side = tk.LEFT)

v_port = tk.StringVar()
e_port = tk.Entry(frp, textvariable=v_port, width=12)
e_port.pack(side = tk.LEFT)
v_port.set("/dev/ttyUSB0")

lbl_port = tk.Label(frp, text="speed:")
lbl_port.pack(side = tk.LEFT)

v_speed = tk.StringVar()
e_speed = ttk.Combobox(frp, textvariable=v_speed, width=6, values=['1200', '2400', '4800', '9600'])
e_speed.pack(side = tk.LEFT)
e_speed.current(3)

def connect():
  global ser
  global connected

  if connected:
    ser.close()
    connected = False
    b_conn.config(text="CONNECT")
  else:
    try:
      ser = serial.Serial (v_port.get())
      ser.baudrate = v_speed.get()

      connected = True
      b_conn.config(text="DISCONNECT")
    except:
      v_cmd.set("Error opening port!")

b_conn = tk.Button(frp, text="CONNECT", width=8, command=connect)
b_conn.pack(side = tk.LEFT)

lbl_proto = tk.Label(frp, text="protocol:")
lbl_proto.pack(side = tk.LEFT)


def proto_selected(event):
  global proto

  tmp = c_proto.current()
  if tmp==0:
    proto = ptz.pelco.d
  elif tmp==1:
    proto = ptz.pelco.p

c_proto = ttk.Combobox(frp, width=6, values=['Pelco-D', 'Pelco-P'])
c_proto.current(0)
c_proto.pack(side = tk.LEFT)
c_proto.bind("<<ComboboxSelected>>", proto_selected)

v_addr = tk.StringVar()
e_addr = tk.Entry(frame, textvariable=v_addr, state='readonly', width=15)
e_addr.grid(column=3, row=2, columnspan=2)
v_addr.set("addr:{:03d} buf:{:03d}".format(addr, buf))


def motion(event):
  global mouse
  global x
  global y
  global ser
  global connected

  x_max = 130 #c.winfo_width()
  y_max = 130 #c.winfo_height()

  x_cur = event.x
  y_cur = event.y

  if mouse and x_cur < x_max and y_cur < y_max: 
    #print("Mouse position: (%s %s)" % (event.x, event.y))
    x = (x_cur - x_max / 2) * 256 / x_max 
    y = (y_cur - y_max / 2) * 256 / y_max 
    #x = x_cur
    #y = y_cur

    side0 = ""
    if x:
      side0 = 'left'
      if x > 0: 
        side0 = 'right'
    
    side1 = ""
    if y:
      side1 = 'up'
      if y > 0: 
        side1 = 'down'

    side = ' '.join([side0, side1]).strip()
    #print side

    cmd = proto.cmd_encode(addr,side,[abs(x),abs(y)])
    v_cmd.set(cmd.encode('hex'))
    if connected:
      ser.write(cmd)

    #v_cmd.set("x:{} y:{}".format(x,y))
    v_lbl.set("x:{} y:{}".format(x,y))

    tmp = float(y_cur)/(1.2*float(y_max))
    sby.set(tmp, 0.2+tmp)
    tmp = float(x_cur)/(1.2*float(x_max))
    sbx.set(tmp, 0.2+tmp)
  return

def mouse_down(event):
  global mouse
  mouse = True

def mouse_up(event):
  global mouse
  global x
  global y
  global addr
  global ser
  global connected
  mouse = False
  x = 0
  y = 0
  cmd = proto.cmd_encode(addr,'stop',[0,0])
  v_cmd.set(cmd.encode('hex'))
  if connected:
    ser.write(cmd)

  v_lbl.set("x:{} y:{}".format(x,y))
  sby.set(0.4,0.6)
  sbx.set(0.4,0.6)

frc = tk.Frame(frame, width=130, height=130)
frc.grid(column=5, row=1, rowspan=6)

sby = tk.Scrollbar(frc)  
sby.pack( side = tk.RIGHT, fill = tk.Y )
sby.set(0.4,0.6)

sbx = tk.Scrollbar(frc, orient = tk.HORIZONTAL)  
sbx.pack( side = tk.BOTTOM, fill = tk.X )
sbx.set(0.4,0.6)

c = tk.Canvas(frc, width=130, height=130, bg='black')
c.bind('<Motion>',motion)
c.bind('<ButtonPress-1>', mouse_down)
c.bind('<ButtonRelease-1>', mouse_up)
c.pack(side=tk.LEFT,expand=True,fill=tk.BOTH)

v_lbl = tk.StringVar()
lbl = tk.Label(frame, textvariable=v_lbl, bg='black', fg='white')
v_lbl.set("x:{} y:{}".format(x,y))
lbl.grid(column=5, row=2)


def onNumbersButton(num):
  global pos
  global buf

  if pos < 3:
    tmp = buf*10 + num
    if tmp < 256: 
      buf = tmp
    if tmp == 0:
      pos = 0

    pos = pos + 1

  else:
    pos = 0
    buf = 0

  v_addr.set("addr:{:03d} buf:{:03d}".format(addr, buf))

def onCamButton():
  global addr
  global buf

  addr = buf
  v_addr.set("addr:{:03d} buf:{:03d}".format(addr, buf))

b_cam = tk.Button(frame, text="OK", width=5, command=onCamButton)
b_cam.grid(column=1, row=5, columnspan=2)

b_0 = tk.Button(frame, text="0", command=lambda:onNumbersButton(0))
b_0.grid(column=0, row=5)


b_1 = tk.Button(frame, text="1", command=lambda:onNumbersButton(1))
b_1.grid(column=0, row=4)

b_2 = tk.Button(frame, text="2", command=lambda:onNumbersButton(2))
b_2.grid(column=1, row=4)

b_3 = tk.Button(frame, text="3", command=lambda:onNumbersButton(3))
b_3.grid(column=2, row=4)


b_4 = tk.Button(frame, text="4", command=lambda:onNumbersButton(4))
b_4.grid(column=0, row=3)

b_5 = tk.Button(frame, text="5", command=lambda:onNumbersButton(5))
b_5.grid(column=1, row=3)

b_6 = tk.Button(frame, text="6", command=lambda:onNumbersButton(6))
b_6.grid(column=2, row=3)

b_7 = tk.Button(frame, text="7", command=lambda:onNumbersButton(7))
b_7.grid(column=0, row=2)

b_8 = tk.Button(frame, text="8", command=lambda:onNumbersButton(8))
b_8.grid(column=1, row=2)

b_9 = tk.Button(frame, text="9", command=lambda:onNumbersButton(9))
b_9.grid(column=2, row=2)

b_close = tk.Button(frame, text="CLOSE", width=5, command=lambda:onCmdButton("close"))
b_close.grid(column=3, row=3)

b_open = tk.Button(frame, text="OPEN", width=5, command=lambda:onCmdButton("open"))
b_open.grid(column=4, row=3)

b_near = tk.Button(frame, text="NEAR", width=5, command=lambda:onCmdButton("near"))
b_near.grid(column=3, row=4)

b_far = tk.Button(frame, text="FAR", width=5, command=lambda:onCmdButton("far"))
b_far.grid(column=4, row=4)

def onCmdButton(txt):
  global addr
  global ser
  global connected
  cmd = proto.cmd_encode(addr,txt,[0,0])
  #print ("fuck")
  v_cmd.set(cmd.encode('hex'))
  if connected:
    ser.write(cmd)

b_wide = tk.Button(frame, text="WIDE", width=5, command=lambda:onCmdButton("wide"))
b_wide.grid(column=3, row=5)

b_tele = tk.Button(frame, text="TELE", width=5, command=lambda:onCmdButton("tele"))
b_tele.grid(column=4, row=5)

v_cmd = tk.StringVar()
e_cmd = tk.Entry(frame, textvariable=v_cmd, width=35)
e_cmd.grid(column=0, row=6, columnspan=5)
v_cmd.set("Hello!")


root.mainloop()