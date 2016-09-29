class Vector(object):
  #three dimensional vector
  def __init__(self,x = 0,y = 0,z = 0):
    self.x = x
    self.y = y
    self.z = z

  def length2(self):
    return self.x * self.x + self.y * self.y + self.z * self.z 
  
  def length(self):
    return pow(self.x * self.x + self.y * self.y + self.z * self.z,0.5)
  
  def normalize(self):
    l = self.length()
    if l > 1e-6: 
      return Vector(self.x / l, self.y / l, self.z / l)
    else:
      return Vector(0,0,0)
