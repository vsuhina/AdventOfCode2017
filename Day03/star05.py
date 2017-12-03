from math import sqrt, ceil, fabs
input = 312051

# total element count by adding new circles: 1, 9, 25,... i.e. i*2 where i % 2 != 0 

# how big the matrix should be (in rows or cols)
matrix_size = ceil(sqrt(input))

# matrix size must be odd number
if matrix_size % 2 == 0:
    matrix_size += 1

# Manhattan distance to outer circle
dist_outer = int((matrix_size / 2) - 0.5)

# element count in inner circles (i.e. count of all elements in all inner circles)
inner_cirles = (matrix_size - 2) * (matrix_size - 2)

# element count in last circle (i.e. circle where our input is)
last_circle = matrix_size * matrix_size - inner_cirles

# how many steps in last circle (it starts from (almost) bottom right corner and goes counterclockwise
steps = input - inner_cirles

# how many gaps until outer circle is completed (we calculate with gaps because it ends nicely on last position in row)
gaps = last_circle - steps

# it doesn't matter on which side of matrix our input is
gaps = gaps % matrix_size

# max offset in last row
max_offset = (matrix_size - 1) / 2

# offset in one direction (no mather row or col)
dist_offset = fabs(gaps - max_offset)

# Manhattan distance to element is distance to outer circle and distance from central line (row or col)
dist = dist_outer + int(dist_offset)

print (dist)