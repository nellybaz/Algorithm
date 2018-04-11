def flip(p,k):
    b_c = 0
    h_c = 0
    f_c = 0
    all_happy = False
    while all_happy == False:
        for i in range(len(p)):
            if p[i] == '+':
                h_c+=1
                if h_c ==len(p):
                    all_happy = True
                    i = 0
                    return 'all happy', p, h_c, b_c, f_c
                
                elif b_c >= k and p[i] == '+':
                    for j in range(i-1, (i-b_c)-1, -1):
                        p[j] = '+'
                    b_c = 0
                    f_c+=1
                    print(i, f_c, 'p', p)
                    i = 0
                    
                        
                if i == len(p)-1 and h_c >= k:
                    for j in range(i, (i-b_c)-1, -1):
                        p[j] = '-'   
                    b_c = 0
                    f_c+=1
                    print(i, f_c, 'o', p, h_c)
                    i = 0
                            
                
                
                else:
                    continue
                
                
            elif p[i] == '-':
                b_c+=1
                if b_c == len(p):
                    for j in range(len(p)):
                        p[j] = '+'
                    h_c = 0
                    b_c = 0
                    f_c +=1
                    print(i, f_c, 'n', p)
                    i = 0
                        
                elif h_c >= k:
                    for j in range(i-1, (i-h_c)-1, -1):
                        p[j] = '+'
                    h_c = 0
                    b_c = 0
                    f_c+=1
                    print(i, f_c, 'm')
                    i = 0
                
                if i == len(p)-1 and b_c >= k:
                    for j in range(i, (i-b_c)-1, -1):
                        p[j] = '+'
                    h_c = 0
                    b_c = 0
                    f_c+=1
                    print(i, f_c, 'me')
                    i = 0
                    
                elif b_c == 1 or b_c < k:
                        
                        for j in range(i, i+k):
                            if p[j] == '-':
                                p[j] = '+'
                            else:
                                p[j] = '-'
                        #f_c+=1
                        print(i, f_c, 'l', p)
                        i = 0
                        break
                        h_c, b_c = 0,0
                        
                        
                    
s = '--+'
p = []
for j in range(len(s)):
    p.append(s[j])
                
print(flip(p,2))