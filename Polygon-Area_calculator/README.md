Polygon Area Calculator

This is a simple program that includes two classes, Rectangle and Square, that can be used to calculate the area and perimeter of polygons.

Rectangle Class

The Rectangle class is defined with the following methods:

_init_(self, width, height): Initializes a new rectangle with the given width and height.
_str_(self): Returns a string representation of the rectangle in the format Rectangle(width=..., height=...).
set_width(self, width): Sets the width of the rectangle to the given value.
set_height(self, height): Sets the height of the rectangle to the given value.
get_area(self): Calculates and returns the area of the rectangle.
get_perimeter(self): Calculates and returns the perimeter of the rectangle.
get_diagonal(self): Calculates and returns the length of the diagonal of the rectangle.
get_picture(self): Returns a string representation of the rectangle as a picture made up of * symbols.
get_amount_inside(self, shape): Calculates and returns the maximum number of instances of the given shape that can fit inside the rectangle. The shape can be either a Rectangle or a Square.
Square Class

The Square class is defined as a subclass of the Rectangle class and inherits all of its methods. It is defined with the following additional methods:

_init_(self, length): Initializes a new square with the given length.
_str_(self): Returns a string representation of the square in the format Square(side=...).
set_side(self, length): Sets the length of the square to the given value.

Example:

# Create a rectangle
rect = Rectangle(5, 10)

# Get the area of the rectangle
area = rect.get_area()
print(f"Area: {area}")  # Output: "Area: 50"

# Create a square
square = Square(7)

# Get the perimeter of the square
perimeter = square.get_perimeter()
print(f"Perimeter: {perimeter}")  # Output: "Perimeter: 28"
