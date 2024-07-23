import socket
import pickle
class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server = ""
        self.port = 5555
        self.addr = (self.server,self.port)
        self.playerId = self.connect(self.addr)

    def connect(self,addr):
        try :
            self.client.connect(self.addr)
            return self.client.recv(2048).decode() # PlayerId

        except:
            pass
    def send(self,data):
        try :
            self.client.send(str.encode(data))
            return pickle.loads(self.client.recv(2048 * 2))
        except socket.error as e:
             print(e)
