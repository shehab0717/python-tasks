
class Queue :

    def __init__(self) -> None:
        self._list = list()
        
    def insert(self, item):
        self._list.append(item)

    def isEmpty(self):
        return len(self._list) == 0

    def pop(self):
        if self.isEmpty():
            raise Exception("Empty queue exception!!")
        value = self._list[0]
        del self._list[0]
        return value


    def __str__(self) -> str:
        return str(self._list)


# queue = Queue()

# queue.insert(1)
# queue.insert(2)
# queue.insert(3)
# queue.insert(4)
# queue.insert(5)


# while not queue.isEmpty():
#     print(queue.pop())

