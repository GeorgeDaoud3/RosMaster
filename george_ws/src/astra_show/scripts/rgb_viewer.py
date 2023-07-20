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
	#print("put");
    def imageCallback(self, msg):
        #print(msg.width*msg.height*2)
	#print(msg.step)
        #print(msg.width)	
	#print(help(msg.deserialize_numpy))
        parsed_data=np.frombuffer(msg.data, dtype='u1').reshape((msg.height,msg.width,3))
        #parsed_data =np.array(parsed_data / 256, dtype=np.uint8)
        #print(parsed_data.shape)
	#print(parsed_data)
        #print(rospy.get_param("/camera/camera_rgb/frame_rate"))
	#img = cv2.imread("/home/jetson/yahboom.jpg")
        #print(parsed_data.shape)
	
        cv2.imshow("display", parsed_data)
	k = cv2.waitKey(50)
    
    def __init__(self):
        self.c=0;

        print('I"m here');
	#cv2.startWindowThread()
        #cv2.namedWindow("windows display", cv2.WINDOW_NORMAL)
        rospy.init_node('RGB_Viewer', anonymous = True) # ROS node initialization
       # print(rospy.get_param("camera/camera_rgb/frame_rate"))
	rospy.Subscriber("/camera/rgb/image_rect_color", sensor_msgs.msg.Image, self.imageCallback)
        #rospy.set_param("/camera/camera_rgb/frame_rate",10)
	#/camera/rgb/image_rect_color
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

