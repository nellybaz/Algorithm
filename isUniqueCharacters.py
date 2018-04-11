def isUniqueChar(x):
    if not isinstance(x, str) or not x:
        return False
    else:
        check = set()
        for i in x:
            if i in check:
                return False
            else:
                check.add(i)
        return True
    
x = 'abcc'
print(isUniqueChar(x))

