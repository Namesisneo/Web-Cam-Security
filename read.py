import cv2
# called opencv not cv2[don't install this library]
# Built on top of numpy
# It uses BGR --> Blue,Green,Red not rgb
array = cv2.imread("image.png")


print(array.shape)
print(array)
