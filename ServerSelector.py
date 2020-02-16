from keyboard import *
from os import *

select = 1
length = 4

def menu():
    system("cls")
    global select
    for i in range(1, 5):
        print("{0}. {1} \t{2}".format(i, "option", "<<" if select == i else " "))

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
add_hotkey('up', up)
add_hotkey('down', down)
add_hotkey('enter', enter)
wait()

