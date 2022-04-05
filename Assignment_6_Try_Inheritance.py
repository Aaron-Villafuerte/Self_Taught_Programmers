class Shape():
    def what_am_i(self):
        print("I am a shape")

class Rectangle(Shape):
    def __init__(self, w, l):
        self.width = w
        self.length = l

    def calculate_perimeter(self):
        return 2*(self.width + self.length)
    
class Square(Shape):
    def __init__(self, s1):
        self.s1 = s1
 
    def calculate_perimeter(self):
        return 4*(self.s1)

    def change_size(self, x):
        self.s1 += s1


a_rectangle = Rectangle(10,12)
a_square = Square(11)

a_rectangle.what_am_i()
a_square.what_am_i()
