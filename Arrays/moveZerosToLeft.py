"""
1. Maintain 2 pointers
    - start: index of first non zero number
    - stop : looks for zero

    if stop sees a zero:
        move (start,stop)
        start+=1
    stop+=1
    
    
    move function:
     
      valueToWrite = 0
      
      start from start:
          temp = arr[start]
          arr[start] = valueToWrite
          valueToWrite = temp
          start+=1
          
          
   Runtime : O(N^2)
          
"""



def moveZeros2left(arr):
    start = 0
    stop = 0

    while stop < len(arr):

        if arr[stop] == 0:
            move(arr,start, stop)
            start +=1
        stop += 1


def move(arr,start, stop):
    print (arr)
    temp = 0
    ind = start

    while ind <= stop:
        x = arr[ind]
        arr[ind] = temp
        temp = x
        ind += 1

arr = [1,2,0,0,4,7,0]
moveZeros2left(arr)
print (arr)

arr = [0,2,0,0,4,7,0]
moveZeros2left(arr)
print (arr)

arr = [0]
moveZeros2left(arr)
print (arr)
