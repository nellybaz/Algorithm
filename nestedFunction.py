def isDo(l, n=0):
    #n = 0
    if n >= len(l):
        return 
   # print(l[n])
    if l[n] % 2 != 0:
        print(l[n])
    #n+=1
    return isDo(l, n+1)
    
    
l = [2,4,7,5,3,6,4,6]
print(isDo(l ))