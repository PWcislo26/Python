import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img = cv2.imread('images/sample_text.jfif')
img1 = cv2.imread('images/sample_text2.png')
img2 = cv2.imread('images/sample_text3.png')
img3 = cv2.imread('images/sample_text4.jpg')


def read_from_image(img):
    return pytesseract.image_to_string(img)


print(read_from_image(img))
print(read_from_image(img1))
print(read_from_image(img2))
print(read_from_image(img3))
