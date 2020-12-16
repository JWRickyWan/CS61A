"""Discussion 3: Feb 12, 2020
-----------------Recursion---------------
"""
def product_nums(m,n):
    if m ==0 or n==0:
        return 0
    else:
        return m + product_nums(m,n-1)
        
def hailstone(n):
    """Print out the hailstone sequence starting at n,
    and return thenumber of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    print(n)
    if n ==1:
        return 1
    elif n%2 ==0:
        return 1+hailstone(n//2)
    else:
        return 1+hailstone(3*n+1)
