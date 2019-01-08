"""
（1）检测出图像中的每一种形状的轮廓
（2）计算轮廓的中心——也叫形心。
转换成灰度图；
滤波以减少高频噪声，使轮廓检测更加精确；
图像二值化。边缘检测和阈值化经常被用于此过程，本教程采用阈值化。
"""

import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
#--image 参数: 磁盘中待处理图像的路径
ap.add_argument("-i","--image",required=True,help="path to the input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#5×5 内核的高斯平滑
blurred = cv2.GaussianBlur(gray,(5,5),0)
#阈值化
thresh = cv2.threshold(blurred,60,255,cv2.THRESH_BINARY)[1]

#使用轮廓检测去定位这些白色区域
#返回图像上每一个白块对应的边界点集合（即轮廓）
cnts = cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]

#处理每一条轮廓
for c in cnts:
    #计算轮廓区域图像的矩
    M = cv2.moments(c)
    #计算轮廓的中心
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    #在形状的中心 (cX, cY) 处绘制一个白色的小圆
    cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
    cv2.circle(image, (cX, cY), 7, (255, 255, 255), -1)
    cv2.putText(image, "center", (cX - 20, cY - 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
cv2.imshow("Image", image)
cv2.waitKey(0)