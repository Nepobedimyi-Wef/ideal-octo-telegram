import cv2
import pytesseract

image = cv2.imread('maxresdefault.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

text = pytesseract.image_to_string(blurred_image)
print(text)
