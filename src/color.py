# -*- coding: utf-8 -*-
import math
import time
import cv2
import numpy as np


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
    return red, yellow, blue, count, area_all

cap = cv2.VideoCapture(0)

while cv2.waitKey(1) != 27:
    ret, image = cap.read()
    red, yellow, blue, n, s = waitDataColor(image)
    print('Number of figures:', n, 'Area of all figures:', s)
    cv2.imshow('red', red)
    cv2.imshow('yellow', yellow)
    cv2.imshow('blue', blue)
    cv2.imshow('image', image)