from keyboard import *
from os import *

select = 1
length = 4

def menu():
    system("cls")
    global select
    for i in range(1, 5):
        print("{1} {0}. Do {0} {2}".format(i, ">" if select == i else " ", "<" if select == i else " "))

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

menu()
add_hotkey('up', up)
add_hotkey('down', down)
wait()

