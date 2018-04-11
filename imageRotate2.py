def rotate(image):
    
    j=0
    i=0
    new_row = []
    new_image = []
    while j < len(image):
        #print(1)
        for row in image:
            new_row.append(row[i])
        new_image.append(list(reversed(new_row)))
        del new_row[:]
        j+=1
        i+=1
        
        
    #print(list(reversed(new_row1)))
    #print(list(reversed(new_row2)))
    print('Image')
    for x in image:
        
        print(x,'\n')
        
        
    print('Rotated image')
    for x in new_image:
        
        print(x,'\n')
    #print(image)
#image = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
image = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate(image))