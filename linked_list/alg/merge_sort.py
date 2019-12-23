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
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def two_halfs_ll(head):
    mid = split_half(head)
    right = mid.next
    mid.next = None
    return head, right

def merge(first,second):
    if first and second:
        if first.val>second.val:
            first,second = second,first
        first.next = merge(first.next,second)
    return first or second

# def merge_sort(head):
    # if not head or not head.next:
    #     return head
    # middle_node = split_half(head)#len(ls)//2
    # left = merge_sort(head)
    # right = merge_sort(middle_node)
    # return merge(left, right)

t_ll = test_ll(1)
print_ll(t_ll)
left, right = two_halfs_ll(t_ll)
print_ll(left)
print_ll(right)
