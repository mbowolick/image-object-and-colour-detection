import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

FILE = './src/media/image9.jpg'
SCALE_PERCENT = 20  # percent of original size

# Import test image
original = cv.imread(FILE, cv.IMREAD_UNCHANGED)
original_RGB = cv.cvtColor(original, cv.COLOR_BGR2RGB)

# Import image as greyscale
greyscale_img = cv.imread(FILE, cv.IMREAD_GRAYSCALE)

# resize image
width = int(greyscale_img.shape[1] * SCALE_PERCENT / 100)
height = int(greyscale_img.shape[0] * SCALE_PERCENT / 100)
dim = (width, height)

resized_original_img = cv.resize(
    original_RGB, dim, interpolation=cv.INTER_AREA)
resized_greyscale_img = cv.resize(
    greyscale_img, dim, interpolation=cv.INTER_AREA)

blur = cv.GaussianBlur(resized_greyscale_img, (5, 5), 0)
ret3, th3 = cv.threshold(blur, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)

# plot all the images and their histograms
replaced_background = []
object_pixels = []
for i in range(th3.shape[0]):
    replaced_background.append([])
    for j in range(th3.shape[1]):
        if(th3[i][j] == 0):
            replaced_background[i].append(resized_original_img[i][j])
            object_pixels.append(resized_original_img[i][j])
        else:
            # set background white
            replaced_background[i].append(np.array([255, 255, 255]))

a = np.asarray(object_pixels)
unique_colors, count = np.unique(a,  axis=0,  return_counts=True)
dom_color = unique_colors[count.argmax()]

swatch = np.full((150, 150, 3), np.array(dom_color))

# Row 1
plt.subplot(3, 2, 1)
plt.imshow(original_RGB, 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(3, 2, 2)
plt.hist(original_RGB.ravel(), 256, ec='k')
plt.title('Original Histogram'), plt.xlim([-5, 256])


# Row 2
plt.subplot(3, 2, 3)
plt.imshow(replaced_background, 'gray')
plt.title('Background Removed'), plt.xticks([]), plt.yticks([])

plt.subplot(3, 2, 4)
plt.hist(np.asarray(object_pixels).ravel(), 256, ec='k')
plt.title('Background Removed'), plt.xlim([-5, 256])

# Row 3
plt.subplot(3, 2, 5)
plt.imshow(swatch, 'gray')
plt.title('Dominant Color: rgb{}'.format(dom_color)
          ), plt.xticks([]), plt.yticks([])

plt.subplot(3, 2, 6)
plt.hist(swatch.ravel(), 256, ec='k')
plt.title('Dominant Colour Histogram'), plt.xlim([-5, 256])
plt.xlabel('Colour Scale: 0:black - 255:white')

plt.show()
