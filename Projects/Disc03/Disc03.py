"""Discussion 3: Feb 12, 2020
-----------------Recursion---------------
"""
def product_nums(m,n):
    if m ==0 or n==0:
        return 0
    else:
        return m + product_nums(m,n-1)
        
