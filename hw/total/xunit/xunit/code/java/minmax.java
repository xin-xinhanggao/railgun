public class minmax { 
    public double get_min(double a, double b, double c) {
		if (a < b) {
		    if (a < c)
		        return a;
		    return c;
		}
		else {
		    if (b < c)
		        return b;
		    return c;
		}
	}
}
