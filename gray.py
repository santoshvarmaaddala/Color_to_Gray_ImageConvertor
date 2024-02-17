import cv2 as c
#In imread func u declare the photo name or path to be convert
img = c.imread(r"C:\Users\KITS\Pictures\virat.jpg")
#Below line can be convert photo to Gray
#If you want to Convert it into another color then choose another attribute
gry = c.cvtColor(img,c.COLOR_BGR2GRAY)
#In double quotes you have to give a name for converted image
c.imwrite("gray.jpg",gry)
