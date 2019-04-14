class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        if len(self.s1) == 0:
            self.s1.append(x)
        else:
            self.s2.append(x)
            
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        
        while len(self.s1) > 1:
            self.s2.append(self.s1.pop())
            
        
        temp = self.s1
        self.s1 = self.s2
        self.s2 = temp
       
        
        return self.s2.pop()

        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        while len(self.s1) > 0:
            
            curr = self.s1.pop()
            self.s2.append(curr)
        while len(self.s2) > 0:
            self.s1.append(self.s2.pop())
        
        return curr

        
        
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if len(self.s1)== 0:
            return True

        
        return False
            


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
