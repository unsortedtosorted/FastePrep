"""
Print all braces combinations for a given value 'n' so that they are balanced.

Keep track of open and close brackets.
if open brackets are less than n, add it and increament o by 1
if close brackets are less than open brackets, add it and increment c by 1


"""
def print_all_braces(n):
  
    out = []
    def dfs(o,c,s):

        if o == n and c == n:
            out.append(s)
            print (s)
        else:
            if o < n:
                s = s+["{"]
                dfs(o+1,c,s)
                s = s[:-1]
                
            if c < o:
                s = s+["}"]
                dfs(o,c+1,s)
                s = s[:-1]

    dfs(0,0,[])
    
    return out
