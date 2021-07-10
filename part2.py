import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

file = './src/media/image1.jpg'

# Import test image
original = cv.imread(file, cv.IMREAD_UNCHANGED)
original_RGB = cv.cvtColor(original, cv.COLOR_BGR2RGB)

# Import image as greyscale
greyscale_img = cv.imread(file, cv.IMREAD_GRAYSCALE)
blur = cv.GaussianBlur(greyscale_img, (5, 5), 0)
ret3, th3 = cv.threshold(blur, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)

# plot all the images and their histograms
new_original = np.empty(th3.shape, dtype=int)
for i in range(th3.shape[0]):
    for j in range(th3.shape[1]):
        if(th3[i][j] == 0):
            new_original[i][j] = original_RGB[i][j]
        else:
            # set background white
            # TODO: Fix ValueError
            new_original[i][j] = np.array([255, 255, 255])


# Row 1
plt.subplot(2, 2, 1)
plt.imshow(original_RGB, 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(2, 2, 2)
plt.hist(original_RGB.ravel(), 256, ec='k')
plt.title('Original Histogram'), plt.ylim(0, 100000)


# Row 2
plt.subplot(2, 2, 3)
plt.imshow(new_original, 'gray')
plt.title('Background Stripped'), plt.xticks([]), plt.yticks([])

plt.subplot(2, 2, 4)
plt.hist(new_original.ravel(), 256, ec='k')
plt.title('Stripped Background Hist'), plt.ylim(0, 100000)

plt.show()
