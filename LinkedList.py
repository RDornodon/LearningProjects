class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, head=None, break_circular=True):
        self.head = head
        self.tail = head
        self.break_circular = break_circular

    def append(self, value, after_node=None):
        new_node = Node(value)

        # insert to the end
        if not after_node:
            if not self.head:
                self.head = new_node
            else:
                self.tail.next = new_node
            self.tail = new_node

        # insert to the beginning
        if after_node == self:
            if not self.head:
                self.head = new_node
                self.tail = new_node
            else:
                prev_first = self.head
                self.head = new_node
                new_node.next = prev_first

        # insert to after the first matching node
        else:
            if found_node := self.find(after_node):
                prev_next = found_node.next
                found_node.next = new_node
                new_node.next = prev_next
                if not prev_next:
                    self.tail = new_node

    def find(self, node) -> Node:
        if self.head:
            current = self.head
            while current is not None:
                if current == node or current.value == node:
                    return current
                current = current.next
        return None

    def __len__(self):
        if self.head == self.tail.next and not self.break_circular:
            raise Exception('Non-breaking circular list')
        return len([_ for _ in self])

    def __str__(self):
        nodes = [f'{node.value}' for node in self]
        return ' --> '.join(nodes)

    def __iter__(self):
        self.iter_node = self.head
        self.circular = False
        return self

    def __next__(self):
        if self.iter_node is None:
            raise StopIteration
        inode = self.iter_node
        self.iter_node = inode.next
        if self.iter_node == self.head and self.break_circular:
            self.iter_node = Node('...')
        return inode

# new list
ll = LinkedList()

# append 3 items & print
ll.append(3)
ll.append(2)
ll.append(1)
print(ll)

# prepend on item & print
ll.append(4, ll)
print(ll)

# insert one item & print
ll.append(3.5, 3)
print(ll)
print(len(ll))

# make list circular & print
ll.tail.next = ll.head
print(ll)
print(len(ll))

# make non-breaking
ll.break_circular = False
print(len(ll))
