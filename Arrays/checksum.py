"""
Given an array of integers and a value, determine 
if there are any two integers in the array whose 
sum is equal to the given value.


1. keep seen value in set
2. if seen and val-seen in set, return True
3. can also be solved using binary search:
    
  while left < right:
    found = arr[left] + arr[right]
    
    if found > val:
        right = right - 1
    elif found < val :
          left = left+=1
    else:
        return True

  return False
"""

def checksum(arr, val):
    m = set()

    for x in arr:
        m.add(x)
        if val - x in m:
            return True

    return False

print (checksum([2, 1, 8, 4, 7, 3], 3))
print (checksum([2, 1, 8, 4, 7, 3], 7))
print (checksum([2, 1, 8, 4, 7, 3], 20))
