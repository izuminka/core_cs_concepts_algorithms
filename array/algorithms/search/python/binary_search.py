def binary_search(ls,v, isFirstCheck=False, isLastCheck=False):
    """Iterative implementation of a binary search. If the searched desired number
     repeats, can return the first, last or first found occurance. If no bools
     are initiated, returns the first found occurance.

    Args:
        ls (type): list of sorted nums
        v (type): num we are searching for
        isFirstCheck (type): if ind of first occurance of v is needed
        isLastCheck (type): if ind of last occurance of v is needed

    Returns:
        int: ind of v of the desired occurance.

    """
    l = 0
    last_ind = len(ls)-1
    r = last_ind
    if isFirstCheck: # if the first occurance of v is needed
        while(l<=r):
            m = round(l +(r-l)/2)
            # check if v is at ind m and any value less than ind m is less than v
            # insure that the boundary case is included where m===0
            if ls[m] == v and (m == 0 or ls[m-1] < v):
                return m
            if ls[m] < v:
                l = m+1
            else:
                r = m-1
        return -1

    elif isLastCheck: # if the last occurance of v is needed
        while(l<=r):
            m = round(l +(r-l)/2)
            # check if v is at ind m and any value more than ind m is more than v
            # insure that the boundary case is included where m===last_ind
            if ls[m] == v and (m == last_ind or v < ls[m+1]):
                return m
            if v < ls[m]:
                r = m-1
            else:
                l = m+1
        return -1

    else: # if the first found occurance of v
        while(l<=r):
            m = round(l +(r-l)/2)
            if ls[m] == v:
                return m
            if v < ls[m]:
                r = m-1
            else:
                l = m+1
        return -1



ls = [1,4,4,4,5,8,8,19,29,40]
ls = [4,4]
test_cases = [4]

# tests1 = [binary_search(ls,v,isFirstCheck=True) for v in test_cases]
tests2 = [binary_search(ls,v,isLastCheck=True) for v in test_cases]
tests3 = [binary_search(ls,v) for v in test_cases]

tests1
tests2
tests3





# def binary_search_it(ls,v):
#     """implementation of a simple finary search.
#         iterative implementation
#     Args:
#         ls (list): list of sorted floats
#         v (float): float we are searching for
#
#     Returns:
#         int: index of the v in the list or -1 if absent
#
#     """
#     l = 0
#     r = len(ls)-1
#     while(l<=r):
#         m = round(l +(r-l)/2)
#         #check if the number is the one we are looking for
#         if ls[m] == v:
#             return m
#         if ls[m] < v:
#             l = m+1
#         else:
#             r = m-1
#     return -1

# def binary_search_rec(ls,v,l,r):
#     """implementation of a simple finary search.
#         recursive implementation
#     Args:
#         ls (list): list of sorted floats
#         v (float): float we are searching for
#
#     Returns:
#         int: index of the v in the list or -1 if absent
#
#     """
#     if l<=r:
#         m = round(l +(r-l)/2)
#         #check if the number is the one we are looking for
#         if ls[m] == v:
#             return m
#         if ls[m] < v:
#             return binary_search_rec(ls,v,m+1,r)
#         else:
#             return binary_search_rec(ls,v,l,m-1)
#     else:
#         return -1

# tests_it = [binary_search_it(ls,v) for v in test_cases]
# tests_it = [it_binary_search_first(ls,v,isFirstCheck=True) for v in test_cases]
# tests_rec = [binary_search_rec(ls,v,0,len(ls)-1) for v in test_cases]
