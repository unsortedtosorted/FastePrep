"""

1. There are two ways to do binary seach 
  1.1 Recursive
      Time complexity : O(logN)
      Space complexity : O(logN) {because of memory consumption on call stack}
      
  1.2 Iterative
      Time complexity : O(logN)
      Space complexity : O(1)


"""




#a is sorted list
def binary_search(a, key): 
  def iterative(a,key):
    
    l=0
    r=len(a)
    
    
    while l<r:
      mid=(l+r)//2
      
      if a[mid]==key:
        return mid
      elif a[mid]>key:
        r=mid-1
      else:
        l=mid+1
    
    return -1
    
    
  return iterative(a,key)
  
  def recursive(a,key):
    
    def search(l,r):
      mid=(l+r)//2
      if l>r:
        return -1
      
      if a[mid]==key:
        return mid
      elif a[mid]>key:
        return search(l,mid-1)
      else:
        return search(mid+1,r)
      
    return search(0,len(a))  
  
  return recursive(a,key)
 
  return -1
