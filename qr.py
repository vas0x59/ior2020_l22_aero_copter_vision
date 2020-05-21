# -*- coding: utf-8 -*-
import math
import time
import cv2
import numpy as np

from pyzbar import pyzbar
        
def most_frequent(arr):
    try:
        return max(set(arr), key = arr.count)
    except:
        return "none"

def waitDataQR(image):
    barcodeData = []
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    barcodes = pyzbar.decode(gray)
    for barcode in barcodes:
        (x, y, w, h) = barcode.rect
        barcodeData.append(barcode.data.decode("utf-8"))
        xc = x + w/2
        yc = y + h/2
        cv2.rectangle(image,(x, y), (x+w, y+h),(0,255,0),3)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(image,barcodeData[-1],(xc,yc), font, 0.5,(0,255,0),2,cv2.LINE_AA)
    return image, barcodeData

cap = cv2.VideoCapture(0)

while cv2.waitKey(1) != 27:
    ret, image = cap.read()
    image, data = waitDataQR(image)
    print(data)
    cv2.imshow('image', image)