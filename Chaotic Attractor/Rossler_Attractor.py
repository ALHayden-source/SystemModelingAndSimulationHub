# Simulation of the Rosler Atrtaction for COSC 
# info on the Rossler attrator: https://en.wikipedia.org/wiki/R%C3%B6ssler_attractor
import numpy as np
import pylab as pl
from mpl_toolkits.mplot3d import Axes3D

def Rossler_attractor(init,a,b,c,speed,steps):
	xs = np.zeros((steps))
	ys = np.zeros((steps))
	zs = np.zeros((steps))
	xs[0] = init[0]
	ys[0] = init[1]
	zs[0] = init[2]
	
	for i in range(1,steps):
		x = xs[i-1]
		y = ys[i-1]
		z = zs[i-1]
		dx = -y-z
		dy = x+a*y
		dz = b+z*(x-c)
		xs[i] = x+speed*dx
		ys[i] = y+speed*dy
		zs[i] = z+speed*dz
		
	fig = pl.figure()
	ax = Axes3D(fig)
	ax.plot(xs,ys,zs)
	pl.show()

Rossler_attractor(init = (0.1,0.1,0.1), a = 0.35, b = 0.5, c = 12, speed = 0.01, steps = 15000)