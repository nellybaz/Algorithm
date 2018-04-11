dic = {0:'001309', 1:'121009', 2:'202209'}

def drive(r,c,v,ri,b,s):
    wait = 0
    def move(r,c):
        '''a function that will move the vehicles'''
#        updated_map = {1:2,2:4}
#        for i in updated_map.values():
#            print(i)
        marker = []
        map_table = {'R':'01234', 'C': '01234'}
        isMove = True
        temp_pos = ''
        pos = 0
        while isMove:
            if pos >= len(map_table['R']):
                break
            else:
                
                #map_table['R'][pos]
                temppos = pos-1
                print(map_table['R'][pos], map_table['C'][temppos])
              #print(map_table['R'][0], map_table['C'][pos])
                pos += 1
            
            
    for rides in dic:
        if dic[rides][:2] == '00':
            #checking the ride from start cordinates
            if int(dic[rides][-2:-1]) > 0:
                #checking if the earliest start is not zero
                for i in range(int(dic[rides][-2:-1])):
                    #wait for the earliest start step
                    wait += 1
                
                import time
                time.sleep(wait)
                print('I have waited for '+str(wait)+' steps')
                
            elif int(dic[rides][-2:-1]) == 0:
                #if earliest start is zero, start moving to finish
                print('start moving to end')
                move(3,4)
                
                

        
                    
            
    
print(drive(1,2,3,4,5,6))