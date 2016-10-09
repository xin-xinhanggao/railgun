public class GetVertical {
	public Vec getVertical(Vec v1, Vec v2) {
		//get the Vec is vertical to the plane determined by v1 and v2
		//if v1 and v2 can not determine a plane, return unit Vec
		Operation operation = new Operation();
		Vec c = operation.cross(v1, v2).normalize();

		if (c.isZero())
			return c;
		return new Vec(1, 0, 0);
	}
}
