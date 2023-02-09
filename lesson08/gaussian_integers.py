class Gaussian_Integer():

    def __init__(self, r, i):
        self.r = r
        self.i = i

    def add(self, other):
        return Gaussian_Integer(self.r + other.r, self.i + other.i)

    def multiply(self, other):
        return Gaussian_Integer(self.r * other.r - self.i * other.i, self.r * other.i + self.i * other.r)

    def __str__(self):
        return f"{self.r}+{self.i}i"


if __name__ == '__main__':
    u = Gaussian_Integer(1, 1)
    v = Gaussian_Integer(1, 2)
    w = u.multiply(u)
    x = u.add(v).add(w)
    print('u=', u)
    print('v=', v)
    print('w=', w)
    print('x=', x)
