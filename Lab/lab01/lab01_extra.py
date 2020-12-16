"""Optional questions for Lab 1"""

# While Loops

def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    NFact = 1
    while k > 0:
        NFact = NFact * n
        n -= 1
        k -= 1
    return NFact

def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    nStr = str(n)
    nList = list(nStr)
    if len(nList) <2:
        return False
    for i in range (0,len(nList)-1):
        if int(nList[i])==8 and int(nList[i+1])==8:
            return True

    return False

