# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 13:32:34 2017

@author: jkh2597
"""

from astropy.io import fits


def load(filename):
    header = fits.open(filename)
    header.info()
    return header
    
    
if __name__ == '__main__':
    my_fits = load('ua1l2901m_drz.fits')
    my_image = my_fits['SCI'].data
    print(type(my_image))
    print(my_image.shape)
    