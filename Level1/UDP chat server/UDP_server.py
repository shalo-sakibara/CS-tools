import socket


class Server:
    def __init__(self, host='127.0.0.1', port=22032):
        self.host = host
        self.port = port
        self.server_run = None
        self.server_socket = None
        self.users = []
        
        
    def runsrever(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind((self.host, self.port))
        self.server_run = True
        self.message_handler()
    
    def message_handler(self):
        while self.server_run:
            msg, addr = self.server_socket.recvfrom(1024)
            msg = f"{addr}: {msg.decode('utf-8')}".encode('utf-8')
            if addr not in self.users:
                self.users.append(addr)
            self.send_msg_users(msg=msg, exec_user=addr)
            
        self.close_server()        
    
    def send_msg_users(self, msg, exec_user=None):
        disconnected_users = []
        for addr_client in self.users:
            if addr_client != exec_user:
                try:
                    self.server_socket.sendto(msg, addr_client)
                except:
                    disconnected_users.append(addr_client)
        
        for client in disconnected_users:
            self.users.remove(client)
        
    
    def close_server(self):
        self.server_run = False
        self.server_socket.close()
        


if __name__ == '__main__':
    HOST, PORT = '127.0.0.1', 22032
    server = Server(HOST, PORT)
    server.runsrever()
    
            
        