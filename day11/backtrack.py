import functools
import sys

n = int(input())
k = int(input())

sys.setrecursionlimit(10000000)

@functools.cache
def fun(n, k, s):
    if n == 0 and s >= k:
        return 1
    if n + s < k:
        return 0
    
    return fun(n-1, k, s) + fun(n-1, k, s+1)

print(fun(n, k, 0))


"""

time complexity: O(2^n)

"""