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
        """Get size of the list
        """
        return self.__size

    def print_list(self):
        """Print list vals
        """
        current = self.__head
        while current:
            print(current.val)
            current = current.next

    def reverse(self):
        """Reverse the list
        """
        if self.__size > 1:
            prev = None
            current = self.__head
            while current:
                temp = current.next
                current.next = prev
                prev = current
                current = temp
            self.__head = prev

    def at(self, index):
        """Get Node at the index strating from 0. If beyond len list return None

        Args:
            index (int): index of the desired Node.

        Returns:
            Node if index exists, None otherwise.
        """
        i = 0
        current = self.__head
        while(i < index and current):
            current = current.next
            i += 1
        return current

    def front(self):
        """Get head Node
        """
        return self.__head

    def pop_front(self):
        """Remove the last node of the list
        """
        if self.__head:
            if self.__head.next:
                self.__head = self.__head.next
            else:
                self.__head = None
            self.__size -= 1

    def push_front(self, val):
        """Insert a new head node

        Args:
            val (float): val to be inserted

        Returns:
            None
        """
        if not self.__head:
            self.__head = Node(val)
        else:
            new_head = Node(val)
            old_head = self.__head
            self.__head = new_head
            self.__head.next = old_head

    def back(self):
        """Get the last Node of the list
        """
        return self.at(self.__size - 1)

    def pop_back(self):
        """Remove the last node of the list
        """
        if self.__size > 1:
            # find a node one less than last one and set Node.next to None
            self.at(self.__size - 2).next = None
        else:
            self.__head = None
        self.__size = -1

    def push_back(self, val):
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
        self.__size += 1

    def insert(self, index, val):
        """Insert value at an index in the array

        Args:
            index (int): index to incert the val at
            val (float): val to be inserted

        Raises:
            ValueError: index out of range

        Returns:
            None
        """
        if index < 0 or self.__size < index:
            raise ValueError('Index outside the range')
        else:
            if index == 0:
                self.push_front(val)
            elif 0 < index < self.__size:
                prev = self.at(index - 1)
                post = prev.next
                prev.next = Node(val)
                prev.next.next = post
            else:
                self.push_back(val)
            self.__size += 1

    def delete(self, index):
        """Find node at index and del it

        Args:
            index (int): index of the node to be deleted

        Raises:
            ValueError: index out of range

        Returns:
            None
        """
        if index < 0 or self.__size <= index:
            raise ValueError('Index outside the range')
        else:
            if index == 0:
                self.pop_front()
            elif 0 < index < self.__size - 1:
                prev = self.at(index - 1)
                prev.next = prev.next.next
            else:
                self.pop_back()
            self.__size -= 1
