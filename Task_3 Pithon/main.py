
class ListNode:
    def __init__(self, val, priority: int, next_node=None):
        self.__val = val
        self.__priority = priority
        self.__next = next_node

    @property
    def val(self):
        return self.__val

    @val.setter
    def val(self, val):
        self.__val = val

    @property
    def priority(self):
        return self.__priority

    @priority.setter
    def priority(self, priority):
        self.__priority = priority

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next_node):
        self.__next = next_node


class PriorityQueue:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count: int = 0

    @property
    def head(self):
        return self.__head

    @head.setter
    def head(self, node: ListNode):
        self.__head = node

    @property
    def tail(self):
        return self.__tail

    @tail.setter
    def tail(self, node: ListNode):
        self.__tail = node

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, count: int):
        self.__count = count

    def is_empty(self):
        return self.__count == 0

    def insert(self, val, priority: int):
        new_node = ListNode(val, priority)
        if self.head is None:
            self.head = self.tail = new_node
        elif self.tail.priority <= priority:
            self.tail.next = new_node
            self.tail = new_node
        elif self.head.val > priority:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next is not None and current.next.priority <= priority:
                current = current.next
            new_node.next = current.next
            current.next = new_node

        self.count += 1

    def peek(self):
        return self.head.val

    def extract_max(self) -> object:
        if self.is_empty():
            return None
        result = self.head.val
        self.head = self.head.next
        self.count -= 1
        return result

    def __iter__(self):
        self.__current = self.head
        return self

    def __next__(self) -> tuple[object, int]:
        if self.__current is None:
            raise StopIteration
        result = (self.__current.val, self.__current.priority)
        self.__current = self.__current.next
        return result

    def __str__(self):
        return " -> ".join(str(i) for i in self)


