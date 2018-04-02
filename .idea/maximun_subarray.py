import math

def find_max_crossing_subarrary(A,low,mid,high):
    left_sum=float("-inf")
    sum=0
    max_left=0
    max_right=0
    mid = int(mid)
    low = int(low)
    for i in range(mid,low-1,-1):
        sum = sum +A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    right_sum = float("-inf")
    sum = 0
    high = int(high)
    for j in range(mid+1,high):
        sum  += A[j]
        if sum > right_sum:
            right_sum=sum
            max_right=j
    return [max_left,max_right,left_sum+right_sum]


def find_maximum_subarray(A,low,high):
    if high == low:

        low = int(low)
        return [low,high,A[low]]
    else:
        mid = math.floor((low+high)/2)
        [left_low,left_high,left_sum]=find_maximum_subarray(A,low,mid)
        [right_low,right_high,right_sum]=find_maximum_subarray(A,mid+1,high)
        [cross_low,cross_high,cross_sum]=find_max_crossing_subarrary(A,low,mid,high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return [left_low,left_high,left_sum]
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return [right_low,right_high,right_sum]
        else:
            return [cross_low,cross_high,cross_sum]






a = [1,5,-6,7,-10,4,1,9,-5,6,-5]
[low,high,sum]=find_maximum_subarray(a,0,10)
print(low)
print(high)
print(sum)

