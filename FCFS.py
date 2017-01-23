from tqdm import tnrange, tqdm_notebook, tqdm
from time import sleep
from Process import Process
from Log import Log


class FCFS:
    def __init__(self, p_list):
        self.processes_list = []
        self.process_queue = p_list
        self.burst_queue = []
        self.amount = len(p_list)
        self.create_processes(self.process_queue)
        self.fill_queue()
        self.log = Log('FCFS')

    def create_processes(self, p):
        p.sort(key=lambda words: words[2])

        for x in p:
            self.processes_list.append(Process(x[0], x[1], x[2], x[3]))

    def fill_queue(self):
        for p in self.processes_list:
            self.burst_queue.append(p.burst())

        print ('ProcessName\tArrivalTime\tBurstTime')
        for x in self.processes_list:
            print (x.name, '\t\t', x.arrival_time, '\t\t', x.burst_time)
        sleep(1)

    def run(self):
        t = 0
        for x in range(self.amount):
            actual_pname = str(self.processes_list[x].name)
            self.log.start(actual_pname)
            for i2 in tqdm(range(self.burst_queue[x]), desc=actual_pname):
                # do something, e.g. sleep
                self.log.pending(actual_pname)
                sleep(1)
                t+=1
                for p in self.processes_list:
                    if int(p.arrival_time) == int(t) and str(p.name) != actual_pname:
                        tqdm.write('Process {} is waiting. Time: {}'.format(p.name, t))
                        self.log.waiting(p.name)






