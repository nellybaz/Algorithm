def isUnigue(st):
    if len(st) > 256:
        return False
    else:
        checker = 0
        for i in st:
            val = ord(i)
            pos = 1 << val
            #print(val)
            #print(pos)
            if checker & pos > 0:
                return False
            checker |= pos
        #print(checker)
        return True
    
s = 'abcda'
print(isUnigue(s))