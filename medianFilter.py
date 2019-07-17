import cv2
import numpy as np
from matplotlib import pyplot as plt
image = cv2.imread('red_eyes2.jpg')
blur = median = cv2.medianBlur(img,5)
plt.subplot(121),plt.imshow(image),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()