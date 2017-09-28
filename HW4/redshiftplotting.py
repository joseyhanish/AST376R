"""
This script will plot redshift vs lookback time according to Hogg Eqn 30, 14
"""

import scipy.integrate
import matplotlib.pyplot as plt
import numpy as np


def integral(func, x0, x1, *args):
    """
    Args:
        func (callable): mathematical function to integrate
        x0 (number): lower limit of integration
        x1 (number): upper limit of integration
    """
    return scipy.integrate.quad(func, x0, x1, args)[0]

def _integrand(z, om, ok, ol):
    return ((1+z)*(((om*(1+z)**3)+(ok*(1+z)**2)+ol))**0.5)**(-1)

def lookback_time(z, th, om, ok, ol):
    """
    z: redshift
    th: Age of universe
    om: Density ratio of matter
    ok: Density ratio of something?
    ok: Density ration of cosmological constant
    """
    return th*integral(_integrand, 0, z, om, ok, ol)

if __name__ == '__main__':
    th=13.88
    om = 0.28
    ok = 0
    ol = 0.72
    x = np.linspace(0, 20)
    y = []
    for n in x:
        y.append(lookback_time(n, th, om, ok, ol))
    plt.figure()
    plt.plot(x,y)
    plt.xlabel('Redshift z')
    plt.ylabel('Lookback Time tL')
#    plt.text(u'tL = tH\u222b', 5, 12)
    plt.show()
    print u'u\8747'