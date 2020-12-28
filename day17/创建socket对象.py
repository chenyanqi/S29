import socket
sock = socket.socket()
ip_port = ("127.0.0.1",8899)
sock.bind(ip_port)

sock.listen(5)

print("server is waiting....")
while 1:
    client_sock,addr = sock.accept()

    print("来自客户端%s的请求" % str(addr))

    while 1:
        try:
            data = client_sock.recv(1024)
            print("data:",data.decode())
            res = input("服务端的响应：》》》")
            client_sock.send(res.encode())
        except ConnectionResetError:
            print("客户端退出，服务端退出")
            break
