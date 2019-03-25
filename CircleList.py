class CList :
    class Node :
        def __init__(self, next, item):
            self.next = next
            self.item = item

    def __init__(self):
        self.last = None
        self.size = 0

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def insert(self, item):
        node = self.Node(None, item)
        if self.is_empty():
            node.next = node
            self.last = node
        else:
            temp = self.node(self.size-1)
            node.next = self.last
            temp.next = node
        self.size += 1

    def first(self):
        if self.is_empty():
            raise EmptyError('Underflow')
        node = self.last
        return node

    def delete_first(self):
        node = self.last
        self.last = node.next
        self.size -= 1

    def print_list(self):
        node = self.last
        for  k in range(self.size):
            print(node.item,' -> ', end='')
            node = node.next

    def node(self, index):
        node = self.last
        for k in range(index):
            node = node.next
        return node

if __name__ == "__main__":
    c = CList()
    c.insert('apple')
    c.insert('banana')
    c.insert('kiwi')
    c.insert('pineapple')
    c.print_list()