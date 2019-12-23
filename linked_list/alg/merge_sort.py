class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

def print_ll(node):
    while node:
        print(node.val)
        node = node.next

def test_ll():
    ls = list(range(9,-1,-1))
    head = curr = Node(ls[0])
    for v in ls[1:]:
        curr.next = Node(v)
        curr = curr.next
    return head



t_ll = test_ll()
print_ll(t_ll)
#
# t = Node(0)
# t.next = Node(1)
# t.next.next = Node(3)
# t.next.next.next = Node(4)
