import numpy as np
from scipy.interpolate import interp1d
import cv2
wps = np.loadtxt("points.txt")
img1 = cv2.imread('1.png')
x = wps[:,0]
y = wps[:,1]
t = np.linspace(0, 1, num=len(x))
f1 = interp1d(t,x,kind='cubic')
f2 = interp1d(t,y,kind='cubic')
newt = np.linspace(0,1,100)
newx = f1(newt)
newy = f2(newt)
import matplotlib.pyplot as plt
plt.imshow(img1)
plt.scatter(x, y)
plt.plot(newx, newy)
plt.show()
