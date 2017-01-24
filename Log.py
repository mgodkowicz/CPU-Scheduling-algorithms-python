from time import gmtime, strftime


class Log:
    def __init__(self, algorithm):
        self.fileName = algorithm+'Log.txt'
        logFile = open(self.fileName, 'w').close()

    def start(self, id, t):
        time = strftime("%H:%M:%S", gmtime())
        str = time + '  {} started after waiting for {} seconds'.format(id, t)
        self.save(str)

    def pending(self, id):
        time = strftime("%H:%M:%S", gmtime())
        str = time + '  {} is running'.format(id)
        self.save(str)

    def waiting(self, id):
        time = strftime("%H:%M:%S", gmtime())
        str = time + '  {} is waiting'.format(id)
        self.save(str)

    def save(self, msg):
        logFile = open(self.fileName, 'a')
        logFile.write(msg)
        logFile.write('\n')

        logFile.close()

    def final(self, time, a):
        str = "Total wait time: {}".format(time)
        str2 = "Average process wait time: {}".format(time/a)
        self.save(str)
        self.save(str2)

