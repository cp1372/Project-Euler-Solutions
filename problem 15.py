#Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner. How many such routes are there through a 20×20 grid?

#Easy way using combinatorics 
def binomialCoefficent(n,k):
	paths = 1
	for i in range (0,k):
		paths *= (2*n) - i
		paths /= i+1
	return paths
	
print (binomialCoefficent(20,20))

#Long brute force method
cols_count = 21
rows_count = 21
matrix = [[0 for x in range(cols_count)] for x in range(rows_count)]

matrix[cols_count-1][rows_count-1] = 777

def nextStep(m,x,y):

	if (x >= cols_count or y >= rows_count):
		return 0
	if (m[x][y] == 777):
		return 1
	else:
		return (nextStep(m,x+1,y) + nextStep(m,x,y+1))