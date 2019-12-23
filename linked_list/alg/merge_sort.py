class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

def print_ll(node):
    while node:
        print(node.val)
        node = node.next

def test_ll(s):
    ls = list(range(s,-1,-1))
    head = curr = Node(ls[0])
    for v in ls[1:]:
        curr.next = Node(v)
        curr = curr.next
    return head

def split_half(head):
    if not head or not head.next:
        return head
    slow = head.next
    fast = head.next
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow

# def merge_sort(head):
    # if not head or not head.next:
    #     return head
    # middle_node = split_half(head)#len(ls)//2
    # left = merge_sort(head)
    # right = merge_sort(middle_node)
    # return merge(left, right)

t_ll = test_ll(1)
print_ll(t_ll)
split_half(t_ll).val


# t = Node(0)
# t.next = Node(1)
# t.next.next = Node(3)
# t.next.next.next = Node(4)
