import socket

# Данные сервера
HOST, PORT = ('127.0.0.1', 22032)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

msg = input("Введите сообщение: ")
b_msg = bytes(msg, encoding='utf-8')

client.sendall(b_msg) #Отправка сообщения на сервер

server_echo_msg = str(client.recv(1024))
print(server_echo_msg.decode('utf-8'))