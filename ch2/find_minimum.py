def find_min_quadratic(ls):
    """Return the minimum number in a list in O(n^2)."""
    
    m = ls[0]
    
    # Compare each number to every other number on the list
    for n in ls:
        is_min = True
        for other in ls:
            if other < n:
                is_min = False
        if is_min:
            m = n
    
    return m


def find_min_linear(ls):
    """Return the minimum number in a list in O(n)."""
    
    m = ls[0]
    
    for n in ls:
        if n < m:
            m = n
    
    return m