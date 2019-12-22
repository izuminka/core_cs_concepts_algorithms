import random #import randrange
import time

def quicksort(ls):
    len_ls = len(ls)
    if len_ls < 2:
        return ls
    else:
        pivot = ls[random.randrange(len_ls)]
        ls_left = []
        ls_right = []
        pivots = []
        for el in ls:
            if el == pivot:
                pivots.append(el)
            elif el < pivot:
                ls_left.append(el)
            else:
                ls_right.append(el)
        return quicksort(ls_left) + pivots + quicksort(ls_right)



num_trials = 10
arr_size = 10**6
max_val = 10**6
min_val = -max_val


results = []
for i in range(num_trials):
    ls = random.sample(range(min_val, max_val), arr_size) #[54, 42, 2, 48, 95, 44, 51,2, 49, 21, 62, 30] #
    start = time.time()
    test = quicksort(ls)
    end = time.time()
    results.append( (end-start)*1000)
print(results)

average = 0
for r in results:
    average+=r
average = average/num_trials
print(average)