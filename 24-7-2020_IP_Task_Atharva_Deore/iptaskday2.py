import cv2
import numpy as np
original = cv2.imread(r"C:\Users\sony\Desktop\Day 2\Task Image\yellow_flower.jpg")
res = cv2.resize(original, (400,300))
rgbl = np.array([0, 0, 172], np.uint8)
rgbh = np.array([255, 255, 255], np.uint8)
mask = cv2.inRange(res, rgbl, rgbh)
cv2.imshow('masked', mask)
kernel = np.ones((5,5),np.uint8)
blur = cv2.filter2D(res, -1, kernel)
avg = cv2.blur(res, (5, 5))
gaus_blur = cv2.GaussianBlur(res, (5, 5), 0)
median = cv2.medianBlur(res,5)
bilateral = cv2.bilateralFilter(res, 5, 111, 111)
cv2.imshow("original", res)
cv2.imshow("blurred", blur)
cv2.imshow("averaging", avg)
cv2.imshow("gaussian blur", gaus_blur)
cv2.imshow("median blur normal", median)
cv2.imshow("bilateral", bilateral)
res=cv2.ellipse(res,(190,230),(50,10),0,0,360,(203,192,255),3)
res=cv2.line(res,(140,230),(160,290),(203,192,255),3)
res=cv2.line(res,(240,230),(220,290),(203,192,255),3)
res=cv2.ellipse(res,(190,290),(30,5),0,180,360,(120,120,30),-1)
font=cv2.FONT_HERSHEY_COMPLEX
res=cv2.putText(res,'flower',(5,25),font,1,(255,255,255),2,cv2.LINE_AA)
cv2.imshow('name',res)
cv2.imwrite(r'C:\Users\sony\Desktop\Day 2\Task Image\original.jpg',original)
cv2.imwrite(r'C:\Users\sony\Desktop\Day 2\Task Image\mask.jpg',mask)
cv2.imwrite(r'C:\Users\sony\Desktop\Day 2\Task Image\blur.jpg',blur)
cv2.imwrite(r'C:\Users\sony\Desktop\Day 2\Task Image\avg.jpg',avg)
cv2.imwrite(r'C:\Users\sony\Desktop\Day 2\Task Image\gauss.jpg',gaus_blur)
cv2.imwrite(r'C:\Users\sony\Desktop\Day 2\Task Image\median.jpg',median)
cv2.imwrite(r'C:\Users\sony\Desktop\Day 2\Task Image\bilateral.jpg',bilateral)
cv2.imwrite(r'C:\Users\sony\Desktop\Day 2\Task Image\name.jpg',res)
cv2.waitKey(0)
cv2.destroyAllWindows()