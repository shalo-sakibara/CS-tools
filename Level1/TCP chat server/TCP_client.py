import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                print("Соединение с сервером разорвано")
                break
            print(message)
        except:
            print("Отключен от сервера")
            break

def start_client():
    host = 'localhost'
    port = 5555
    
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        
       
        welcome = client_socket.recv(1024).decode('utf-8')
        print(welcome, end='')
        
        nickname = input().strip()
        client_socket.send(nickname.encode('utf-8'))
        
        receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
        receive_thread.daemon = True
        receive_thread.start()
        
        print("Вы добавлены в чат!")        
        
        while True:
            message = input()
            if message.lower() == '/выход':
                client_socket.send(message.encode('utf-8'))
                msg = client_socket.recv(1024).decode('utf-8')
                if msg == "[!]Отключаю вас":
                    break
            client_socket.send(message.encode('utf-8'))
    
    finally:
        client_socket.close()
        print("До свидания!")
        exit()

if __name__ == "__main__":
    start_client()