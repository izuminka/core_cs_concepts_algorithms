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
        self.size = 0


    def print_list(self):
        current = self.head
        while current:
            print(current.val)
            current = current.next

    def at(self,index):
        """get Node at the index strating from 0. If beyond len list return None

        Args:
            index (int): index of the desired Node.

        Returns:
            Node if index exists, None otherwise.

        """
        i = 0
        current = self.head
        while(i<index and current):
            current = current.next
            i+=1
        return current

    def back(self):
        """Get last node of the list

        Returns:
            Node: last node

        """
        current = self.head
        while current.next:
            current = current.next
        return current

    def pop_back(self):
        """Remove the last node of the list
        """
        if self.size>1:
            #find a node one less than last one and set next to not
            self.at(self.size-2).next = None
        else:
            self.head = None
        self.size=-1

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
            self.back().next = Node(val)
        self.size+=1

# ll_test = SinglyLinkedList()
# ll_test.push_back(0)
# ll_test.push_back(1)
# ll_test.push_back(2)
# ll_test.print_list()
#
# ll_test.size
# ll_test.pop_back()
# ll_test.back().val
# ll_test.at(5)
