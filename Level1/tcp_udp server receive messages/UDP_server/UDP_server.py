import socket

HOST, PORT = ('127.0.0.1', 22032)

socket_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

socket_server.bind((HOST, PORT))


print(f"UDP-сервер запущен на {HOST}:{PORT}. Ожидание подключения...")

while True:
        # Получаем датаграмму и адрес отправителя
        data, addr = socket_server.recvfrom(1024) # [ Данные ] + [ Адрес отправителя ]
        # Декодируем байты в строку
        message = data.decode('utf-8')
        print(f"Получено сообщение от {addr}: {message}")
        if message == 'close':
            socket_server.sendto('UDP-сервер выключен'.encode('utf-8'), addr)
            break

        socket_server.sendto(f"UDP-ответ на: {message}".encode('utf-8'), addr)
        
        