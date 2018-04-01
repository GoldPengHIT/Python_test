

def insert_sort(lists):
    count = len(lists)
    for i in range(1,count):
        key = lists[i]
        j = i - 1
        while (j >= 0 and lists[j] > key):
            lists[j+1]=lists[j]
            lists[j]= key
            j -= 1
    return lists



ll=[3, 4, 1, 6, 2, 9, 7, 0, 8, 5]
lls=insert_sort(ll)
print(lls)