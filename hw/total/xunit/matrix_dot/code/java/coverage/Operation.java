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

	public double dot(double [][]matrix) {
		try {
			if (!checkMatrix(matrix))
				return 0;
			if (matrix[0].length != matrix.length)
				return 0;
			if (matrix.length == 1)
				return matrix[0][0];
			double sum = 0.0;
			int row = matrix.length;
			double factor = 1.0;
			double [][]submatrix = new double[row - 1][row - 1];
			for (int i = 0; i < row; ++i)  {
				int subj = 0;
				for (int j = 0; j < row; ++j) {
					if (i != j) {
						for (int k = 1; k < row; ++k)
							submatrix[j - subj][k - 1] = matrix[j][k];
					}
					else
						subj = 1;
				}
				sum += matrix[i][0] * dot(submatrix) * factor;
				factor *= -1.0;
			}
			return sum;
		} catch (Exception e) {
			return 0;
		}
	}
}
