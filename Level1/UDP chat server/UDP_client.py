import socket
import threading

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def listen():
    while True:
        try:
            data, addr = client_socket.recvfrom(1024)
            print(f"{data.decode('utf-8')}")
        except:
            client_socket.sendto(''.encode('utf-8'), ('127.0.0.1', 22032))
            print("Вы подключены к серверу")
            pass


thread = threading.Thread(target=listen)
thread.daemon = True
thread.start()

print("Подключение к чату...")

while True:
    try:
        msg = input()
        client_socket.sendto(msg.encode('utf-8'), ('127.0.0.1', 22032))
    except KeyboardInterrupt:
        break
    except:
        break