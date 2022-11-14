import image
''' Stater project for playing with images
    COMP 115 - Fall 2019
'''


def makeDarker(img):
    ''' This function takes a gif image gif as input and returns a new image that
        has the intensity of every colour halved
    '''
    #create an empty image of the same size
    new_image = image.EmptyImage(img.getWidth(),img.getHeight())
    
    #for all pixels in the image img row by row, column by column
    for row in range(img.getHeight()):
        for col in range(img.getWidth()):
            
            #get the pixel
            p = img.getPixel(col, row)

            #get RGB components of the pixel
            red = p.getRed()
            green = p.getGreen()
            blue = p.getBlue()

            #set the RGB components of the corresponding new image to
            #half the intensity of the old image
            p.setRed(red//2)
            p.setGreen(green//2)
            p.setBlue(blue//2)
    
            #set the pixel in the new image
            new_image.setPixel(col,row, p)

           
    return new_image


def main():
    IMAGE_FILE = 'cap.gif'
    
    original_img = image.Image(IMAGE_FILE)
    win1 = image.ImageWin(original_img.getWidth(), original_img.getHeight())
    original_img.draw(win1)
    
    # Create a transformed copy of the image and display it    
    transformed_img = makeDarker(original_img)
    win2 = image.ImageWin(transformed_img.getWidth(), transformed_img.getHeight())
    transformed_img.draw(win2)
               

main()