def bs(arr,key):
  
  low = 0
  high = len(arr)
  
  while low<high:
    
    mid = (high+low)//2
    
    if arr[mid] == key:
      return mid
    
    elif arr[mid] > key:
      high = mid-1
      
    else:
      low = mid+1
    
  return -1
  
  

def find_low_index(arr,key):
 #TODO: Write - Your - Code
  val = (bs(arr,key))
  if val == -1:
    return -1
  while arr[val] == key:
    val-=1
  return val+1
  

def find_high_index(arr,key):
  #TODO: Write - Your - Code
  val = (bs(arr,key))
  if val == -1:
    return -1
  while arr[val] == key:
    val+=1
  return val-1
