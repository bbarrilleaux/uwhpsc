"""
Module to compute square roots by Newton's method.
"""

def sqrt2(x, debug=False):
	"""Compute square roots via Newton's method."""
	from numpy import nan
	if x==0.:
		return 0.
	elif x<0:
		print "Error, x must be non-negative"
		return nan
	assert x>0. and type(x) is float, "Unrecognized input"

	s = 1.
	kmax = 100
	tol = 1.e-14
	for k in range(kmax):
		if debug:
			print "before iteration %s, s = %20.15f" % (k,s)
		s0 = s
		s = 0.5 * (s + x/s)
		dels = s - s0
		if abs(dels / x) < tol:
			break
	if debug:
		print "after %s iterations, s = %20.15f" % (k+1,s)
	return s