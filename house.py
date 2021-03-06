import random

random.seed()

class device:
    def __init__(self, pOn, avgTime, n, watts):
        self.pOn = pOn
        self.avgTime = avgTime
        self.watts = watts
        self.states = [False for i in range(n)]
        self.timeState = [0 for i in range(n)]
        self.timeOn = [0 for i in range(n)]

    def update(self, seconds):
        self.timeState = [x + seconds for x in self.timeState]

        for i in range(len(self.states)):
            # When on, wait until timeOn[i] has passed
            if(self.states[i]):
                if(self.timeState[i] >= self.timeOn[i]):
                    self.timeState[i] = 0
                    self.states[i] = False
            else:
                p = random.random()
                if(p < self.pOn * seconds):
                    self.timeState[i] = 0
                    self.states[i] = True
                    self.timeOn[i] = random.normalvariate(self.avgTime, self.avgTime / 5.0)

    def deviceWatts(index):
        return max(self.watts * random.normalvariate(1, 0.1), 0) if self.states[index] else 0

    def totalWatts(self):
        total = 0
        for state in self.states:
            total += max(self.watts * random.normalvariate(1, 0.1), 0) if state else 0

        return total

class house:
    def __init__(self, devices):
        self.devices = devices

    def update(self, seconds):
        for device in self.devices:
            device.update(seconds)

    def watts(self):
        total = 0
        for device in self.devices:
            total += device.totalWatts()

        return total
