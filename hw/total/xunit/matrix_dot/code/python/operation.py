def checkMatrix(list):
	# check variable list is whether a matrix full of digit or not 
	# we think empty matrix is illegal
	try:
		typelist = []
		if len(list) == 0 and type(list) != type(typelist):
			return False;
		scale = len(list[0])
		for sublist in list:
			if(len(sublist) != scale) and type(sublist) != type(typelist):
				return False;
			for item in sublist:
				if type(item) != type(0) and type(item) != type(1.1):
					return False
		return (scale > 0)
	except Exception,ex:
		return False

def dot(matrix):
	# get the dot of the matrix
	# if the operation is illegal, we will return False
	if checkMatrix(matrix) == False:
		return False

	if len(matrix[0]) != len(matrix):
		return False

	if len(matrix) == 1:
		return matrix[0][0]

	sum = 0
	row = len(matrix)
	factor = 1

	for cursor in range(0,row):
		submatrix = []
		for x in range(0,row):
			if x != cursor:
				submatrix.append(matrix[x][1:])
		sum += matrix[cursor][0] * dot(submatrix) * factor
		factor *= -1
		
	return sum
