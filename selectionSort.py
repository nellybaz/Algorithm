def selectionSort(s):
    for i in range(0, len(s)-1):
        minIndex = i
        for j in range(i+1, len(s)):
            if s[j] < s[minIndex]:
                minIndex = j
        if minIndex != i:
            s[i],s[minIndex] = s[minIndex], s[i]
    return s
            
s = [2,1,3,6,5,1,9,4]
print(selectionSort(s))