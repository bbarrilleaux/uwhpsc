"""
Module to compute square roots by Newton's method.
"""

def sqrt2(x):
	"""Compute square roots via Newton's method."""
	s = 1.
	kmax = 100
	tol = 1.e-14
	for k in range(kmax):
		print "before iteration %s, s = %20.15f" % (k,s)
		s0 = s
		s = 0.5 * (s + x/s)
		dels = s - s0
		if abs(dels / x) < tol:
			break

	print "after %s iterations, s = %20.15f" % (k+1,s)