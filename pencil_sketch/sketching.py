import cv2

# read the image
#image = cv2.imread('doggy.jpg')
image = cv2.imread('wings.png')
# cv2.imshow('Misery', image)
# cv2.waitKey(0)

# create a new image by converting the original image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Gray Misery', gray_image)
# cv2.waitKey(0)

# invert the new grayscale image
inverted_image = 255 - gray_image
# cv2.imshow('Inverted', inverted_image)
# cv2.waitKey()

# blur the image by using the Gaussian Function in OpenCV
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)

# invert the blurred image, then convert the image to a pencil sketch
inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
# cv2.imshow('Sketch', pencil_sketch)
# cv2.waitKey(0)

# look at both the original image and the pencil sketch
cv2.imshow('original', image)
cv2.imshow('pencil sketch', pencil_sketch)
cv2.waitKey(0)

