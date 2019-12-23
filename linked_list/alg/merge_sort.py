# class Node:
#     def __init__(self,val):
#         self.val = val
#         self.next = None


def get_mid_node(head):
    """Find middle-1 node of linked list

    Args:
        head (Node): head of the linked list

    Returns:
        Node: middle-1 node of the linked list
    """
    if not head or not head.next:
        return head
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def split_half(head):
    """Split linked list in two halfs

    Args:
        head (Node): head node of the linked list

    Returns:
        (Node, Node): head of left and right linked lists
    """
    mid = get_mid_node(head)
    right = mid.next
    mid.next = None
    return head, right


def merge(first, second):
    if first and second:
        if first.val > second.val:
            first, second = second, first
        first.next = merge(first.next, second)
    return first or second


def merge_sort(head):
    if not head or not head.next:
        return head
    left, right = split_half(head)
    return merge(merge_sort(left), merge_sort(right))


# --- HELPER FUNCTIONS ---
def print_ll(node):
    """Print values of linked list

    Args:
        node (type): head of the linked list

    Returns:
        None
    """
    while node:
        print(node.val)
        node = node.next


def test_ll(s=10):
    """Generate a test linked list (s to 0)
    """
    ls = list(range(s, -1, -1))
    head = curr = Node(ls[0])
    for v in ls[1:]:
        curr.next = Node(v)
        curr = curr.next
    return head
