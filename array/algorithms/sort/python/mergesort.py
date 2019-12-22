def merge(first,second):
    merged = []
    f, s = 0, 0
    while f<len(first) and s<len(second):
        if first[f] < second[s]:
            merged.append(first[f])
            f+=1
        else:
            merged.append(second[s])
            s+=1
    merged += first[f:]
    merged += second[s:]
    return merged

def merge_sort(ls):
    if len(ls)<=1:
        return ls
    i_mid = len(ls)//2
    left = merge_sort(ls[:i_mid])
    right = merge_sort(ls[i_mid:])
    return merge(left, right)


ls = [7,7,9,9,9,1,4,2,2,6,6,6,1,2,5]
ls = merge_sort(ls)
ls


count = collections.Counter()
