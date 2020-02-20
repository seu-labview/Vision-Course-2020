import cv2
jpgpath = "C:/Users/hp/Desktop/Iron Man.jpg"
jpg = cv2.imread(jpgpath)
cv2.imshow("Image",jpg)
cv2.waitKey(0)
jpggray = cv2.cvtColor(jpg,cv2.COLOR_BGR2GRAY)
cv2.imshow("Image",jpggray)
cv2.waitKey(0)