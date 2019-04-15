"""
Expression Evaluation
Given an arithmetic expression, evaluate it

"""

def evaluate(expo):
  
  #expression stack
  exp = []
  
  #operator stack
  oper = []
  
  #assign priority
  p = {}
  p['/'] = 2
  p['*'] = 2
  p['+'] = 1
  p['-'] = 1
  
  
  #create postfix
  temp = ''
  
  for x in expo:
    
    if x == ' ':
      continue
    if x not in p:
      temp = temp+x
    else:
      
      exp.append(temp)
      temp = ''
      
      while len(oper) > 1 and p[oper[-1]] >= p[x]:
        exp.append(oper.pop())
      oper.append(x)
   
  if temp!= '':
    exp.append(temp)
  
  while len(oper) > 0:
    exp.append(oper.pop())
  
  #evaluate postfix
  
  total = []
  
  for x in exp:
    
    if x not in p:
      total.append(float(x))
    else:
      
      r = total.pop()
      l = total.pop()
      result = 0
      if x == '+':
        result = l+r
      elif x == '-':
        result = l-r
      elif x == '*':
        result = l*r
      elif x == '/':
        result = l/r
      
      total.append(result)
        
   
  return total[0]
