program Matrix

real(kind = 16), dimension(3, 3) :: mat !two dimensional real array
integer :: i, j, x

! reading matrix from file
open(1, file='matrix_data.dat')
do i = 1, 3
	do j = 1, 3
		!read(1, *, err=30, iostat=x) mat(i, j)
		read(1, *) mat(i, j)
	end do
end do

!30 print *, 'Not a valid number in the file: ', x
!	stop

close(1)


! print matrix
print *, 'Initial Matrix'
do i = 1, 3
	do j = 1, 3
		print *, mat(i, j)
	end do
end do

! multiply matrix
mat = matmul(mat, mat)

! print matrix
print *, 'Final Matrix'
do i = 1, 3
	do j = 1, 3
		print *, mat(i, j)
	end do
end do

end program Matrix
