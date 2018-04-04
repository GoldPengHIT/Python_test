import random



def QuikSort(A,p,r):
    if p < r:
        q=Partition(A,p,r)
        QuikSort(A,p,q-1)
        QuikSort(A,q+1,r)



def Partition(A,p,r):
    num = random.randint(0,r-p)
    x = A[num+p]
    i = p-1
    for j in range(p,r):
        if A[j] <= x:
            i += 1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[r] = A[r],A[i+1]
    return i+1




a=[15,34,42,32,10,9,50,6,47,38,19,20]
QuikSort(a,0,len(a)-1)
print(a)
