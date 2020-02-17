import keyboard
import os

select = 0
length = 0
user = ""
ip = ""
servers = []

class Server():
    def __init__(self, name, version, description):
        self.name = name
        self.version = version
        self.description = description

def connect():
    global user
    global ip
    data = []
    try:
        f = open("connectdata.sese", "r")
    except:
        input("Error 0: connectdata.sese does not exist. Click ENTER to exit: ")
        quit()
    data = [i.strip() for i in f]
    if data == []:
        input("Error 1: serverdata.sese is empty. Click ENTER to exit: ")
        quit()
    user = (data[0].split('='))[1].strip()
    ip = (data[1].split('='))[1].strip()
    f.close()

def listServers():
    global servers
    try:
        f = open("serverdata.sese", "r")
    except:
        input("Error 2: serverdata.sese does not exist. Click ENTER to exit: ")
        quit()
    data = [i.strip() for i in f]
    if data == []:
        input("Error 3: serverdata.sese is empty. Click ENTER to exit: ")
        quit()
    for x in data:
        s = x.split(';')
        servers.append(Server(s[0], s[1], s[2]))
    for s in servers:
        print((s.name, s.version, s.description))
    f.close()

def writeModifiedBatch(u, v, w):    #where u = username, v = ip and w = name (assuming path == name)
    f = open("Start Remote Server.bat", "w")
    f.write("ssh -t {0}@{1} \"cd ~/Desktop/Minecraft/{2} && ./run.sh\"".format(u, v, w))
    f.close()
            
def menu():
    os.system("cls")
    global select
    global servers
    for i in range(0, length):
        print("{0}:\t {1} \t\t{2}".format(i+1, servers[i].name, "<<<" if select == i else " "))

def up():
    global select
    if select == 0:
        select = length - 1
    else:
        select -= 1
    menu()

def down():
    global select
    if select == length - 1:
        select = 0
    else:
        select += 1
    menu()



def enter():
    global select
    global servers
    print("\n{0}: {1} selected to be written to batch file.".format(select+1, servers[select].name))
    writeModifiedBatch(user, ip, servers[select].name)
    print("\nWriting done. Please execute Start Remote Server.bat.")
    input(".\n.\n.\nPress ENTER to exit: ")
    quit()      #doesn't seem to work in cmd even though the rest do ¯\_(ツ)_/¯

def inf():
    global select
    global servers
    print("Server {0}:\n\nName\t\t=\t{1}\nVersion\t\t=\t{2}\nDescription\t=\t{3}\n".format(select + 1, servers[select].name, servers[select].version, servers[select].description))    
    print("Press W to return.")

listServers()
connect()
length = len(servers)
menu()

keyboard.add_hotkey('up', up)
keyboard.add_hotkey('down', down)
keyboard.add_hotkey('enter', enter)
keyboard.add_hotkey('q', inf)
keyboard.add_hotkey('w', menu)
keyboard.wait()

