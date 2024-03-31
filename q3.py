def q3(arr,n):
    count = 0
    for i in arr:
        if (n == i):
            count+=1
    return count

q3([2,4,8,9,78,90,3],9)
