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

def add(matrix1,matrix2):
	# make add operation for two matrixes
	# if the operation is illegal, we will return False
	try:
		if checkMatrix(matrix1) == False or checkMatrix(matrix2) == False:
			return False

		if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
			return False

		matrix = []
		for (submatrix1, submatrix2) in zip(matrix1, matrix2):
			submatrix = []
			for (x,y) in zip(submatrix1, submatrix2):
				submatrix.append(x + y)
			matrix.append(submatrix)

		return matrix
	except Exception,ex:
		return False