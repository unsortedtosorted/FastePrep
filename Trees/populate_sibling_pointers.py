"""
Connect Same Level Siblings

1. save all nodes to dict with nodes with same level at same key
2. go to each node in all level and connect them

"""

from collections import deque,defaultdict
def populate_sibling_pointers(root):
  #TODO: Write - Your - Code
  level = defaultdict(list)
  q = deque()
  q.append((root,0))
  
  while q:
    
    curr = q.pop()
    if not curr:
      continue
      
    level[curr[1]].append(curr[0])
    if curr[0].left:
      q.appendleft((curr[0].left,curr[1]+1))
    if curr[0].right:
      q.appendleft((curr[0].right,curr[1]+1))
    
  for x in level:
    prev = level[x][0]
    for y in level[x][1:]:
      prev.next = y
      prev = prev.next

  return root 
