# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 10:46:40 2017

@author: jkh2597
"""

import cosmolopy.distance as cosmo
import numpy as np

def mass(theta, dl, ds, dls, c=3*(10**8), G=4.3*(10**-3)):
    """
    theta in units of rad
    dmin in units of ???
    dl, ds, dls in units of Mpc    
    c in units of m/s
    G in units of m^2 Mpc Msun^-1 s^-2    
    """
    return theta**2 * ((c**2)/(4*G)) * (dl * ds / dls)
    
if __name__ == '__main__':
    
    theta = [np.radians(v/(60.*60.)) for v in [1.20, 1.50]]
    zlens = 0.222
    zring = 0.609 # of the inner ring
    params = {'omega_M_0' : 0.3, 'omega_lambda_0' : 0.7, 'h' : 0.72}
    params = cosmo.set_omega_k_0(params)
       
    dl = cosmo.angular_diameter_distance(zlens, **params)
    ds = cosmo.angular_diameter_distance(zring, **params)
    dls = cosmo.angular_diameter_distance(zring, zlens, **params)[0]
    
    print('DL = {0}\nDS = {1}\nDLS = {2}'.format(dl, ds, dls))
    
    for th in theta:
        m = mass(th, dl, ds, dls)    
        print('Mlens = {0}'.format(m))