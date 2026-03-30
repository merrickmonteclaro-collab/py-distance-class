class Distance:
    
    def __init__(self, km: int):
        self.km = km
    
    def __str__(self):
        return f"Distance: {self.km} kilometers."
    
    def __repr__(self):
        return f"Distance(km={self.km})"
    
    def __add__(self, other):
        if isinstance(other, Distance):
            total = self.km + other.km
        else:
            total = self.km + other
        return Distance(total)
    
    def __iadd__(self, other):
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self
    
    def __mul__(self, other):
        if not isinstance(other, (int, float)):
            return NotImplemented
        return Distance(self.km * other)
    
    def __rmul__(self, other):
        return self.mul(other)
    
    def __truediv__(self, other):
        if not isinstance(other, (int, float)):
            return NotImplemented
        result = self.km / other
        return Distance(round(result, 2))
    
    def __lt__(self, other):
        if isinstance(other, Distance):
            return self.km < other.km
        if isinstance(other, (int, float)):
            return self.km < other
        return NotImplemented
    
    def __gt__(self, other):
        if isinstance(other, Distance):
            return self.km > other.km
        if isinstance(other, (int, float)):
            return self.km > other
        return NotImplemented
    
    def __eq__(self, other):
        if isinstance(other, Distance):
            return self.km == other.km
        if isinstance(other, (int, float)):
            return self.km == other
        return NotImplemented
    
    def __le__(self, other):
        if isinstance(other, Distance):
            return self.km <= other.km
        if isinstance(other, (int, float)):
            return self.km <= other
        return NotImplemented
    
    def __ge__(self, other):
        if isinstance(other, Distance):
            return self.km >= other.km
        if isinstance(other, (int, float)):
            return self.km >= other
        return NotImplemented
    