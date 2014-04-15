# pdb debugging tool example
import numpy as np

x = np.linspace(0,1,50)

def f(z):
	x = np.cos(z)
	import pdb; pdb.set_trace()
	return x

y = f(x)

print 'x = ', x
print 'y = ', y