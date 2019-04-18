"""
Figure out whether the given words can form a circular chain.

"""
from collections import defaultdict


def findChain(words):

    if len(words) <= 1:
        print (str(words)+" "+str(False))
        return False
    edge = defaultdict(list)


    for x in words:
        for y in words:
            if y[0] == x[-1]:
                edge[x].append(y)



    def backtrack(curr,visited):

        toVisit = edge[curr]

        if curr == words[0]:

            if len(visited) == len(words)+1:
                if set(visited) == set(words):

                    return True
                else:
                    return False

        if len(visited) > len(words)+1:
            return False

        for x in toVisit:

            visited.append(x)
            if backtrack(x, visited):
                return True
            visited.pop()

        return False

    print (str(words) +" "+ str(backtrack(words[0],[words[0]])))

l = ["eve", "eat", "ripe", "tear"]
findChain(l)

l = ["bad", "cab", "bac", "dab"]
findChain(l)

l = ["deg", "fed"]
findChain(l)

l = ["a", "a"]
findChain(l)

l = ["ghi", "abc", "def", "xyz"]
findChain(l)

l = []
findChain(l)

l = ["aa", "aa"]
findChain(l)


l = ["aba", "aba"]
findChain(l)

l = ["aba", "bab"]
findChain(l)

l = ["eve"]

findChain(l)
l = ["eve", "eve", "sail", "lass"]

findChain(l)
l = ["aa", "bb"]

findChain(l)
l = ["ab", "cd", "dc", "ba"]
findChain(l)

l = ["ab", "bc", "cd", "de", "ce", "ea"]
findChain(l)


l = ["ab", "bc", "bc", "cd", "ce", "de", "ea", "eb"]
findChain(l)
