import random
def partition(ls,low,high):
    """partition on the first index of the array"""
    ## if random is desired
    # k = random.randint(low, high)
    # ls[low], ls[k] = ls[k], ls[low]
    ip = low
    for i in range(low+1,high+1):
        if ls[i]<=ls[low]:
            ip+=1
            ls[i], ls[ip] = ls[ip], ls[i]
    ls[ip], ls[low] = ls[low], ls[ip]
    return ip

def quicksort(ls, low, high):
    if high <= low:
        return
    ip = partition(ls,low,high)
    quicksort(ls, low, ip-1)
    quicksort(ls, ip+1, high)

ls = [7,7,9,9,9,1,4,2,2,6,6,6,1,2,5]
quicksort(ls,0,len(ls)-1)
ls
