# import random
# ls = [54, 42, 48, 95, 44, 51, 49, 21, 62, 30]#random.sample(range(1, 100), 10)
#
# def quicksort(ls):
#     if len(ls) < 2:
#         return ls
#     else:
#         pivot = ls[0]
#         ls_left = []
#         ls_right = []
#         for el in ls[1:]:
#             if el < pivot:
#                 ls_left.append(el)
#             else:
#                 ls_right.append(el)
#
#         return quicksort(ls_left) + [pivot] + quicksort(ls_right)
