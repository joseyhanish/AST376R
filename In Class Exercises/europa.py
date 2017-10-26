# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 13:06:41 2017

@author: joskh
"""

from astropy.io import fits
import matplotlib.pyplot as plt
from scipy.signal import convolve
import numpy as np

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

if __name__ == '__main__':

    file_loc = r'C:\Users\joskh\Documents\2017Fall\ast376r\MAST_2017-10-26T1243\MAST_2017-10-26T1243\HST\OCHZ03DWQ\ochz03dwq_flt.fits'
                    
    hdu_list = fits.open(file_loc)
#    hdu_list.info()
    data = hdu_list['SCI'].data
    
#    plt.figure()
#    plt.imshow(data, origin='lower')
#    plt.show()
    
    convolved_data = convolve(data, make_gaussian(np.shape(data)[0], fwhm=200), 
                              mode='same')
#    plt.figure()
#    plt.imshow(convolved_data, origin='lower')
#    plt.show()
    
    sub_data = data - convolved_data
    plt.figure(figsize=(20,20))
    plt.imshow(sub_data, origin='lower', cmap='gray')
    plt.show()
    
    