import cv2
import os
import numpy as np
import matplotlib.pyplot as plt


def semanticLabeling():
    dir = './data'
    img = cv2.imread(os.path.join(dir, 'download.png'))

#    cv2.imshow('Image', img)
#    cv2.waitKey(0)
    
    _ , contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    cv2.drawContours(img, contours, -1, (0,255,0), 3)

    cv2.imshow('Image', img)
    cv2.waitKey(0)

if __name__ == "__main__":
    
    semanticLabeling()
