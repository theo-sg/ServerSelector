import keyboard
import os

select = 1
length = 4
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
    f = open("connectdata.sese", "r")               #reads connect config file
    data = [i.strip() for i in f]
    user = (data[0].split('='))[1].strip()          #and assigns the variables
    ip = (data[1].split('='))[1].strip()
    f.close()

def listServers():
    global servers
    f = open("serverdata.sese", "r")
    # add functionality here
    f.close()

def writeModifiedBatch(u, v, w):    #where u = username, v = ip and w = name (assuming path == name)
    f = open("Start Remote Server.bat", "w")
    f.write("ssh -t {0}@{1} \"cd ~/Desktop/Minecraft/{2} && ./run.sh\"".format(u, v, w))
    f.close()
    
		

def menu():
    os.system("cls")
    global select
    for i in range(1, 5):
        print("{0}. {1} \t\t{2}".format(i, "option", "<<<" if select == i else " "))

def up():
    global select
    if select == 1:
        select = length
    else:
        select -= 1
    menu()

def down():
    global select
    if select == 4:
        select = 1
    else:
        select += 1
    menu()

def enter():
    global select
    print("{0} selected".format(select))

menu()
connect()
writeModifiedBatch(user, ip, "TestServer")
keyboard.add_hotkey('up', up)
keyboard.add_hotkey('down', down)
keyboard.add_hotkey('enter', enter)
keyboard.wait()

