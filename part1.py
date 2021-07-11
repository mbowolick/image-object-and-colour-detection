import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

FILE = './src/media/image4.jpg'
SCALE_PERCENT = 20  # percent of original size

# Import test image
original = cv.imread(FILE, cv.IMREAD_UNCHANGED)
original_RGB = cv.cvtColor(original, cv.COLOR_BGR2RGB)

# Resize image
width = int(original_RGB.shape[1] * SCALE_PERCENT / 100)
height = int(original_RGB.shape[0] * SCALE_PERCENT / 100)
dim = (width, height)

# resize image
resized_img = cv.resize(original_RGB, dim, interpolation=cv.INTER_AREA)

# Row 1
plt.subplot(2, 2, 1)
plt.imshow(original_RGB, 'gray')
original_title = 'Original Dimensions : {}'.format(original_RGB.shape)
plt.xlabel('{} px'.format(original_RGB.shape[1])), plt.ylabel(
    '{} px'.format(original_RGB.shape[0]))
plt.title(original_title), plt.xticks([]), plt.yticks([])

plt.subplot(2, 2, 2)
plt.hist(original_RGB.ravel(), 256, ec='k')
original_hist_title = 'Original Histogram, Total Pixels = {}'.format(
    original_RGB.size)
plt.title(original_hist_title)
plt.ylabel('Number of Pixels'), plt.xlabel('Colour Scale: 0:black - 255:white')


# Row 2
plt.subplot(2, 2, 3)
plt.imshow(resized_img, 'gray')
resized_title = 'Resized Dimensions : {}'.format(resized_img.shape)
plt.xlabel('{} px'.format(resized_img.shape[1])), plt.ylabel(
    '{} px'.format(resized_img.shape[0]))
plt.title(resized_title), plt.xticks([]), plt.yticks([])

plt.subplot(2, 2, 4)
plt.hist(resized_img.ravel(), 256, ec='k')
resize_hist_title = 'Resized Histogram, Total Pixels = {}'.format(
    resized_img.size)
plt.title(resize_hist_title)
plt.ylabel('Number of Pixels'), plt.xlabel('Colour Scale: 0:black - 255:white')

plt.show()
