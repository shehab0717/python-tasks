from queue import Queue


from Queue import Queue
from Exceptions import QueueOutOfRangeException


class NamedQueue(Queue):
    def __init__(self, name, limit):
        self.name=name
        self.limit=limit
        super().__init__()
    
    def size(self):
        return len(self._list)

    def insert(self, item):
        if self.size() == self.limit:
            raise QueueOutOfRangeException()
        super().insert(item)


queue = NamedQueue(name="My queue", limit=4)

queue.insert(1)
queue.insert(2)
queue.insert(3)
queue.insert(4)
# queue.insert(5) #OutOfRangeException


while not queue.isEmpty():
    print(queue.pop())