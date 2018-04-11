def stringCompress(s):
    if len(s) == 1:
        return s
    
    d_hold = []
    last =''
   
    for c in s:
        
        if c not in d_hold and last != c:
            d_hold.append(c)
            d_hold.append(1)
            last = c
        elif c in d_hold and last == c:
            
            val = d_hold[-1]
            
            val = int(val)
            val+=1
            #print(val)
            d_hold[-1] = val
            last = c
            
            
            
        elif c in d_hold and last != c:
            d_hold.append(c)
            d_hold.append(1)            
            last = c
            
    if len(s) == len(d_hold):
        return s
    print(len(s), len(d_hold))
    return d_hold
            
s = 'aabbhhaabb'
print(stringCompress(s))