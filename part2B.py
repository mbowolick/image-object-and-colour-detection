import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

FILE = './src/media/image4.jpg'
SCALE_PERCENT = 20  # percent of original size

# Import test image
original = cv.imread(FILE, cv.IMREAD_UNCHANGED)
original_RGB = cv.cvtColor(original, cv.COLOR_BGR2RGB)

# Import image as greyscale
greyscale_img = cv.imread(FILE, cv.IMREAD_GRAYSCALE)

width = int(greyscale_img.shape[1] * SCALE_PERCENT / 100)
height = int(greyscale_img.shape[0] * SCALE_PERCENT / 100)
dim = (width, height)

# resize image
resized_original_img = cv.resize(
    original_RGB, dim, interpolation=cv.INTER_AREA)
resized_greyscale_img = cv.resize(
    greyscale_img, dim, interpolation=cv.INTER_AREA)

blur = cv.GaussianBlur(resized_greyscale_img, (5, 5), 0)
ret3, th3 = cv.threshold(blur, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)

# plot all the images and their histograms
new_original = []
for i in range(th3.shape[0]):
    new_original.append([])
    for j in range(th3.shape[1]):
        if(th3[i][j] == 0):
            new_original[i].append(resized_original_img[i][j])
        else:
            # set background white
            new_original[i].append(np.array([255, 255, 255]))


# Row 1
plt.subplot(2, 2, 1)
plt.imshow(resized_original_img, 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(2, 2, 2)
plt.hist(resized_original_img.ravel(), 256, ec='k')
plt.title('Original Histogram')
plt.ylabel('Number of Pixels'), plt.xlabel('Colour Scale: 0:black - 255:white')


# Row 2
plt.subplot(2, 2, 3)
plt.imshow(new_original, 'gray')
plt.title('Background Stripped'), plt.xticks([]), plt.yticks([])

plt.subplot(2, 2, 4)
plt.hist(np.asarray(new_original).ravel(), 256, ec='k')
plt.title('Replaced Background')
plt.ylabel('Number of Pixels'), plt.xlabel('Colour Scale: 0:black - 255:white')

plt.show()
