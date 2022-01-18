import pytesseract
import cv2
from cv2 import ADAPTIVE_THRESH_GAUSSIAN_C

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img = cv2.imread('images/captcha3.png')
img1 = cv2.imread('images/captcha7.jpg')
img2 = cv2.imread('images/noise.jpg')



def read_from_image(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    filtered = cv2.adaptiveThreshold(cv2.GaussianBlur(gray, (5, 5), 0), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

    cv2.imshow('',filtered)
    cv2.waitKey(0)
    return pytesseract.image_to_string(filtered)



print(read_from_image(img2))
