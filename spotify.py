import socket, datetime, random, argparse, time


MAX_BYTES = 65536
class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
    
    def launch(self):
        server_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_s.bind((self.host, self.port))
        print(f"Server launched on {self.host}:{self.port}")
        while True:
            data, addr = server_s.recvfrom(MAX_BYTES)
            if random.random() < 0.7:
                print(f"Dropped packet from {addr}")
                continue
            text = data.decode("utf-8")
            print(f"Client {addr} said: {text}")
            respond = f"I recieved your message Client: {addr}".encode("utf-8")
            server_s.sendto(respond, addr)
            print(f"Respond sent to {addr}")

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        
    def launch(self):
        client_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        msg = f"This is a message to server {self.host}:{self.port}. It is {datetime.datetime.now()} here".encode("utf-8")
        client_s.connect((self.host, self.port))
        delay = 0.1
        hour = datetime.datetime.now().hour
        interval=0
        if hour<12: interval = 3
        elif hour >= 12 and hour < 17: interval = 1
        elif hour >= 17 and hour <= 23: interval = 2        
        while True:
        	client_s.send(msg)
        	print("Waiting for %.1f seconds for a reply" % delay)
        	client_s.settimeout(delay)        
        	try:
        		respond = client_s.recv(MAX_BYTES).decode("utf-8")
        	except socket.timeout:
        		if interval == 1 or interval == 3:
        			delay *= 2
        		elif interval == 2:
        			delay *= 3        
        		if (interval == 1 and delay > 2) or (interval == 2 and delay > 4) or (interval == 3 and delay > 1):
        			raise RuntimeError("Server not responded")
        	else: 
        		break        
        print(f"Recieved '{respond}' message from {self.host}:{self.port}")
            
            
def main():
    parser = argparse.ArgumentParser("UDP connection with Spotify server test")
    choices = {"client": Client, "server": Server}
    parser.add_argument("role", choices=choices, help = "Select user or server interface")
    parser.add_argument("host", help="Interface of sever to launch on")
    parser.add_argument("-p", metavar="PORT", type = int, default=65432)

    args = parser.parse_args()
    cl = choices[args.role]
    obj = cl(args.host, args.p)
    obj.launch()


if __name__ == "__main__":
    main()
