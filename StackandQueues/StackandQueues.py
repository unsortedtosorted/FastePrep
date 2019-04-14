"""
Implement a stack using Queues.

1. push keep adding to q1
2. keep shifting all except last element to q2, change q1 to q2 and q2 to q1

"""


class stack_using_queue:
  #Write - Your - Code
  def __init__(self):
    self.q1 = deque()
    self.q2 = deque()
  
  def push(self, data):
    
    if self.q1:
      self.q1.appendleft(data)
    else:
      self.q1.appendleft(data)
    return data  

  def isEmpty(self):
    if self.q1:
      return True
    if self.q2:
      return True
    return False

  def pop(self):
    if self.q1:
      while len(self.q1)>1:
        curr = self.q1.pop()
        self.q2.appendleft(curr)
      curr = self.q1.pop()
      return curr
    else:
      while len(self.q2)>1:
        curr = self.q2.pop()
        self.q1.appendleft(curr)
      curr = self.q2.pop()
      return curr
    
    return -1
