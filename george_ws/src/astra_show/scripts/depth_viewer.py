#!/usr/bin/env python
#use the default python compiler
# -*- coding: utf-8 -*-
# This routine will publish turtle1/cmd_vel topic, message type geometry_msgs::Twist

import rospy
import sensor_msgs.msg
import cv2
import threading
import numpy as np

class Stero_show():
    def queue_stereo(self, lmsg, rmsg):
        q_stereo.put((lmsg, rmsg))
	print("put");
    def imageCallback(self, msg):
        #print(msg.width*msg.height*2)
	#print(msg.step)
        #print(msg.width)	
	#print(help(msg.deserialize_numpy))
        parsed_data=np.frombuffer(msg.data, dtype='>u2').reshape((msg.height,msg.width))
        parsed_data =np.array(parsed_data / 256, dtype=np.uint8)
        #print(parsed_data.shape)
	#print(parsed_data)
	img = cv2.imread("/home/jetson/yahboom.jpg")
        #print(parsed_data.shape)
        cv2.imshow("display", parsed_data)
	k = cv2.waitKey(20)
    
    def __init__(self):
        self.c=0;
        print('I"m here');
	#cv2.startWindowThread()
        #cv2.namedWindow("windows display", cv2.WINDOW_NORMAL)
        rospy.init_node('Depth_Viewer', anonymous = True) # ROS node initialization
	rospy.Subscriber("/camera/depth_registered/image", sensor_msgs.msg.Image, self.imageCallback)

	rospy.spin() #

# the main process
if  __name__  ==  '__main__' :
    print(1)
    stero_show = Stero_show()
    try :
        # call the node's logic implementation function
	stero_show = Stero_show()
    except  rospy.ROSInterruptException :
        pass

