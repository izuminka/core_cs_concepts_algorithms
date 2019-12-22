from math import ceil

a = [0, 42, 2, 100, 1, 48, 95, 44, 51, 2, 49, 21, 62, 30]


def parent(i):
    return ceil(i/2) - 1

def left(i):
    return i*2 + 1

def right(i):
    return i*2 + 2

def last_ind(ls_nums):
    return len(ls_nums) - 1

# def swap(ls_nums, i, j):
    # temp = ls_nums[i]
    # ls_nums[i] = ls_nums[j]
    # ls_nums[j] = temp
    # return ls_nums


def max_heapify(ls_nums, l_ind, i):
    i_of_lar = i

    # check left child, make sure it's not outside the range
    if (l_ind >= left(i)) and (ls_nums[left(i)] > ls_nums[i]):
        i_of_lar = left(i)

    # check right child, make sure it's not outside the range
    if (l_ind >= right(i)) and (ls_nums[right(i)] > ls_nums[i_of_lar]):
        i_of_lar = right(i)

    if i_of_lar != i:
        # swap to make i the largest of the 3
        # ls_nums = swap(ls_nums, i, i_of_lar)
        ls_nums[i], ls_nums[i_of_lar] = ls_nums[i_of_lar], ls_nums[i]
        return max_heapify(ls_nums, l_ind, i_of_lar)
    else:
        return ls_nums

# Test max_heapify
# print(a)
# a = max_heapify(a, 0)
# print(a)

def build_max_heap(ls_nums):
    """ build a binary heap out of the array"""
    for i in range(parent(last_ind(ls_nums)),-1, -1):
        ls_nums = max_heapify(ls_nums,last_ind(ls_nums), i)
    return ls_nums

# test build_max_heap
# print(a)
# a = build_max_heap(a)
# print(a)

def heapsort(ls_nums):
    ls_nums = build_max_heap(ls_nums)
    print(ls_nums)
    l_ind = last_ind(ls_nums)
    while(l_ind!=0):
        # ls_nums = swap(ls_nums, 0, l_ind)
        ls_nums[0], ls_nums[l_ind] = ls_nums[l_ind], ls_nums[0]
        l_ind-=1
        ls_nums = max_heapify(ls_nums, l_ind, 0)
        # print(l_ind)
        # print(ls_nums)

    return ls_nums



# test build_max_heap
print(a)
a = heapsort(a)
print(a)