class Node:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data

    def __str__(self):
        return str(self.data)


class MyList:
    def __init__(self, lst=None):
        self.head = None
        self.tail = None
        if lst is not None:
            for i in lst:
                self.add(i)

    def add(self, value):
        obj = Node(value)
        current_tail = self.tail
        self.tail = obj
        if self.head is None:
            self.head = obj
            return
        obj.prev = current_tail
        current_tail.next = obj

    def __len__(self):
        count = 0
        obj = self.head
        while obj is not None:
            count += 1
            obj = obj.next
        return count

    def __str__(self):
        current = self.head
        lst = []
        while current is not None:
            lst.append(str(current.data))
            current = current.next
        return " ".join(lst)

    def __getitem__(self, item):
        if type(item) != int:
            raise IndexError('неверный индекс')
        if item < 0:
            raise IndexError('неверный индекс')
        start = 0
        obj = self.head
        while start < item:
            if obj is None:
                raise IndexError('неверный индекс')
            obj = obj.next
            start += 1
        if obj is None:
            raise IndexError('неверный индекс')
        return obj

    def reverse(self):
        current = self.head
        while current is not None:
            current.next, current.prev = current.prev, current.next
            current = current.prev
        self.head, self.tail = self.tail, self.head

    def sort(self, reverse=False):
        len_list = len(self)
        for i in range(len_list):
            current = self[0]
            j = 0
            next_obj = current.next
            if next_obj is None:
                self.tail = current
            while next_obj is not None and j < len_list - 1 - i:
                j+=1
                if current.data > next_obj.data:
                    if current == self.head:
                        self.head = next_obj
                    if next_obj == self.tail:
                        self.tail = current
                    if current.prev is not None:
                        current.prev.next = next_obj
                    if next_obj.next is not None:
                        next_obj.next.prev = current
                    current.prev, current.next, next_obj.prev, next_obj.next = next_obj, next_obj.next, current.prev, current
                else:
                    current = next_obj

                next_obj = current.next
        if reverse:
            self.reverse()


def ex():
    lst = MyList([1, 2, 6, 2, 9, 3, 5, 1])
    print(lst)
    lst.reverse()
    print(lst)
    lst.sort()
    print(lst)

if __name__ == '__main__':
    ex()