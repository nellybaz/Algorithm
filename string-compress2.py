def stringCompress(s):
    if len(s) == 1:
        return s
    
    hold = []
    last =''
    
    def append1(x):
        hold.append(x)
        hold.append(1)
   
    for c in s:
        
        if c not in hold and last != c:
            append1(c)
            last = c
        elif c in hold and last == c:
            
            val = hold[-1]
            
            val = int(val)
            val+=1            
            hold[-1] = val
            last = c
            
            
            
        elif c in hold and last != c:
            append1(c)            
            last = c
            
    if len(s) <= len(hold):
        return s
    

        
    
    new_s = ''
    for x in hold:
        new_s+=str(x)
        
    return new_s
            
s = 'aaaaaaaaaaaaaaaaaaaaaaaaaabbbDDD'
print(stringCompress(s))