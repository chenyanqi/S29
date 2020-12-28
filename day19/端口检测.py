from telnetlib import Telnet
import time
#import telnetlib

# import telnetlib
#
# HOST = "<put host name here>"
# # PORT = < put
# port
# here >
# t = telnetlib.Telnet('http://voice.b2m.cn',80,1)
# print(t)

# import telnetlib

# HOST = "voice.b2m.cn"
# PORT = 80
#
# t = telnetlib.Telnet()
# print(t.open(HOST,PORT))
n = 0

while 1:
    now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    tn = Telnet('voice.b2m.cn',80,3)
    tn.write(b'guido\r\n')
    # s = str.encode(tn.read_all())
    print(f"第{n}次telnet", tn)
    n += 1
    # # tn = Telnet('voice.b2m.cn', 80)
    # with open('d:/telnet.log',encoding='utf-8',mode='a+') as f:
    #     f.write(f"{now_time} 第{n}次telnet {tn}\n" )
    time.sleep(5)