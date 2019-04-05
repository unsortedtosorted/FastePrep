"""
Find Low/High index

Binary search to get the mid

keeping looking in left , until mid-1 is still = val
keep looking right, until mid+1 is still = val

runtime : logn

"""


def findlowhigh(arr, val):

    def bs(start, stop, val):

        while start <= stop:
            mid = (start + stop)// 2
            if arr[mid] == val:
                return mid
            elif arr[mid] > val:
                stop -= 1
            elif arr[mid] < val:
                start += 1
        return -1

    pos = bs(0, len(arr) - 1, val)

    l = pos
    while l - 1 >= 0 and arr[l - 1] == val:
        l = bs(0, l - 1, val)
        print (l)
    r = pos
    while r + 1 < len(arr) and arr[r + 1] == val:
        r = bs(r + 1,len(arr)-1, val)


    return (l,r)

print (findlowhigh([1,2,3,4,5,5,5,5,5,5,5,5,6,7,8,9,10],5))
print (findlowhigh([1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6],5))
print (findlowhigh([1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6],2))
