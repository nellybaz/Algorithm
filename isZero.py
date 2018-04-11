def isZero(s):
    x,x1=0,0
    y,y1 =0,0
    #count=0
    #p=0
   
    c = 9999999999999
    for row in s:
        
        for col in row:
            
            if col==0 and c!= row.index(col):
                y,y1=0,0
                x,x1=0,0 
                c = row.index(col)
                while y<len(s):
                    row[x]=0
                    x+=1
                    y+=1
                while y1 < len(row):
                    s[x1][c] = 0
                    x1+=1
                    y1+=1
            
                
    for x in s:
        print(x, '\n')
           
s = [[1,4,0,6],[6,3,7,6],[3,2,4,5],[8,5,5,0]]
print(isZero(s))
                