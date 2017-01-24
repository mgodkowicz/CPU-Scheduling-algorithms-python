from tqdm import tnrange, tqdm_notebook, tqdm
from time import sleep
from Process import Process
from Log import Log


class Priority():
    def __init__(self, p_list):
        self.processes_list = []
        self.process_queue = p_list
        self.burst_queue = []
        self.amount = len(p_list)
        self.create_processes(self.process_queue)
        self.fill_queue()
        self.log = Log('Priority')
        self.average_wait_time = 0

    def create_processes(self, p):
        p.sort(key=lambda words: words[2])

        for x in p:
            self.processes_list.append(Process(x[0], x[1], x[2], x[3]))

        self.sort_processes()

    def sort_processes(self):
        queue2 = []
        queue2.append(self.processes_list[0])

        for i in range(1, len(self.processes_list)):
            temp = []
            for j in range(1, len(self.processes_list)):
                if self.processes_list[j].arrival_time <= (queue2[i-1].burst_time + queue2[i-1].arrival_time):

                    temp.append(self.processes_list[j])

            temp.sort(key=lambda p_queue: p_queue.priority)
            for x in temp:
                if not x in queue2:
                    queue2.append(x)

        self.processes_list = queue2

    def fill_queue(self):
        for p in self.processes_list:
            self.burst_queue.append(p.burst())

        self.print_data()

    def print_data(self):
        print('ProcessName\tArrivalTime\tBurstTime\tPriority')
        for x in self.processes_list:
            print(x.name, '\t\t\t\t', x.arrival_time, '\t\t', x.burst_time, '\t\t\t', x.priority)
        sleep(1)

    def run(self):
        t = 0
        self.calculate(True)
        sleep(1)

        for x in range(self.amount):
            #self.print_data()
            self.calculate(False)
            self.aging(t)
           # self.print_data()
            actual_pname = str(self.processes_list[x].name)
            self.log.start(actual_pname, t - int(self.processes_list[x].arrival_time))
            for i2 in tqdm(range(self.burst_queue[x]), desc=actual_pname):
                self.log.pending(actual_pname)
                sleep(1)
                t += 1
                for p in self.processes_list:
                    if int(p.arrival_time) == int(t) and str(p.name) != actual_pname:
                        tqdm.write('Process {} is waiting. Time: {}'.format(p.name, t))
                        self.log.waiting(p.name)
        self.log.final(self.average_wait_time, self.amount)

    def calculate(self, write):
        start_time = 0
        average_wait = 0
        m = len(self.processes_list)
        for p in self.processes_list:
            if int(p.arrival_time) > start_time:
                start_time = p.arrival_time
                p.w_time = 0
            else:
                p.w_time = start_time - int(p.arrival_time)
            average_wait += p.w_time
            p.e_time = int(start_time) + int(p.burst_time)
            start_time += int(p.burst_time)

        if write:
            self.average_wait_time = average_wait

            print("\nTotal wait time= ", average_wait)
            print("Average process wait time: ", float(average_wait / m))

    def aging(self, t):
        queue2 = []
        for p in self.processes_list:
            if t - int(p.arrival_time) >= 10:
                p.priority = 1

        queue2.append(self.processes_list[0])
        for i in range(1, len(self.processes_list)):
            temp = []
            for j in range(1, len(self.processes_list)):
                if self.processes_list[j].arrival_time <= (queue2[i - 1].burst_time + queue2[i - 1].arrival_time):
                    temp.append(self.processes_list[j])

            temp.sort(key=lambda temp: int(temp.priority))#, reverse=True)
            for x in temp:
                if not x in queue2:
                    queue2.append(x)
        # for x in queue2:
        #     print(x.name + str(x.priority))
        self.processes_list = queue2
