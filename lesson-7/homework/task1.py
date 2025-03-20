import math


class Vector:
    def __init__(self, *components):
        self.components = tuple(components)

    def __repr__(self):
        return f"Vector{self.components}"
    
    def __add__(self, other):
        if(len(self.components) != len(other.components)):
            raise ValueError("Vectors must have the same dimension")
        result = []
        for i in range(len(self.components)):
            result.append(self.components[i] + other.components[i])
        return Vector(*result)
    
    def __sub__(self, other):
        if(len(self.components) != len(other.components)):
            raise ValueError("Vectors must have the same dimension")
        result = []
        for i in range(len(self.components)):
            result.append(self.components[i] - other.components[i])
        return Vector(*result)
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(*(a * other for a in self.components))
        elif isinstance(other, Vector):
            if len(self.components) != len(other.components):
                raise ValueError("Vectors must have the same dimensions")
            return sum(a * b for a, b in zip(self.components, other.components))
        else:
            raise TypeError("Type Error between Vector and other types")
    
    def __rmul__(self, other):
        return self * other
    
    def magnitude(self):
        return math.sqrt(sum(a**2 for a in self.components))
    
    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector")
        return Vector(*(a / mag for a in self.components))
    



v1 = Vector(5, 2, 3)
v2 = Vector(4, 6, 1)

print("v1:", v1)
print("v2:", v2)

v3 = v1 + v2
print("v1 + v2:", v3)

v4 = v2 - v1
print("v2 - v1:", v4)

dot_product = v1 * v2
print("v1 * v2 (dot product):", dot_product)

v5 = 3 * v1
print("3 * v1:", v5)

print("Magnitude of v1:", v1.magnitude())

v_unit = v1.normalize()
print("Normalized v1:", v_unit)