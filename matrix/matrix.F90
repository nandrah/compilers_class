program Matrix

real, dimension(3, 3) :: mat !two dimensional real array
integer :: i, j

! assigning some values to the matrix
!do i = 1, 3
!	do j = 1, 3
!		matrix(i, j) = i * j
!	end do
!end do

! reading matrix from file
open(1, file='matrix_data.dat')
do i = 1, 3
	do j = 1, 3
		read(1, *) mat(i, j)
	end do
end do
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
