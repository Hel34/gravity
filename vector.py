class vector:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return vector(other.getX()+ self.x, other.getY() + self.getY())

    def __mul__(self, other):
        return vector(other* self.x, other* self.getY())

    def __truediv__(self, other):
        return vector(self.x/other, self.getY()/other)

    def __sub__(self, other):
        return self + other*(-1)

    def length(self):
        return self.lengthsq()**0.5

    def lengthsq(self):
        return self.x**2+self.y**2

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def normalized(self):
        length = self.length()
        if length == 0:
            return self
        return self/length