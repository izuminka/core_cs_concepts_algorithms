class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SinglyLinkedList:
    """Singly Linked List

    Attributes:
        head (class Node): head of the list

    """
    def __init__(self):
        self.head = None

    def push_back(self,val):
        """Push val at the end of the list

        Args:
            val (float): val to insert

        Returns:
            None

        """
        if not self.head:
            self.head = Node(val)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(val)

    def print_list(self):
        current = self.head
        while current:
            print(current.val)
            current = current.next

ll_test = SinglyLinkedList()
ll_test.push_back(1)
ll_test.push_back(2)
ll_test.push_back(3)
ll_test.print_list()
