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

def multiply(matrix1,matrix2):
	# make multiply operation for two matrixes
	# if the operation is illegal, we will return False
	if checkMatrix(matrix1) == False or checkMatrix(matrix2) == False:
		return False

	if(len(matrix1[0]) != len(matrix2)):
		return False

	matrix = []
	row = len(matrix1)
	column = len(matrix2[0])

	for x in range(0,row):
		submatrix = []
		for y in range(0,column):
			item = 0
			xrow = matrix1[x]
			for index in range(0,len(xrow)):
				item = item + xrow[index] * matrix2[index][y]
			submatrix.append(item)
		matrix.append(submatrix)

	return matrix
