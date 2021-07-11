# image-object-and-colour-detection

A Python project to explore image processing: object and colour detection

## Step 1 - Import your image and resize

Using the `cv.imread()`, import the images in the original and greyscale formats:

```python
original_img = cv.imread('./src/media/image1.jpg', cv.IMREAD_UNCHANGED)
greyscale_img = cv.imread('./src/media/image1.jpg', cv.IMREAD_GRAYSCALE)
```

Note, OpenCV uses BGR as its default colour order for images, matplotlib uses RGB. When you display an image loaded with OpenCv in matplotlib the channels will be back to front:

```python
original_RGB = cv.cvtColor(original, cv.COLOR_BGR2RGB)
```

For optimising the processing time the image will be resize. Retaining quality is not needed for the goal of mapping out colours.

For resizing, the default scale for resize has been set to 20%. Resize is achieved through cv.resize(ORIGINAL_IMG, NEW_DIMENSIONS)

![Import and Resize](./src/readme-imgs/part-1-import-and-resize.png)

## Step 2 - Isolate the subject and filter background

To isolate the subject and filter out the background CV Image Threasholding should be leveraged.

Image Threasholding applies fixed-level thresholding to a multiple-channel array. The function is typically used to get a bi-level (binary) image out of a grayscale image ( compare could be also used for this purpose) or for removing a noise, that is, filtering out pixels with too small or too large values. There are several types of thresholding supported by the function, however, the current project will focus on 'Otsu's thresholding'.

For more info relating to all other types, see the OpenCV docs page:
https://docs.opencv.org/4.5.2/d7/d4d/tutorial_py_thresholding.html

### 2A) Build the Bimodal Distribution Map

Let's start with what is a bimodal image? This, also can be aligned to a bimodal distribution (two peaks). Data distributions in statistics can have one peak, or they can have several peaks. The type of distribution you might be familiar with seeing is the normal distribution, or bell curve, which has one peak. The bimodal distribution has two peaks.

Therefore, using a test image of your chosing, the first goal should be to identify the bimodal model and then separate the primary peak from the secondary peak. Consider an image with only two distinct image values (bimodal image), where the histogram would only consist of two peaks. A good threshold would be in the middle of those two values. Similarly, Otsu's method determines an optimal global threshold value from the image histogram.

![Bimodal Image Processing](./src/readme-imgs/part-2A-original-gaussian-otsus-histogram.png)

### 2B) Filter backgound

Using the identified bimodal distribution, and create the new image.
Where black (0) keep the original image pixel, where white (0) replace with white.

```python
new_original = []
for i in range(th3.shape[0]):
    new_original.append([])
    for j in range(th3.shape[1]):
        if(th3[i][j] == 0):
            new_original[i].append(original_RGB[i][j])
        else:
            new_original[i].append(np.array([255, 255, 255]))  #<-- new background
```

In the example below the grey background, becomes white in the bimodal distribution map which can be easily identified in the
![Replaced Background](./src/readme-imgs/part-2B-replace-background.png)

## Step 3 - Find the dominant RGB array of the isoloated object

Isolate only the object pixels and find the dominant RGB array:

```python
replaced_background = []
object_pixels = []    # <---- ISOLATED OBJECT
for i in range(th3.shape[0]):
    replaced_background.append([])
    for j in range(th3.shape[1]):
        if(th3[i][j] == 0):
            replaced_background[i].append(resized_original_img[i][j])
            object_pixels.append(resized_original_img[i][j])  # <---- ADD PIXELS
        else:
            replaced_background[i].append(np.array([255, 255, 255]))

```

From the `object_pixels`, convert the list to a Numpy Array:

```python
a = np.asarray(object_pixels)
```

And then, find the unique colours and return the colour with the highest count:

```python
colours, count = np.unique(a, axis=0, return_counts=True)
dom_color = colours[count.argmax()]
```

| Component  | Explained                          |
| ---------- | ---------------------------------- |
| `axis = 0` | to not flatten the colours array   |
| `argmax()` | returns the index of the max count |

![Dominant Color](./src/readme-imgs/part-3-dominant-colour.png)
