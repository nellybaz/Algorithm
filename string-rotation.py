def stringRotation(a,b):
    '''Same as isPemutation function'''
    if not isinstance(a,str) or not isinstance(b,str) or not a or not b or len(a) != len(b):
        return False
    else:
        checklist = {}
        for i in a:
            if i in checklist:
                checklist[i] += 1
            else:
                checklist[i] = 1
        
        for char in b:
            if char not in checklist:
                return False
            elif checklist[char] == 0:
                return False
            else:
                checklist[char] -= 1
            
        return True


    
    
s1 = 'gmn'
s2 = 'anm'
print(stringRotation(s1,s2))