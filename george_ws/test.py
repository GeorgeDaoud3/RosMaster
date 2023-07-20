import cv2 as cv
import sys
img = cv.imread("/home/jetson/yahboom.jpg")
img2= cv.imread("/home/jetson/ROS/X3plus/yahboomcar_ws/src/yahboomcar_visual/simple_qrcode/yahboom.jpg")
if img is None:
 sys.exit("Could not read the image.")
c=0;
while True:
	if c==0 :
		cv.imshow("Display window", img)
	else:
		cv.imshow("Display window2", img2)
	c=c+1
	if c==2:
		c=0;
	k = cv.waitKey(20)
	if k == ord("s"):
		cv.imwrite("starry_night.png", img)

