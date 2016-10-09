import java.math.*;

public class Vec {
	//three dimensional Vec
	double x;
	double y;
	double z;

	public Vec() {
		x = 0; 
		y = 0;
		z = 0;
	}

	public Vec(double x, double y, double z) {
		this.x = x;
		this.y = y;
		this.z = z;
	}

	public double getLength2() {
		return x * x + y * y + z * z;
	}

	public double getLength() {
		return Math.sqrt(getLength2());
	}

	public Vec normalize() {
		double l = getLength();
		if (l > 1e-6)
			return new Vec(x / l, y / l, z / l);
		else
			return new Vec(0, 0, 0);
	}

	public boolean isZero() {
		return getLength() < 1e-6;
	}
}
