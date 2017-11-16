# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 12:39:22 2017

@author: joskh
"""

import numpy as np
import matplotlib.pyplot as plt

def box_kernel(size, box_width, center=None):
    """
    Make a kernel shaped like a box.
    """
    x = np.arange(0, size, 1, float)
    y = x[:,np.newaxis]
    
    if center is None:
        x0 = y0 = size // 2
    else:
        x0 = center[0]
        y0 = center[1]
    
    z = np.

plt.plot(box_kernel(100, 10)) 
