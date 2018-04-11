def possiblePalindrome(s):
    if len(s) == 1:
        return s
    new_l = {}    
    for char in s:
        if char in new_l:
            new_l[char]+=1
        else:
            new_l[char] = 1
    print( new_l)
    count_odd = 0
    left = 0
    right = -1
    isPal_odd = False
    for key in new_l:
        if len(s) % 2 == 0 and new_l[key] % 2 != 0:
            return 'Not a palidrome'
        
        elif len(s) % 2 != 0 and new_l[key] %2!=0:
            count_odd+=1
            if count_odd>1:
                return 'Not a palidrome'
            else:
                isPal_odd = True
            
      
            
        
            
    new_new_l = [0]*len(s)
    for x in new_l:        
        if new_l[x] >= 2:
            
            
            new_new_l[right] = x
            new_new_l[left] = x
            right-=1
            left+=1
        if isPal_odd and new_l[x] % 2 != 0:
            
            mid = len(new_new_l) //2
                #print(mid)
            new_new_l[mid] = x
                
            
        
            
    return new_new_l
            
s = 'cccfccc'
print(possiblePalindrome(s))