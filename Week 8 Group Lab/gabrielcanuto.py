'''
Gabriel Canuto COMP 115 
'''

import image
'''
Stater project for playing with images
COMP 115 - Fall 2019
'''

def makeDarker(img):
    ''' This function takes a gif image gif as input and returns a new image that
        has the intensity of every colour halved
    '''
    #create an empty image of the same size
    
    new_image = image.EmptyImage(img.getWidth(),img.getHeight())
    print('Test')
    
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

#Exercise 1
'''
Add a function to image_demo.py   that takes an image as input and returns the grayscale copy of the image. 
To obtain a grayscale copy you need to replace the red, green and blue component of each pixel by the same value. That value equals the average of the components, i.e. (𝑟𝑒𝑑+𝑔𝑟𝑒𝑒𝑛+𝑏𝑙𝑢𝑒)/3.
Test your function on the image cap.gif.
'''
def makeGray(img):
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
            
            gray = (red+green+blue)//3

            #set the RGB components of the corresponding new image to
            #half the intensity of the old image
            p.setRed(gray)
            p.setGreen(gray)
            p.setBlue(gray)
    
            #set the pixel in the new image
            new_image.setPixel(col,row, p)

           
    return new_image

#Exercise 2
'''
Add a function to image_demo.py   that takes an image as input and returns image whose right half is a mirror image of
its left half. For the  cap.gif  your function should return the following image:
'''
def screen_image(img):
    #create an empty image of the same size
    new_image = image.EmptyImage(img.getWidth(),img.getHeight())
    
    half_width = img.getWidth()//2
    
    print(f'Width {img.getWidth()}, Height {img.getHeight()}')
    
    #for all pixels in the image img row by row, column by column
    for row in range(img.getHeight()):
        for col in range(half_width):
            
            #It was giving a error for being out of range, so I subtracted 1
            col_right = img.getWidth() - col -1
            
            #print(f'Right {col_right}, Left {col}')
           
            #get the pixel
            p_left = img.getPixel(col, row)
            p_right = img.getPixel(col_right, row)

            #get RGB components of the pixel
            red = p_left.getRed()
            green = p_left.getGreen()
            blue = p_left.getBlue()
            
            #set the RGB components of the corresponding new image to
            #half the intensity of the old image
            p_right.setRed(red)
            p_right.setGreen(green)
            p_right.setBlue(blue)
    
            #set the pixel in the new image
            new_image.setPixel(col,row, p_left)
            new_image.setPixel(col_right,row, p_right)

    return new_image

#Exercise 3
'''
School photos, weather reports and action movies all make use of technique
called “chroma key compositing”, but better known as “green screen”
(https://en.wikipedia.org/wiki/Chroma_key). The idea is to use a solid colour
background for a scene that can be easily filtered out and replaced with a
different background image, leaving the foreground scene (usually a person or
character) in front.
'''

def fill_background(img, background):
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
            
            #Red<=1, Green>=254, Blue<=1

            #set the RGB components of the corresponding new image to
            #half the intensity of the old image
            
            if red <= 1 and green >= 254 and blue <= 1:
                p_back = background.getPixel(col, row)
                red_back = p_back.getRed()
                green_back = p_back.getGreen()
                blue_back = p_back.getBlue()
                p.setRed(red_back)
                p.setGreen(green_back)
                p.setBlue(blue_back)
        
            #set the pixel in the new image
            new_image.setPixel(col,row, p)

           
    return new_image
     
def main():
    IMAGE_FILE = 'ImageProcessing\cap.gif'
    
    original_img = image.Image(IMAGE_FILE)
    win1 = image.ImageWin(original_img.getWidth(), original_img.getHeight())
    original_img.draw(win1)
    
    # Create a transformed copy of the image and display it    
    
#     transformed_img = makeDarker(original_img)
#     win2 = image.ImageWin(transformed_img.getWidth(), transformed_img.getHeight())
#     transformed_img.draw(win2)               
    
    #Exercise 1
    
#     transformed_img = makeGray(original_img)
#     win2 = image.ImageWin(transformed_img.getWidth(), transformed_img.getHeight())
#     transformed_img.draw(win2)
#     

    #Exercise 2\
    
#     transformed_img = screen_image(original_img)
#     win2 = image.ImageWin(transformed_img.getWidth(), transformed_img.getHeight())
#     transformed_img.draw(win2)
    #Exercise 3\
#     IMAGE_FILE = 'ImageProcessing\minion-greenscreen.gif'
#     BACKGROUND_FILE = 'ImageProcessing\cap.gif'
#     
#     original_img = image.Image(IMAGE_FILE)
#     background_img = image.Image(BACKGROUND_FILE)
#     transformed_img = fill_background(original_img, background_img)
#     win2 = image.ImageWin(transformed_img.getWidth(), transformed_img.getHeight())
#     transformed_img.draw(win2)

    #With Greta
    
    IMAGE_FILE = 'ImageProcessing\greta.gif'
    BACKGROUND_FILE = 'ImageProcessing\wedgemont-glacier.gif'
    
    original_img = image.Image(IMAGE_FILE)
    background_img = image.Image(BACKGROUND_FILE)
    transformed_img = fill_background(original_img, background_img)
    win2 = image.ImageWin(transformed_img.getWidth(), transformed_img.getHeight())
    transformed_img.draw(win2)
    
    
main()
