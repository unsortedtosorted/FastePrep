"""
Find an efficient algorithm to find the maximum sum of a 
subsequence in an array so that no consecutive elements 
are part of this subsequence.

Iterate over the entire input array, and in every iteration pick the maximum of these two values:

Max Sum of the last iteration
Max Sum of second last iteration + current iteration index.


"""

def find_max_sum_nonadjacent(a):
    def dp(i):

        if i <= 1:
            return a[i]
        else:
            curr = a[i]
            return max(dp(i-1),dp(i-2)+curr,curr,dp(i-2))


    return dp(len(a)-1)
