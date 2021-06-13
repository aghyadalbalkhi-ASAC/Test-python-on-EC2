# get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from random import random


# print('length, aka number of rows:', len(img))
# print('height, aka number of columns in each row:', len(img[0]))
# print('depth, in this case the color channels', len(img[0][0]))
# print('Easier just to ask for the shape', img.shape)


def rgb2gray(rgb):
    gray = np.dot(rgb[...,:3], [0.299, 0.587, 0.114])
    plt.imshow(gray, cmap = plt.get_cmap('gray'))
    # plt.show()
    plt.savefig(r"student_scores.png", bbox_inches='tight', pad_inches=0)
    print("finish image")

def loadimag():
    print("load image")
    img = mpimg.imread('./onion.png')
    return img

