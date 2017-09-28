
# coding: utf-8

# In[1]:

import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')
import urllib


# In[2]:

# Open the data, set the x & y values, plot the data
#try:
#    url_opener = urllib.URLopener()
#    url_opener.retrieve('http://www.as.utexas.edu/~gebhardt/a376f17/bhsig2.txt', 
#    'bhsig2.txt')    
#except:
#    print 'Could not download file. Looking for file locally in this directory.'

try:
    data = np.loadtxt('bhsig2.txt')
except:
    print 'Could not open bhsig2.txt'
    quit()

mbh = data[:,1]
sigmav = data[:,0]

# In[12]:
log_mbh = np.log10(mbh)
log_sigmav = np.log10(sigmav)

plt.figure(figsize=(10,10))
plt.title('$M_{\odot}$ vs $\sigma_V$', size='x-large')
#plt.scatter(sigmav, mbh, s=0.5)
plt.scatter(log_sigmav, log_mbh, s=0.5)
#plt.yscale('log')
#plt.xscale('log')
plt.ylabel('Log $M_{\odot}$', size='x-large')
plt.xlabel('Log $\sigma_V$', size='x-large')
#plt.xlim(sigmav.min(),sigmav.max())
#plt.ylim(mbh.min(),mbh.max())

# Fit a line
# Set params a,b by eye
a = 5.7
b = -5
#yt = 10**((a * np.log10(sigmav)) + b)
#plt.plot(sigmav, yt)
yt1 = a * log_sigmav + b
plt.plot(log_sigmav, yt1)
#chi_squared = sum((np.log10(mbh)-np.log10(yt))**2)

p0 = np.polyfit(log_sigmav, log_mbh, 1)
#yt2 = p0[0] * log_sigmav + p0[1]
yt2 = np.polyval(p0, log_sigmav)
plt.plot(log_sigmav, yt2, 'red')

chi_squared1 = sum((log_mbh - yt1)**2)
chi_squared2 = sum((log_mbh - yt2)**2)
plt.text(1.8, 10, 
         'By eye:\nslope={0}\nintercept={1}\nchi-squared={2}\n\n'
         'By polyfit:\nslope={3}\nintercept={4}\nchi_squared={5}'.format(
         a,b,chi_squared1,p0[0],p0[1],chi_squared2), 
         verticalalignment='top',
         fontsize=12)

#plt.savefig('InClass9-19.pdf')
plt.show()


# In[ ]:




# In[ ]:



