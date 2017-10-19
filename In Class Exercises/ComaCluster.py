# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 12:59:36 2017

@author: jkh2597
"""

import numpy as np
import matplotlib.pyplot as plt
#from astropy.stats import biweight_midvariance

def load_velocities(fname):
    vels = []
    with open(fname) as data:
        for line in data.readlines():
            if not line.startswith('#'):
                vels.append(float(line.split('\t')[5]))
    return vels
    
def calculate_mass(sigma):
    pass
    
if __name__ == '__main__':
    velocities = load_velocities('ComaCluster.txt')

    stdev = np.std(velocities)
#    biweight = biweight_midvariance(velocities)
    biweight = None

    plt.figure()
    plt.hist(velocities)
    plt.text(3000, 100, 'stdev = {0}\nbiweight = {1}'.format(stdev, biweight))
    plt.title('Histogram of Velocities in the Coma Cluster')
    plt.xlabel('Velocity (km/s)')
#    plt.savefig('ComaClusterHist2.pdf')
    plt.show()
    
    
    