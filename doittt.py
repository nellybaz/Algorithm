def pemutation(a,b):
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
    
a = 'dog'
b = 'ddo'

print(pemutation(a,b))