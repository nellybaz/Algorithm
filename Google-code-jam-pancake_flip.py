def pancakes(p, k):
    blank_count = 0
    flip_count = 0
    go_left = True
    side_happies=0
    for i in range(0, len(p)):
       if p[i] == '-':
          blank_count+=1
          if i!=len(p)-1 and p[i+1]!='-':              
              if blank_count >= k and p[i+1]!='-':
                  
                  flip_count+=1
                  blank_count = 0
          
              elif blank_count < k:
                  #print('check sides')
                  #check left first
                  for j in range(i,0,-1):                      
                      if p[j-1] == '+':
                          side_happies+=1
                          if side_happies >= k:
                              flip_count+=2
                              side_happies=0
                              break
                      else:
                          go_left = False
                          print('left didn\'t work, go right')

                  
          if i == len(p)-1:
              if blank_count>=k:
                  flip_count +=1
                 
              else:
                 
                  for j in range(i, 0, -1):
                      
                      if p[j-1] == '+':
                          side_happies+=1
                          if side_happies >= k:
                              z=i
                              for k in range(side_happies):
                                  p[z-1]='-'
                                  z-=1
                              flip_count+=2
                              side_happies=0
                          
                          
                      else:
                          break
                  
       elif  p[i] == '+':
           blank_count=0
           
    return flip_count, blank_count, p         
                            
             
    #print(blank_count, happy_count, flip_count)
    
p = ['+','+','-']
print(pancakes(p,2))
        