
# coding: utf-8

# In[1]:

import numpy as np
from matplotlib import pyplot as plt
get_ipython().magic(u'matplotlib inline')

from scipy.optimize import curve_fit

import os


# In[2]:

class my_funcs(object):
    def __init__(self, freq, amp, phase, offset, linslope):
        self.freq = freq
        self.amp = amp
        self.phase = phase
        self.offset = offset
        self.linslope = linslope
        
    def my_sin(self, x):
        return np.sin(x * self.freq + self.phase) * self.amp + self.offset             + self.linslope*(x-2457400.)
        
    def chi_squared(self, point, comp_function):
        """return chi squared for a data point, compared to the 
        comparison function for that point"""
        x = ((point[1] - comp_function(point[0])) / 1)**2
        return x


# In[3]:

if os.path.isfile('proximacentaurirv.txt'):
    data = np.loadtxt('proximacentaurirv.txt')
elif os.path.isfile('rv.txt'):
    data = np.loadtxt('rv.txt')
else:
    raise RuntimeError('Cannot find data file')
julian_date = data[:,0]
radial_velocity = data[:,1]
plt.scatter(julian_date,radial_velocity,s=0.6,color='blue')
plt.xlabel('Julian Date')
plt.ylabel('Radial Velocity (m/s)')
plt.title('Proxima Centauri Radial Velocity over Time - Josey Hanish')
plt.savefig('proxima_centauri_rv.pdf')
plt.show()
plt.close()


# In[4]:

plt.scatter(julian_date, radial_velocity, s=0.6, color='blue', 
            label='original data')
plt.xlabel('Julian Date')
plt.ylabel('Radial Velocity (m/s)')
plt.xlim((2457400.,2457490.))
plt.title('Proxima Centauri Radial Velocity over Time - Josey Hanish')

# def my_sin(x, freq, amplitude, phase, offset, linslope):
#     return np.sin(x * freq + phase) * amplitude + offset \
#         + linslope*(x-2457400.)

xt = np.linspace(2457400.,2457490.,num=1000)
# f = 2pi*(1/T)
my_freq = 2*np.pi*(1/11.2)
my_amp = 1.38
my_phase = 14
my_offset = 2
my_linslope = -0.06

fns = my_funcs(my_freq, my_amp, my_phase, my_offset, my_linslope)

# yt = fns.my_sin(xt, my_freq, my_amp, my_phase, my_offset, my_linslope)
yt = fns.my_sin(xt)
plt.plot(xt, yt, label='sin fit')
plt.legend()
plt.savefig('proxima_centauri_rv_fit.pdf')
plt.show()
plt.close()


# In[7]:

# def chi_squared(point, freq, amplitude, phase, offset, linslope):
#     """return chi squared for a data point, compared to the sin fit for that point"""
#     x = ((point[1] - my_sin(point[0], freq, amplitude, phase, offset, linslope)) / 1)**2
#     return x

# 
# julian_date_cut = []
# chi_sq_list = []
# for point in zip_data:
#     if point[0] < 2457400. or point[0] > 2457490.:
#         continue
#     else:
# #         chi_sq_list.append(fns.chi_squared(point, my_freq, my_amp, 
# #                                            my_phase, my_offset, my_linslope))
#         chi_sq_list.append(fns.chi_squared(point, fns.my_sin))
#         julian_date_cut.append(point[0])
    
zip_data = zip(julian_date, radial_velocity)
julian_date_cut = [point[0] for point in zip_data 
                   if point[0] > 2457400. and point[0] < 2457490.]
chi_sq_list = [fns.chi_squared(point, fns.my_sin) for point in zip_data 
               if point[0] > 2457400. and point[0] < 2457490.]
print '# of data points = {}'.format(len(julian_date_cut))
    
    
plt.figure()
plt.scatter(julian_date_cut, chi_sq_list, s=0.6, color='blue')
plt.title('Chi-Squared over Time - Josey Hanish')
plt.xlabel('Julian Date')
plt.ylabel('Chi-Squared')
plt.show()

print 'chi-squared = {}'.format(sum(chi_sq_list))


# In[ ]:

# # Here's some stuff I haven't made work yet
# # Please don't grade this part :)

# # https://stackoverflow.com/questions/16716302/how-do-i-fit-a-sine-curve-to-my-data-with-pylab-and-numpy
# def my_sin(x, freq, amplitude, phase, offset):
#     return np.sin(x * freq + phase) * amplitude + offset

# guess_freq = 2*np.pi*(1/11.2)
# guess_amplitude = 1.38
# guess_phase = 14
# # guess_offset = np.mean(radial_velocity)
# guess_offset = 2

# p0=[guess_freq, guess_amplitude,
#     guess_phase, guess_offset]

# try:
#     fit = curve_fit(my_sin, julian_date, radial_velocity, p0=p0)
#     print fit[0]

#     xt = np.linspace(2457400.,2457490.,num=1000)

#     data_fit = []
#     for my_date in xt:
#         data_fit.append(my_sin(my_date, *fit[0]))

#     plt.figure()
#     plt.plot(xt,data_fit)
#     # plt.xlim((2457400.,2457490.))
#     plt.show()
#     plt.close()
    
# except Exception as e:
#     print e

