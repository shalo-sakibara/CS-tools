import socket

# Конфигурации сервера
HOST = '127.0.0.1'
PORT = 22032


socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket_server.bind((HOST, PORT)) #Привязываем сокет к адресу и порту

socket_server.listen(1) #Прослушаваю сокет
print(f"TCP-сервер запущен на {HOST}:{PORT}. Ожидание подключения...")

mess, addr = socket_server.accept()

while mess:
    print(f"Подключен клиент с адресом: {addr}")
    while True:
            # Получаем данные от клиента (максимум 1024 байта)
            data = mess.recv(1024)
            if not data:
                # Если данных нет, клиент закрыл соединение
                break
            # Декодируем байты в строку и выводим
            message = data.decode('utf-8')
            print(f"Получено от {addr}: {message}")

            # Отправляем эхо-ответ
            mess.sendall(f"Эхо: {message}".encode('utf-8'))

    print("Соединение с клиентом закрыто.")
    break