"""
2 approch:

  1. top down :  swap left and right of root and go to children
  2. bottom down: reflect left and right children then go to parent

"""


def mirror_tree(root):
  #TODO: Write - Your - Code
  
  def BottomUpreflect(root):
    
    if root:
        
        if root.left or root.right:
          #reflect left and right subtree
          BottomUpreflect(root.left)
          BottomUpreflect(root.right)
          
          #swap left and right child
          lsub = root.left
          rsub = root.right
          root.left = rsub
          root.right = lsub
  def topDownReflect(root):
    if root:
      
      lsub = root.left
      rsub = root.right
      
      root.left = rsub
      root.right = lsub
      
      topDownReflect(root.left)
      topDownReflect(root.right)
      
      
  BottomUpreflect(root)
  topDownReflect(root)
  BottomUpreflect(root)
  return root
