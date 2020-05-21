# -*- coding: utf-8 -*-
import math
import rospy
import time
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
import numpy as np

rospy.init_node('team_name_color_node', anonymous=True)

image_pub = rospy.Publisher("/color/debug_img",Image)
image_pub_red = rospy.Publisher("/color/debug_img_red",Image)
image_pub_green = rospy.Publisher("/color/debug_img_green",Image)
image_pub_yellow = rospy.Publisher("/color/debug_img_yellow",Image)
image_pub_blue = rospy.Publisher("/color/debug_img_blue",Image)

def most_frequent(arr):
    try:
        return max(set(arr), key = arr.count)
    except:
        return "none"

def waitDataColor(image):
    ratio = 1
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    lower_yellow    = np.array([10,  50,  80])
    upper_yellow    = np.array([35,  255, 255])
    lower_red       = np.array([170, 40,  40])
    upper_red       = np.array([255, 255, 255])
    lower_blue      = np.array([75,  80,  80])
    upper_blue      = np.array([130, 255, 255])
    
    b_m = cv2.inRange(hsv, lower_blue, upper_blue)
    r_m = cv2.inRange(hsv, lower_red, upper_red)
    y_m = cv2.inRange(hsv, lower_yellow, upper_yellow)

    thresh = cv2.threshold(b_m, 80, 255, cv2.THRESH_BINARY)[1]
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

    yellow  = cv2.bitwise_and(image, image, mask = y_m) 
    red     = cv2.bitwise_and(image, image, mask = r_m)
    blue    = cv2.bitwise_and(image, image, mask = b_m)
    
    count = 0
    area_all = 0

    for c in cnts:
        area = cv2.contourArea(c)
        if area < 150: continue
        M = cv2.moments(c)
        cX = int((M["m10"] / (M["m00"]+ 1e-7)) * ratio)
        cY = int((M["m01"] / (M["m00"]+ 1e-7)) * ratio)
        count += 1
        area_all += area
        c = c.astype("int")
        cv2.drawContours(blue, [c], -1, (0, 255, 0), 2)
    ret, image = cap.read()
    red, yellow, blue, n, s = waitDataColor(image)
    print('Number of figures:', n, 'Area of all figures:', s)
    cv2.imshow('red', red)
    cv2.imshow('yellow', yellow)
    cv2.imshow('blue', blue)
    cv2.imshow('image', image)
    return red, yellow, blue, count, area_all

def img_clb(data):
    cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
    

# cap = cv2.VideoCapture(0)
bridge = CvBridge()
image_sub = rospy.Subscriber(
    "/main_camera/image_raw", Image, img_clb)


rospy.spin()

# while cv2.waitKey(1) != 27:
#     ret, image = cap.read()
#     red, yellow, blue, n, s = waitDataColor(image)
#     print('Number of figures:', n, 'Area of all figures:', s)
#     cv2.imshow('red', red)
#     cv2.imshow('yellow', yellow)
#     cv2.imshow('blue', blue)
#     cv2.imshow('image', image)