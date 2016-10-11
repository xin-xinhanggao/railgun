public class Operation {
	public boolean checkMatrix(double [][]list) {
		try {
			int dim1 = list.length;
			if (dim1 == 0)
				return false;
			int dim2 = list[0].length;
			if (dim2 == 0)
				return false;
			for (int i = 0; i < dim1; ++i) {
				if (list[i].length != dim2)
					return false;
			}
			return true;
		} catch (Exception e) {
			return false;
		}
	}

	public double[][] multiply(double [][]matrix1, double [][]matrix2) {
		try {
			if (!checkMatrix(matrix1) || !checkMatrix(matrix2))
				return null;
			if (matrix1[0].length != matrix2.length)
				return null;
			double [][]matrix = new double[matrix1.length][matrix2[0].length];
			for (int i = 0; i < matrix1.length; ++i) {
				for (int j = 0; j < matrix2[0].length; ++j) {
					matrix[i][j] = 0;
					for (int k = 0; k < matrix2.length; ++k)
						matrix[i][j] += matrix1[i][k] * matrix2[k][j];
				}
			}
			return matrix;
		} catch (Exception e) {
			return null;
		}
	}
}
