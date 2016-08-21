from vector import Vector

def dot(v1,v2):
	#get the dot product of two vectors
	return v1.x * v2.x + v1.y * v2.y + v3.x * v3.y
	
def cross(v1,v2):
	#get the product of two vectors
	return Vector(v1.y * v2.z - v1.z * v2.y, v1.z * v2.x - v1.x * v2.z, v1.x * v2.y - v1.y * v2.x)

