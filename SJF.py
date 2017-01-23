from tqdm import tnrange, tqdm_notebook, tqdm
from time import sleep
from Process import Process


class SJF:
    def __init__(self, p_list):
        self.processes_list = []
        self.process_queue = p_list
        self.burst_queue = []
        self.amount = len(p_list)
        self.create_processes(self.process_queue)
        self.fill_queue()

    def create_processes(self, p):
        queue2 = []
        p.sort(key=lambda words: words[2])
       # p.sort(key=lambda words: int(words[1]) | int(words[2]))

        for x in p:
            self.processes_list.append(Process(x[0], x[1], x[2], x[3]))

        print(len(self.processes_list))
        queue2.append(self.processes_list[0])
        for i in range(1, len(self.processes_list)):
            temp = []
            for j in range(1, len(self.processes_list)):
                if self.processes_list[j].arrival_time <= (queue2[i - 1].burst_time + queue2[i - 1].arrival_time):
                    temp.append(self.processes_list[j])
            temp.sort(key=lambda p_queue: p_queue.burst_time)
            print(temp)
            queue2.append(temp[i - 1])

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
            for i2 in tqdm(range(self.burst_queue[x]), desc=actual_pname):
                # do something, e.g. sleep
                sleep(1)
                t+=1
                for p in self.processes_list:
                    if int(p.arrival_time) == int(t) and str(p.name) != actual_pname:
                        tqdm.write('Process {} is waiting. Time: {}'.format(p.name, t))




    # queue2 = []
    # process_queue.sort(key=lambda p_queue: p_queue.arrival)
    # queue2.append(process_queue[0])
    # for i in range(1,len(process_queue)):
    #     temp = []
    #     for j in range(1, len(process_queue)):
    #         if process_queue[j].arrival <= (queue2[i-1].burst+queue2[i-1].arrival):
    #             temp.append(process_queue[j])
    #     temp.sort(key=lambda p_queue: p_queue.burst)
    #     queue2.append(temp[i-1])
