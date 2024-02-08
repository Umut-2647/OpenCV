import cv2
import numpy as np

img_filter=cv2.imread("filter.png")
img_bilateral=cv2.imread("bilateral.png")
img_median=cv2.imread("median.png")

blur=cv2.blur(img_filter,(11,11)) ##pozitif tek sayilar
blur2=cv2.GaussianBlur(img_filter,(11,11),cv2.BORDER_DEFAULT)
median_blur=cv2.medianBlur(img_median,9)
bilateral_blur=cv2.bilateralFilter(img_bilateral,9,95,95)




"""
cv2.imshow("Original",img_filter)
cv2.imshow("Blur",blur)
cv2.imshow("GaussianBlur",blur2)"""

"""
cv2.imshow("Original",img_median)
cv2.imshow("MedianBlur",median_blur)"""


cv2.imshow("Original",img_bilateral)
cv2.imshow("BilateralBlur",bilateral_blur)


cv2.waitKey(0)
cv2.destroyAllWindows()