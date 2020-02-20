import cv2 as cv

if __name__ == '__main__':
    src = cv.imread('E:\\picture.png')
    cv.imshow('picture', src)
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    cv.imshow('gray_picture', gray)
    cv.waitKey(0)
    cv.destroyAllWindows()