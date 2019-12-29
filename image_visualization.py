import numpy as np
import matplotlib.pyplot as plt
import cv2

class Formatter(object):
    def __init__(self, im):
        self.im = im
    def __call__(self, x, y):
        z = self.im.get_array()[int(y), int(x)]
        return 'x={:.01f}, y={:.01f}, z={:.01f}'.format(x, y, z)

data = cv2.imread('./data/a1.png')
name = 'img'
cv2.namedWindow(name, cv2.WINDOW_NORMAL)
cv2.imshow(name, data)
# cv2.resize('img', 1000, 1000)
cv2.waitKey(0)
cv2.destroyAllWindows()
#
#fig, ax = plt.subplots()
#im = ax.imshow(data, interpolation='none')
#ax.format_coord = Formatter(im)
#plt.show()
