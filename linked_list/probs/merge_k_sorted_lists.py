# class Node(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def merge(first, second):
    """Merge 2 sorted linked lists

    Args:
        first (Node): head of first sorted linked list
        second (Node): head of second sorted linked list

    Returns:
        Node: head of the merged sorted linked list
    """
    if first and second:
        if first.val > second.val:
            first, second = second, first
        first.next = merge(first.next, second)
    return first or second

def merge_k_lists(lists):
    """Merge K sorted linked lists

    Args:
        lists (list of Nodes): list of sorted linked lists

    Returns:
        Node: head of the merged sorted linked list
    """
    if not lists:
        return
    if len(lists) == 1:
        return lists[0]
    mid = len(lists)//2
    l = mergeK(lists[:mid])
    r = mergeK(lists[mid:])
    return merge(l, r)
