import socket
import threading
 
class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.users = []
        self.server_socket = None
        self.nicknames = {}
        self.server_run = False
    
    def runserver(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.server_run = True
        self.server_socket.listen()
        print(f"[!] Server запущен")
        print("[!] Ожидание подключений...")
        
        accept_thread = threading.Thread(target=self.accept_users)
        accept_thread.daemon = True
        accept_thread.start()
        
        while self.server_run:
            pass
        
        
    def accept_users(self):
        while self.server_run:
            client, addr = self.server_socket.accept()
            print(f"Подключение от {addr[0]}:{addr[1]}")
            client.send("Напиши свой никнейм:".encode('utf-8'))
            client_thread = threading.Thread(
                    target=self.message_handler, 
                    args=(client, addr)
                )
            client_thread.daemon = True
            client_thread.start()
	
            
    
    
    def message_handler(self, client, addr):
        try:
            nickname_user = client.recv(1024).decode('utf-8')
            self.nicknames[client] = nickname_user
            self.users.append(client)
            print(f"{nickname_user} ({addr[0]}) присоединился к чату")
            while self.server_run:
                msg = client.recv(1024).decode('utf-8')  
                if msg == "/выход":
                    break
                else:
                    self.send_msg_users(nickname_user, msg, client)  
        finally:
            client.send("[!]Отключаю вас".encode('utf-8'))
            client.close()
            self.users.remove(client)
            del self.nicknames[client]
            if self.server_run:
                self.send_msg_users(msg=f"[!]{nickname_user} покинул чат", exec_client=client)
        
        
    def stopserver(self):
        for client in self.users:
            try:
                client.close()
            except:
                pass
        self.server_run = False
        self.server_socket.close()
        
    
    
    
    def send_msg_users(self, name='Server )', msg="", exec_client=None):
        for client in self.users:
            if client != exec_client:
                client.send(f"{name}: {msg}".encode('utf-8'))
        

if __name__ == '__main__':
    HOST, PORT = '127.0.0.1', 5555
    server_chat = Server(HOST, PORT)
    server_chat.runserver()      