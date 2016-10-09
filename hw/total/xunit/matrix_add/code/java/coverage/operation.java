public class operation {
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

	public double[][] add(double [][]matrix1, double [][]matrix2) {
		try {
			if (!checkMatrix(matrix1) || !checkMatrix(matrix2))
				return null;
			if (matrix1.length != matrix2.length)
				return null;
			if (matrix1[0].length != matrix2[0].length)
				return null;
			double [][]matrix = new double[matrix1.length][matrix1[0].length];
			for (int i = 0; i < matrix1.length; ++i) {
				for (int j = 0; j < matrix1[0].length; ++j)
					matrix[i][j] = matrix1[i][j] + matrix2[i][j];
			}
			return matrix;
		} catch (Exception e) {
			return null;
		}
	}
}
