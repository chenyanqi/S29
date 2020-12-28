import socket
sock = socket.socket()
ip_port=("127.0.0.1",8899)
sock.connect(ip_port)

while 1:
    data = input("客户端的请求>>>>:")
    sock.send(data.encode())
    res=sock.recv(1024)

    print("服务器响应:%s " % res.decode())