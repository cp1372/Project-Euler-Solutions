filePath ="p081_matrix.txt"
matrix = []
for row in open(filePath, 'r').readlines():
	numbers = row.split(',')
	segment = []
	for n in numbers:
		segment.append( int(n) )
	matrix.append(segment)
	
N = len(matrix)
for i in range(0, N,):
	for j in range(0, N):
		
		if i == 0 and j == 0:
			matrix[i][j]
		elif i == 0:
			matrix[i][j] += matrix[i][j-1]
		elif j == 0:
			matrix[i][j] += matrix[i-1][j]
		else:
			matrix[i][j] += min( matrix[i-1][j], matrix[i][j-1] )
		

print (matrix[N-1][N-1])