import numpy as np
import matplotlib.pyplot as plt


def make_plot():
   
   data = np.loadtxt('co2_mm_mlo.txt')
   x = data[:,2]
   y = data[:,4]

   plt.plot(x,y)
   plt.xlabel('Year')
   plt.ylabel('Mole fraction of CO$_2$ (ppm)')
   plt.title('Mauna Loa CO$_2$ monthly mean data')

   #plt.show()
   plt.savefig('co2_monthly.pdf')
   plt.close()


def plot_with_trend():
   
   data = np.loadtxt('co2_mm_mlo.txt')
   x = data[:,2]
   y1 = data[:,4]
   y2 = data[:,5]

   plt.scatter(x, y1, s=0.6, color='g', alpha=0.8, label='monthly average')
   plt.plot(x, y2, '-', color='r', lw=1.2, alpha=0.8, label='trend (seasonal correction)')
   plt.xlabel('Year')
   plt.ylabel('Mole fraction of CO$_2$ (ppm)')
   plt.xlim(1957, 2019)
   
   legend = plt.legend(loc=0, scatterpoints=6, title='Mauna Loa CO$_2$', frameon=False)
   legend.get_title().set_fontsize('x-large')
   
   plt.savefig('co2_monthly_with_trend.pdf')
   plt.close()


if __name__ == '__main__': 
   make_plot()
   plot_with_trend()