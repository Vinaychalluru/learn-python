import random
import traceback


class Node:
    """A Node"""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """A LinkedList"""

    def __init__(self):
        self.head = None

    def printList(self):
        temp_node = self.head
        while temp_node:
            print(temp_node.data)
            temp_node = temp_node.next


if __name__ == '__main__':
    try:
        ll = LinkedList()
        n1, n2, n3 = Node(1), Node(2), Node(3)
        ll.head = n1
        n1.next = n2
        n2.next = n3
        ll.printList()

    except Exception as e:
        pass
