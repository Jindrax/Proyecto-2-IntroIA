import math
class PQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0

    # for inserting an element in the queue
    def insert(self, data):
        self.queue.append(data)

    # for popping an element based on Priority
    def delete(self):
        try:
            minVal = math.inf
            minIndex = 0
            for i in range(len(self.queue)):
                if self.queue[i][0] < minVal:
                    minVal = self.queue[i][0]
                    minIndex = i
            return self.queue.pop(minIndex)
        except IndexError:
            None