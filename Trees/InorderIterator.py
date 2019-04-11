"""

Write an In-Order Iterator for a Binary Tree
Implement a class that implements an InOrder Iterator on a Binary Tree

1. prepare tree by pushing all left nodes to the stack
2. on pop, return curr node, again push all left nodes of the right child of curr


"""

class InorderIterator:
  def __init__(self, root):
    #TODO: Write - Your - Code
    
    self.stack = [root]
    
    temp = root
    
    while temp.left:
      self.stack.append(temp.left)
      temp = temp.left
      
      
    return
  
  def hasNext(self):
    
    return len(self.stack)!=0
  
  # getNext returns null if there are no more elements in tree
  def getNext(self):
    
    curr = self.stack.pop()
    
    if curr.right:
      
      temp = curr.right
      while temp:
        self.stack.append(temp)
        temp = temp.left
      
    
    return curr

def inorder_using_iterator(root):
  iter = InorderIterator(root)
  result = ""
  while iter.hasNext():
    ptr = iter.getNext()
    result += str(ptr.data) + " "
  return result
