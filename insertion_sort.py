def insertionSort(s):
    if len(s) == 1:
        return s
    
    for i in range(1,len(s)): 
       
        for j in range(i-1,0,-1):
            
            if s[j] > s[j+1]:
                s[j],s[j+1] = s[j+1],s[j]
            else:
                break
            
            
    return s
                
s = [2,1,4,5,3,8,0,9,11,30]
print(insertionSort(s))