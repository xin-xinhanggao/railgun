public class Operation {
	public double dot(Vec v1, Vec v2) {
		//get the dot product of two Vecs
		return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z;
	}
	public Vec cross(Vec v1, Vec v2) {
		//get the product of two Vecs
		return new Vec(v1.y * v2.z - v1.z * v2.y, v1.z * v2.x - v1.x * v2.z, v1.x * v2.y - v1.y * v2.x);
	}
}
