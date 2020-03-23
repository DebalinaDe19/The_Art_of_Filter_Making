import cv2
import matplotlib.pyplot as plt
im = cv2.imread('Varanasi.jpg')
edges = cv2.Canny(im,100,300)
plt.imshow(edges)
plt.show()