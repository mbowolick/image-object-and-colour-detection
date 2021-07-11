import cv2 as cv
import numpy as np
import time

start_time = time.time()

FILE = './src/media/image9.jpg'
SCALE_PERCENT = 10  # percent of original size

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
object_pixels = []
for i in range(th3.shape[0]):
    for j in range(th3.shape[1]):
        if(th3[i][j] == 0):
            object_pixels.append(resized_original_img[i][j])

a = np.asarray(object_pixels)
unique_colors, count = np.unique(a,  axis=0,  return_counts=True)
dom_color = unique_colors[count.argmax()]
hexcode = '{:02x}{:02x}{:02x}'.format(
    dom_color[0], dom_color[1], dom_color[2])

print('rgb', dom_color)
print('File: {} | {}'.format(FILE, hexcode))
print("--- %s s to process ---" % (time.time() - start_time))
