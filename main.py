#!/usr/bin/python
from Process import Process
from FCFS import FCFS
from SJF import SJF
from Priority import Priority

words = []
processes = list()
processesSJF = list()

with open('process', 'r') as file:
    for line in file:
        words.append(line.split())

def menu():
    print("\nWhat algorithm you want to launch?")
    print('1. FCFS')
    print('2. SJF')
    print('3. Priority')
    print('4. End')
    z = int(input('(1-4):'))
    if z == 1:
        fcfs = FCFS(words)
        fcfs.run()
    elif z == 2:
        sjf = SJF(words)
        sjf.run()
    elif z == 3:
        pr = Priority(words)
        pr.run()
    elif z == 4:
        pass
    else:
        print("Wrong input")
        menu()

while(True):
    menu()

