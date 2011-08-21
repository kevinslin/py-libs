def binary_search(a, b, target):         
    """                            
    Perform binary search on input with two starting values
    @param:     
    a - lower bound starting value
    b - upper bound starting value
    target - target length
    @return:
            result of binary search   
    >>> r1 = binary_search(1, 9, 2) 
    Traceback (most recent call last):
        ...                                      
    Exception: Range too small
    >>> binary_search(3, 12, 1)
    Traceback (most recent call last):
        ...                                      
    Exception: Range too small
    >>> binary_search(1, 12, 2) #doctest: +SKIP 
    9
    >>> binary_search(1, 100, 2) #doctest: +SKIP 
    9
    >>> binary_search(1, 100000, 2) #doctest: +SKIP 
    9
    >>> binary_search(1, pow(10, 5), 3) #doctest: +SKIP 
    31
    """     
    for i in xrange(target):
        offset = offset + str(9)            
    offset = int(offset)    

    m = int(math.ceil(((a+b)/2.0)))
    epsilon=0.000001
    #TODO: replace pow with func
    r_a = pow(a, 2) - offset
    r_b = pow(b, 2) - offset
    r_m = pow(m, 2) - offset    
    if (r_a * r_b >= 0):        
        raise Exception("Range too small")
    else:
        return binary_search_helper(a, b, offset)    

def binary_search_helper(a, b, target):
    """
    Helper to binary_search
    @param:
    a - lower bound
    b - upper bound
    target - ideal value
    """                
    sl.debug("in binary search helper:\n a:%i, b:%i" % (a, b))          
    m = int(math.ceil(((a+b)/2.0)))
    epsilon=0.000001
    r_a = pow(a, 2) - target
    r_b = pow(b, 2) - target
    r_m = pow(m, 2) - target         
    sl.debug("results; a:%i, b:%i, m: %i" %(r_a, r_b, r_m))    
    if (abs(m) <= epsilon): #since we want webM to be between 0 and epsilon, we put absolute values around webM
        return m       
    else:                  
        if (r_a * r_b > 0):        #not best answer but close enough    
            return b       
        else:
            if (r_a * r_m) < 0: 
                if (m == b):    #close enough answer                    
                    return a
                return binary_search_helper(a, m, target)
            else:                  
                if (b == m):
                    return a
                return binary_search_helper(m, b, target)

