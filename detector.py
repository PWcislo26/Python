import cv2
from glob import glob
import imutils


def get_images() -> list:
    """create a list of image paths"""
    images = glob('images/*.jpg') + glob('images/*.jpeg') + glob('images/*.png')
    return images


def detection(image):
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    image = cv2.imread(image)

    image = imutils.resize(image, width=640, height=480)  # resizing image
    # using hog trained network to help detect people in images
    (persons_detected, _) = hog.detectMultiScale(image, winStride=(4, 6), padding=(8, 8))
    print(len(persons_detected))
    for x, y, w, h in persons_detected:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # adding number of persons detected text to the image
    cv2.putText(
        img=image,
        text='persons: ' + str(len(persons_detected)),
        org=(30, 30),
        fontFace=cv2.FONT_HERSHEY_TRIPLEX,
        fontScale=1,
        color=(0, 0, 255),
        thickness=1
    )

    cv2.imshow('image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


print(get_images())
