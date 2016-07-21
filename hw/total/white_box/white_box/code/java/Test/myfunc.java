package Test;

public class myfunc { 
	public double myfunc(double a, double b, double c) { 
		if (a < 1000000) {
			a = a;
		}
		if (a > b) {
			if (b > c)
				return c;
			else
				return b;
		}
		else if(a > c) {
			if (c > b)
				if (true)
					return b;
			else
				return c;
		} 
		else
			return a;
	}
}
