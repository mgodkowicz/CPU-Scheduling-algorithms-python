

class Process:
    def __init__(self, p_name, b_t, a_t, p_p):
        self.name = p_name
        self.burst_time = b_t
        self.arrival_time = a_t
        self.priority = p_p

    def hi(self):
        print('Hi. My name is {}'.format(self.name))

    def burst(self):
        return int(self.burst_time)

    def arrival(self):
        return int(self.arrival_time)

    def get_name(self):
        return str(self.name)