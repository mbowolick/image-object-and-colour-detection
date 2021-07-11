import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

FILE = './src/media/image8.jpg'

# Import test image
original = cv.imread(FILE, cv.IMREAD_UNCHANGED)

# OpenCV uses BGR as its default colour order for images, matplotlib uses RGB.
# When you display an image loaded with OpenCv in matplotlib the channels will be back to front.
original_RGB = cv.cvtColor(original, cv.COLOR_BGR2RGB)

# Import image as greyscale
greyscale_img = cv.imread(FILE, cv.IMREAD_GRAYSCALE)
# global thresholding
# ret1, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
# # Otsu's thresholding
# ret2, th2 = cv.threshold(img, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
# Otsu's thresholding after Gaussian filtering
blur = cv.GaussianBlur(greyscale_img, (5, 5), 0)
ret3, th3 = cv.threshold(blur, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)

# plot all the images and their histograms
titles = [
    'Original',
    'Original Histogram',
    'Gaussian filtered Image',
    'Gaussian Histogram',
    "Otsu's Thresholding",
    "Otsu's Thresh Histogram"]

# Row 1
plt.subplot(3, 2, 1)
plt.imshow(original_RGB, 'gray')
plt.title(titles[0]), plt.xticks([]), plt.yticks([])

# plt.subplot(3, 2, 2)
# plt.imshow(greyscale_img, 'gray')
# plt.title(titles[1]), plt.xticks([]), plt.yticks([])
plt.subplot(3, 2, 2)
plt.hist(original_RGB.ravel(), 256, ec='k')
plt.ylim(0, 100000)
plt.title(titles[1])

# Row 2
plt.subplot(3, 2, 3)
plt.imshow(blur, 'gray')
plt.title(titles[2]), plt.xticks([]), plt.yticks([])

plt.subplot(3, 2, 4)
plt.hist(blur.ravel(), 256, ec='k')
plt.ylim(0, 100000)
plt.title(titles[3])

# Row 3
plt.subplot(3, 2, 5)
plt.imshow(th3, 'gray')
plt.title(titles[4]), plt.xticks([]), plt.yticks([])

plt.subplot(3, 2, 6)
plt.hist(th3.ravel(), 256, ec='k')
plt.ylim(0, 100000)
plt.title(titles[5])

plt.show()
