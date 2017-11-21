# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 13:32:34 2017

@author: jkh2597
"""

from astropy.io import fits
import matplotlib.pyplot as plt
import os
from scipy.ndimage.interpolation import shift
import numpy as np


def load(filename):
    """header (string)"""
    header = fits.open(filename)
#    header.info()
    return header
    
def show_all(images, vmin=0, vmax=0.3, xlim=None, ylim=None):
    """
    images (list): list of np arrays
    xlim (tuple): min, max
    ylim (tuple): min, max
    """
    for my_image in images:
        plt.figure()
        plt.imshow(my_image, cmap='gray', vmin = vmin, vmax = vmax)
        if xlim:
            plt.xlim(xlim)
        if ylim:
            plt.ylim(ylim)
#    plt.show()
        
    
if __name__ == '__main__':
    
    data_path = 'fits'

    images = [] 
    show = False
    for filename in os.listdir(data_path):
        print filename
        my_fits = load(os.path.join(data_path,filename))
        my_image = my_fits['SCI'].data
        images.append(my_image)       
    if show == True:
        show_all(images)
    
    print '{0} images loaded'.format(len(images))
    
    # Recall numpy coordinates are y, x
    shifts = [(0,0),(-2,-5),(-7,-8),(-5,-3)]   
    shifted_images = []
    show = False
    for i, img in enumerate(images):       
        shifted_images.append(shift(img, shifts[i]))
    if show == True:
        show_all(shifted_images, xlim=(400,600), ylim=(500,700))

    combined_image = np.median(np.array(shifted_images), axis=0)  
    
    show_all([combined_image])
    
    fits.writeto('reduced_ring.fits', combined_image, overwrite=True)
    
    plt.show()
    
    
    
# fits.writeto()