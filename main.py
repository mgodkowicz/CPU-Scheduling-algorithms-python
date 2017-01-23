from Process import Process
from FCFS import FCFS
from SJF import SJF

words = []
processes = list()
processesSJF = list()

with open('process', 'r') as file:
    for line in file:
        words.append(line.split())


# fcfs = FCFS(words)
#
# fcfs.run()

# # print("SJF")
sjf = SJF(words)
#
sjf.run()


