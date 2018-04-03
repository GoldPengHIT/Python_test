#coding:utf-8
import random
import math

def Max_Heapify(A,HeapSize,i):#维护堆
    l=2*i+1
    r=l+1
    largest = i
    if l <= HeapSize-1  and A[l] > A[i]:
        largest = l
    if r <= HeapSize-1  and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i],A[largest]=A[largest],A[i]
        Max_Heapify(A,HeapSize,largest)

def Build_Max_Heap(A):#创建堆
    HeapSize = len(A)
    for i in range(int(math.floor((HeapSize)/2))-1,-1,-1):
        Max_Heapify(A,HeapSize,i)

def HeapSort(A):#堆排序
    Build_Max_Heap(A)
    for i in range(len(A)-1,-1,-1):
        A[0],A[i]=A[i],A[0]
        Max_Heapify(A,i,0)
    return A

if __name__ == '__main__':
    a = [30,50,57,77,62,78,94,80,84]
    print (a)
    s = HeapSort(a)
    print (s)
    b = [random.randint(1,1000) for i in range(1000)]
    print b
    HeapSort(b)
    print b
