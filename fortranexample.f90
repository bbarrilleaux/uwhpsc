program myexample
	! force variables to be explicitly declared:
	implicit none

	! declare some 8-bit floating point numbers:
	real (kind=8) :: x,y,z

	! declare a constant:
	integer, parameter :: n = 100

	! declare an array:
	real (kind=8), dimension(n) :: m

	! declare an integer:
	integer :: i

	! exponential notation:
	x = 512.d4
	y = 12345.d-7
	z = x * y

	! splat means "print with full precision"
	print *, "x = ", x
	print *, "y = ", y
	print *, "z = ", z

	! here's what a loop looks like:
	do i=1,n
		m(i) = 4.d0 * i
		enddo

	print *, "end of the array = ", m(n)

end program myexample