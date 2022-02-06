import PIL
from PIL import Image
import numpy as np
import cv2
print("Welcome!\nUpload a picture of your plant to your computer to assess its ripeness and what actions you should take when growing it!\n")
x = input("Enter the name of the image file of your plant: ")
while x != "exit":
    #Names of files: red.jpg, red2.jpg, op.jpg, green.jpg, green2.jpg
    img = Image.open(x)
    img_rgb = img.convert("RGB")
    dom_col = img_rgb.getpixel((10,15))
    ins = ['You are in the Green Stage.\nWatering Level: Thorough and Daily.\nSunlight: Constant.\nSoil: Moist and Fertile.\nAdvice: Since indeterminate varieties continue growing, remove new branches and stems to direct resources to the fruit and main stems.' , 
     'You are now in the Pink-Orange Stage.\nWatering Level: Thrice Daily.\nSunlight: Constant.\nSoil: Moist and Fertile.\nAdvice: The more water you give them the juicier the tomato.' , 'Congratulations! You are now in the Red Stage. Your tomatoes are now fully ripe for the picking!' ]

    stage1 = [(10, 63, 6), (78, 99, 58), (154,205,50), (85,107,47), (107,142,35), (124,252,0), (127,255,0), (173,255,47), (50,205,50), (144,238,144), (60,179,113)] # list of green shades in rgb

    stage2 = [(237, 154, 100), (205,92,92), (240,128,128), (233,150,122), (250,128,114), (255,160,122)] # list of pink shades in rgb

    stage3 = [(109, 11, 2), (144, 0, 2), (128,0,0), (139,0,0), (165,42,42), (178,34,34), (220,20,60), (255,99,71)] # list of red shades in rgb
    print("\n",dom_col, "This is to show the RGB value to show how it works\n")
    if dom_col in stage1:
        print(ins[0])
    if dom_col in stage2:
        print(ins[1])
    if dom_col in stage3:
        print(ins[2])
    x = input("\nEnter the name of the image file of your plant: ")
print("Now you know how to grow!")
