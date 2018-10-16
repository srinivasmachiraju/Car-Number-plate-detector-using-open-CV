

import cv2
from skimage.io import imread
from PIL import Image
import pytesseract
# Loading the cascades
car_cascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')
car_image = imread("car.jpg")
gray = cv2.cvtColor(car_image, cv2.COLOR_BGR2GRAY)

# Doing some Face Recognition with the webcam
number_plates = car_cascade.detectMultiScale(
    gray,
    scaleFactor=1.01,
    minNeighbors=5,
    minSize=(10, 10),
)

print("Found {0} number_plates!".format(len(number_plates)))
min_x=0
min_y=0
max_x=0;
max_y=0
for (x, y, w, h) in number_plates:
    cv2.rectangle(car_image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    min_x=x
    min_y=y
    max_x=x+w
    max_y=y+h


#cutting the part of the picture where the model thought the number plate would be
if(number_plates>0):

	im = Image.open("car.jpg")
	#gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
	crop_rectangle = (min_x, min_y, max_x, max_y)
	cropped_im = im.crop(crop_rectangle)
	cropped_im.show()
	cropped_im.save('out.jpg')

	#trying to identify the text. 
	#Note: not yet completed

	cropped_im.save('out.jpg')
	text = pytesseract.image_to_string(Image.open('temp.jpg'))
	print(text)


#same code but we used gray scaled image


	image = cv2.imread('out.jpg')
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	filename = "{}.jpg".format("temp")
	cv2.imwrite(filename, gray)
	text = pytesseract.image_to_string(Image.open(filename))
	print(text)



