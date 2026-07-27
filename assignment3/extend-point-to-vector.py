import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, point):
        return self.x == point.x and self.y == point.y
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def distance(self, point):
        return math.sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2 )


class Vector(Point):
    def __init__(self, x, y): 
        # Call the parent class's __init__ to set x, y
        super().__init__(x, y)

    def __str__(self):
        return f"<{self.x},{self.y}>"
    
    def __add__(self, vector):
        return Vector(self.x + vector.x, self.y + vector.y)
    

# test Point class
a = Point(1, 2)
b = Point(3, 4)
c = Point(3, 4)

print(f"Point a is {a}, Point b is {b}, Point c is {c}") # print 
print("if a = b?: ", a == b) # equal or not
print("if b = c?: ", b == c) # equal or not
print(f"Distance from a to b is {a.distance(b)}") # distance from a to b

# test Vector class
v = Vector(1, 2)
w = Vector(3, 4)
z = Vector(3, 4)

print(f"Vector v is {v}, Vector w is {w}, Vector z is {z}") # print 
print("if v = w?: ", v == w) # equal or not
print("if w = z?: ", w == z) # equal or not
print(f"Vector v + w is Vector {v+w}") # sum of v to w
print(f"Length of Vector v is {v.distance(Point(0,0))}")

