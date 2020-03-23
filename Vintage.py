import cv2
import numpy as np
from matplotlib import pyplot as plt
im = cv2.imread('Taxi.jpg')
rows, cols = im.shape[:2]
# Create a Gaussian filter
kernel_x = cv2.getGaussianKernel(cols,200)
kernel_y = cv2.getGaussianKernel(rows,200)
kernel = kernel_y * kernel_x.T
filter = 255 * kernel / np.linalg.norm(kernel)
vintage_im = np.copy(im)
# for each channel in the input image, we will apply the above filter
for i in range(3):
    vintage_im[:,:,i] = vintage_im[:,:,i] * filter
plt.imshow(vintage_im)
plt.show()