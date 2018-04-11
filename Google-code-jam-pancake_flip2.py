def pan_flip(p,k):
    side_happies=0
    all_happy=False 
    
    blank_count=0 
    happy_count=0
    flip_count = 0
    flip_left = False
    result = ''
    while all_happy==False:
      for i in range(len(p)):
          if p[i] == '+':
              happy_count+=1
              if happy_count == len(p):                  
                  return p, 'all happy and '+str(flip_count)+ ' flip was made'
              elif blank_count>=k:
                  #if its happy side, and blank side before it is equal or more than k, flip it
                  z = i-1
                  for j in range(blank_count):
                      p[z] = '+'
                      z-=1
                  flip_count+=1
                  blank_count=0
                  #return p
                                
          elif p[i] == '-':
              
              
              blank_count+=1
              if blank_count==len(p):
                  for j in range(blank_count):
                      p[j] = '+'
                  flip_count+=1
                  
              elif blank_count >= k and i==len(p)-1:
                  for q in range(i, i-blank_count, -1):
                      p[q] = '+'
                  flip_count+=1
                  blank_count = 0
                  #return p, 'flip'
                  
              elif blank_count >= k and p[i+1] == '+':
                  continue
#                  for q in range(i, i-blank_count, -1):
#                      p[q] = '+'
#                  flip_count+=1
#                  blank_count = 0
#                  #return p, 'flip'
                  
              elif i!=0 and blank_count == 0:           
                  return p, 'IMpossible'
                 
              elif blank_count < k:
                  if p[i+1] == '+':
                      continue
                  
                  if i == 0:
                      #return 'ok'
                      continue
              
              
                  if i == len(p)-1 and p[i-1]== '+':
                      for a in range(i, 0, -1):
                          if p[a-1] == '-':
                              return 'impo'
                          if p[a-1] == '+':
                              side_happies+=1
                              
                              if side_happies >= k:
                                  flip_left = True
                                  break
                      if side_happies < k:
                          return side_happies, 'impossible'
                      if flip_left:
                          v=i-1
                          for w in range(side_happies):
                              p[v] = '-'
                              v-=1
                          blank_count = side_happies+1
                          flip_count+=1
                          
                                  
                              
                      #return p
                  
#                  if p[i+1] == '-' and i!=len(p)-1:
#                      print('move')
#                      continue
#              
                  
                      return 'find your way'
                 
      happy_count =0          
      blank_count=0   
      #all_happy=True
    return p, flip_count
    
    
p = ['-','-','+','+']
print(pan_flip(p,2))