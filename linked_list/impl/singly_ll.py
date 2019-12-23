class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SinglyLinkedList:
    """Singly Linked List

    Attributes:
        __head (class Node or None): head of the list
        __size (int): size of the list

    """
    def __init__(self):
        self.__head = None
        self.__size = 0

    def size(self):
        return self.__size

    def print_list(self):
        current = self.__head
        while current:
            print(current.val)
            current = current.next

    def at(self,index):
        """Get Node at the index strating from 0. If beyond len list return None

        Args:
            index (int): index of the desired Node.

        Returns:
            Node if index exists, None otherwise.

        """
        i = 0
        current = self.__head
        while(i<index and current):
            current = current.next
            i+=1
        return current


    def front(self):
        return self.__head

    def pop_front(self):
        """Remove the last node of the list
        """
        if self.__head:
            if self.__head.next:
                self.__head = self.__head.next
            else:
                self.__head = None
            self.__size-=1

    def push_front(self,val):
        """Insert a new head node

        Args:
            val (float): val to be inserted

        Returns:
            None
        """
        if not self.__head:
            self.__head = Node(val)
        else:
            new___head = Node(val)
            old___head = self.__head
            self.__head = new___head
            self.__head.next = old___head


    # dep on at()
    def back(self):
        """Get the last Node of the list
        """
        return self.at(self.__size-1)

    #dep on at()
    def pop_back(self):
        """Remove the last node of the list
        """
        if self.__size>1:
            #find a node one less than last one and set Node.next to None
            self.at(self.__size-2).next = None
        else:
            self.__head = None
        self.__size=-1

    #dep on back()
    def push_back(self,val):
        """Push val at the end of the list

        Args:
            val (float): val to insert

        Returns:
            None
        """
        if not self.__head:
            self.__head = Node(val)
        else:
            self.back().next = Node(val)
        self.__size+=1


    # dep on at(), push_back(), push_front()
    def insert(self,index,val):
        """Insert value at an index in the array

        Args:
            index (int): index to incert the val at
            val (float): val to be inserted

        Raises:
            ValueError: index out of range

        Returns:
            None
        """
        if index < 0 or self.__size<index:
            raise ValueError('Index outside the range')
        else:
            if index == 0:
                self.push_front(val)
            elif 0 < index < self.__size:
                prev = self.at(index-1)
                post = prev.next
                prev.next = Node(val)
                prev.next.next = post
            else:
                self.push_back(val)
            self.__size+=1

    #dep at(), pop_front(), pop_back()
    def delete(self,index):
        """Find node at index and del it

        Args:
            index (int): index of the node to be deleted

        Raises:
            ValueError: index out of range

        Returns:
            None
        """
        if index < 0 or self.__size<=index:
            raise ValueError('Index outside the range')
        else:
            if index == 0:
                self.pop_front()
            elif 0 < index < self.__size-1:
                prev = self.at(index-1)
                prev.next = prev.next.next
            else:
                self.pop_back()
            self.__size-=1




# ll_test = SinglyLinkedList()
# # ll_test.push_back(0)
# # ll_test.pop_front()
# # ll_test.push_back(0)
# # ll_test.print_list()
#
# ll_test.push_back(0)
# ll_test.push_back(1)
# ll_test.push_back(2)
#
# ll_test.delete(1)
# ll_test.print_list()
#
# ll_test.insert(3,100)
# ll_test.insert(0,111)
# ll_test.insert(0,21111)
# ll_test.print_list()
# # ll_test.__size
# # ll_test.pop_back()
# ll_test.back().val
# # ll_test.at(5)
