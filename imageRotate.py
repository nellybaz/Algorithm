def imageRotate(image):
    new_row = []
    i = 0
    check = 0
    new_image = []
    while check < len(image):
        
        for row in image:
            new_row.append(row[i])
        new_image.append(list(reversed(new_row)))
        #print(new_image)
        del new_row[:]
        check+=1
        i+=1
        
    
    for x in new_image:
        print(x,'\n')
        
        
        
        
        
image = [[1,2,3],[4,5,6],[7,8,9]]
print(imageRotate(image))