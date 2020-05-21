# -*- coding: utf-8 -*-
import math
import rospy
import time
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
import numpy as np

from pyzbar import pyzbar


image_pub = rospy.Publisher("/qr/debug_img",Image)

def most_frequent(arr):
    try:
        return max(set(arr), key = arr.count)
    except:
        return "none"

def waitDataQR(image):
    out_img = image.copy()
    barcodeData = []
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    barcodes = pyzbar.decode(gray)
    for barcode in barcodes:
        (x, y, w, h) = barcode.rect
        barcodeData.append(barcode.data.decode("utf-8"))
        xc = x + w/2
        yc = y + h/2
        cv2.rectangle(out_img,(x, y), (x+w, y+h),(0,255,0),3)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(out_img,barcodeData[-1],(xc,yc), font, 0.5,(0,255,0),2,cv2.LINE_AA)
    return out_img, barcodeData


def img_clb(data):
    cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
    # out_img = cv_image.copy()
    out_img = waitDataQR(cv_image)
    image_pub.publish(bridge.cv2_to_imgmsg(out_img, "bgr8"))

bridge = CvBridge()
image_sub = rospy.Subscriber(
    "/main_camera/image_raw", Image, img_clb)

# ic = image_converter()



# res_pub = rospy.Publisher("/lane/res",LaneRes)


        

# cap = cv2.VideoCapture(0)
rospy.init_node('image_converter', anonymous=True)

rospy.spin()

# while cv2.waitKey(1) != 27:
#     ret, image = cap.read()
#     image, data = waitDataQR(image)
#     print(data)
#     cv2.imshow('image', image)