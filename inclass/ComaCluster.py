# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 12:59:36 2017

@author: jkh2597
"""

import numpy as np
import matplotlib.pyplot as plt


def load_velocities(fname):
    vels = []
    with open(fname) as data:
        for line in data.readlines():
            if not line.startswith('#'):
                vels.append(float(line.split('\t')[5]))
    return vels
    
def calculate_mass(sigma):
    """
    M = R * sigma^2 / G
    R = physical size of cluster
    sigma = standard dev
    G = gravitational constant = 4.3 * 10^-3 pc (km/s)^2 Msun^-1
    """
    # R = D * theta where theta is in rad
    # Unit of R will be pc
    R = 103 * (20*3.14/float(60*180)) * 10**6
    G = 4.3 * 10**-3
    M = R * sigma**2 / G
    return M
    
if __name__ == '__main__':
    velocities = load_velocities('ComaCluster.txt')

    # Calculate velocity dispersions
    stdev = np.std(velocities)
    try:
        # Astropy has issues
        from astropy.stats import biweight_midvariance
        biweight = biweight_midvariance(velocities)
    except:
        biweight = 'An astropy error occurred'

    # Plot the histogram and dispersion stats
    plt.figure()
    plt.hist(velocities)
    plt.text(3000, 100, 'stdev = {0}\nbiweight = {1}'.format(stdev, biweight))
    plt.title('Histogram of Velocities in the Coma Cluster')
    plt.xlabel('Velocity (km/s)')
#    plt.savefig('ComaClusterHist2.pdf')
    plt.show()
    
    # Calculate the mass of the Coma Cluster
    print calculate_mass(stdev)
    # Result: 1.8e+14 Msun
    
