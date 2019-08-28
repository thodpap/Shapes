class Rectangle:
    height = 0
    width = 0
    def __init__(self,h,w):
        self.height,self.width = h,w

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)

class Square(Rectangle):
    def __init__(self,a):
        super().__init__(a,a)

class LiveRectangle(Rectangle):
    depth = 0
    def __init__(self,a,b,c):
        super().__init__(a,b)
        self.depth = c

    def volume(self):
        return self.height * self.width * self.depth;

class Cube(LiveRectangle):
    def __init__(self,a):
        super().__init__(a,a,a)
