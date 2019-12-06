# Name: PengZhao Feng
# Student ID: 0891248
# Due Date: 12/3/2019
# MSITM 6341


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def rectangle_dimension(self):
        return str(self.width) + " x " + str(self.height) + " = " + str(self.rectangle_area())

    def rectangle_area(self):
        return self.width * self.height

    def rectangle_perimeter(self):
        return 2 * (self.width + self.height)


new_rectangle = Rectangle(14, 20)

print("The dimensions of the rectangle are: " + new_rectangle.rectangle_dimension())

print("the rectangle area is: " + str(new_rectangle.rectangle_area()))

print("the rectangle perimeter is: " + str(new_rectangle.rectangle_perimeter()))
