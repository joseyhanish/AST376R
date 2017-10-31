# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 13:06:41 2017

@author: joskh
"""

from astropy.io import fits
import matplotlib.pyplot as plt
from scipy.signal import convolve
import numpy as np
from astropy.convolution import Box2DKernel

def make_gaussian(size, fwhm = 3, center=None):
    """ Make a square gaussian kernel.

    size is the length of a side of the square
    fwhm is full-width-half-maximum, which
    can be thought of as an effective radius.
    """

    x = np.arange(0, size, 1, float)
    y = x[:,np.newaxis]

    if center is None:
        x0 = y0 = size // 2
    else:
        x0 = center[0]
        y0 = center[1]

    z = np.exp(-4*np.log(2) * ((x-x0)**2 + (y-y0)**2) / fwhm**2)
    return z/np.sum(z)

#def box_kernel(size, box_width, center=None):
#    """
#    Make a kernel shaped like a box.
#    """
#    x = np.arange(0, size, 1, float)
#    y = x[:,np.newaxis]
#    
#    if center is None:
#        x0 = y0 = size // 2
#    else:
#        x0 = center[0]
#        y0 = center[1]
    
    
    

if __name__ == '__main__':

    # Read in the data
    file_loc = r'C:\Users\joskh\Documents\2017Fall\ast376r\MAST_2017-10-26T1243\MAST_2017-10-26T1243\HST\OCHZ03DWQ\ochz03dwq_flt.fits'
                    
    hdu_list = fits.open(file_loc)
    data = hdu_list['SCI'].data
    
    # Plot the original data
    plt.figure(figsize=(20,20))
    plt.imshow(data, origin='lower', cmap='gray')
    plt.text(100,1000,'Original Data')
    plt.show()
    
    # Convolve the data with a large box and subtract it from the original 
    # data to remove large-scale features. Then, convolve the result with a 
    # small box.
    large_box_size = 100
    small_box_size = 2
    
    convolved_data = convolve(data, Box2DKernel(large_box_size), mode='same')
#    plt.figure(figsize=(20,20))
#    plt.imshow(convolved_data, origin='lower', cmap='gray')
#    plt.text(100,1000,'Convolved Data with a large box')
#    plt.show()
    
    sub_data = data - convolved_data
#    plt.figure(figsize=(20,20))
#    plt.imshow(sub_data, origin='lower', cmap='gray')
#    plt.text(100,1000,'Original Data - Convolved Data')
#    plt.show()
    
    smoothed_data = convolve(sub_data, Box2DKernel(small_box_size), mode='same')
    plt.figure(figsize=(20,20))
    plt.imshow(smoothed_data, origin='lower', cmap='gray')
    plt.text(100,1000,'Convolved with a small box')
    plt.arrow(320, 805, 50, 50, head_width=5, head_length=5, fc='k', ec='k')
    plt.savefig('europa.png')
    plt.show()
    
    plt.figure(figsize=(20,20))
    plt.imshow(smoothed_data, cmap='gray', vmin=-20, vmax=10)
    plt.ylim(800,1000)
    plt.xlim(300,500)
    plt.text(300,990,'Zoomed in on Europa')
    plt.arrow(320, 805, 50, 50, head_width=5, head_length=5, fc='k', ec='k')
    plt.savefig('europazoom.png')
    plt.show()
    
    