"""
Josey Hanish
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
    th: Hubble time, inverse of Hubble constant
    om: Density ratio of matter
    ok: Density ratio of something?
    ok: Density ration of cosmological constant
    """
    return th*integral(_integrand, 0, z, om, ok, ol)

if __name__ == '__main__':
    t_universe = 13.88
#    Hubble time = 72 km/(s Mpc)
# There are 3.2e19 km per Mpc
# There are 3.2e16 seconds per Gigayear
    th = (1./72.)*(3.2*10**19)/(3.2*10**16) #unit Gigayears
    print th
    om = 0.28
    ok = 0
    ol = 0.72
    x = np.linspace(0, 20)
    y = []
    for n in x:
        y.append(lookback_time(n, th, om, ok, ol))
    plt.figure()
    plt.plot(x,y)
    plt.title('Lookback Time vs Redshift')
    plt.xlabel('Redshift z')
    plt.ylabel('Lookback Time tL (Gigayears)')
    plt.text(2.5, 0.002, u'tL = tH \u222b dz / '
             u'[(1+z)(\u03a9M(1+z)^3+\u03a9K(1+z)+\u03a9\u039b)^1/2]')
    plt.savefig('LookbackvsRedshiftJoseyHanish.pdf')
    plt.show()