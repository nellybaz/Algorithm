fib_cache = {}
def fibRecur(l):  
    """fibonacci recursion with memoization"""
   
    if l in fib_cache:
        return fib_cache[l]
    if l == 1:
        return 1
    elif l == 2:
        return 1
    elif l > 2:
        value =  fibRecur(l-1) + fibRecur(l-2)
        fib_cache[l]  = value
        return value
    
    
    
    
#l = [1,1,2,3,5,8,13,21]
#print(selectionRecur(8))
for x in range(1,1001):
    print(x, ":", fibRecur(x))