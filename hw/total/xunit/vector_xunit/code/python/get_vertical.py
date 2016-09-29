from vector import Vector
from operation import cross

def vertical(v1,v2):
	# get the vector is vertical to the plane determined by v1 and v2
	# if v1 and v2 can not determine a plane, return unit vector
	c = cross(v1,v2).normalize()
	if c.length() > 0:
		return c
	return Vector(1,0,0)
