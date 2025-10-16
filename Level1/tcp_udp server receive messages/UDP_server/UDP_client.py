import socket

serverAddresPort = ('127.0.0.1', 22032)


client = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

while True:
    msg = input(">>")
    b_msg = msg.encode('utf-8')
    client.sendto(b_msg, serverAddresPort)
    
    data, addr = client.recvfrom(1024)
    server_msg = data.decode('utf-8')
    print(server_msg)
    if server_msg == 'UDP-сервер выключен':
        break
    