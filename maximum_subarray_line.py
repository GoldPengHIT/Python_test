

def maxinum_line(A,left,right):
    l=left
    r=right
    temp =0
    summax=float("-inf")
    for i in range(left,right):
        temp += A[i]
        if temp > summax:
            summax = temp
            r=i
        if temp < 0:
            temp =0
            l =i+1
    return [summax,l,r]



sub = [3,-1,2,5,-3,4,-6,-7,1,8,-3,5,9]
[summax,left,right] = maxinum_line(sub,0,len(sub))
print(summax)
print(left)
print(right)
