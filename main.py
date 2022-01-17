from detector import *


def main():
    for image in get_images():
        detection(image)


if __name__ == "__main__":
    main()
