#! /usr/bin/env python3
import rospy
import cv2
from sensor_msgs.msg import Image
# from std_msgs.msg import Int32
from cv_bridge import CvBridge, CvBridgeError

rospy.init_node("simple_python_CAMERA")

bridge = CvBridge()
cap = cv2.VideoCapture(0)
image_pub = rospy.Publisher("/main_camera/image_raw", Image)
# cap.set()
cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
# cap.set(cv2.CAP_PROP_FPS, 25)
rospy.sleep(0.5)
# r = rospy.Rate(40)
# cap.open(0)
print("TEST CODE")
ret, frame = cap.read()
print(ret)
while not rospy.is_shutdown():
    ret, frame = cap.read()
    print(ret)
    image_pub.publish(bridge.cv2_to_imgmsg(frame, "bgr8"))
    rospy.sleep(0.001)
cap.release()

