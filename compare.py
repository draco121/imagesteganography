from skimage import measure
import matplotlib.pyplot as plt
import numpy as np
import cv2
from PIL import Image
print("=============================================1x1=====================")
image1 = cv2.imread("si/1/pic.jpg",0)
image2 = cv2.imread("si/1/modified.png",-1)

s = measure.compare_mse(image1,image2)
p = measure.compare_psnr(image1,image2)
print(p)
print(s)
print("======================================================================")
print("=============================================2x2=====================")
image1 = cv2.imread("si/2/pic.jpg",0)
image2 = cv2.imread("si/2/modified.png",-1)

s = measure.compare_mse(image1,image2)
p = measure.compare_psnr(image1,image2)
print(p)
print(s)
print("======================================================================")
print("=============================================3x3=====================")
image1 = cv2.imread("si/3/pic.jpg",0)
image2 = cv2.imread("si/3/modified.png",-1)

s = measure.compare_mse(image1,image2)
p = measure.compare_psnr(image1,image2)
print(p)
print(s)
print("======================================================================")
