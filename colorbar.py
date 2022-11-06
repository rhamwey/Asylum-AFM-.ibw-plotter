# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 14:52:39 2022

@author: raham
"""

import numpy as np
import skimage.color
import skimage.io
from matplotlib.colors import LinearSegmentedColormap



#%% get colors
def mud_cmap():
    # get image for analysis
    path = r"C:\Users\raham\Google Drive\work\Lab\Scripts\AFM\AFM reader\asylum_colorbar.PNG"
    

    # a 3d array of RGBA values for every pixel
    image_read = skimage.io.imread(fname=path)
    # dimensions of image_read
    size = np.shape(image_read)

    RGB_list = []
    for y_pixel in range(size[0]):
        RGB = image_read[y_pixel,0,:][0:3]/256
        
        RGB_list.append(RGB)
    
    # have to flip RGB_list for proper order
    RGB_list.reverse()
    mud = LinearSegmentedColormap.from_list("", RGB_list)
    
    return mud

