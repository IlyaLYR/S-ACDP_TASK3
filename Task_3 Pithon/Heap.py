class PriorityQueueMax:
    def __init__(self):
        self.__heap__ =[]

def parent(index: int) -> int:
        return (index - 1) / 2

print(parent(4) )