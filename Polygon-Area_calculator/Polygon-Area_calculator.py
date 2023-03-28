class Rectangle:

  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return (self.width * self.height)

  def get_perimeter(self):
    return (2 * self.width + 2 * self.height)

  def get_diagonal(self):
    return ((self.width**2 + self.height**2)**.5)

  def get_picture(self):
    if self.height >= 50 or self.width >= 50:
      return "Too big for picture."
    else:
      picture = ""
      for i in range(self.height):
        picture += "*" * self.width + "\n"
      return picture

  def get_amount_inside(self, shape):
    if isinstance(shape, Rectangle):
      width_fit = self.width // shape.width
      height_fit = self.height // shape.height
      return width_fit * height_fit
    elif isinstance(shape, Square):
      side_fit = self.width // self.width
      return side_fit**2
    else:
      return TypeError()


class Square(Rectangle):

  def __init__(self, length):
    super().__init__(length, length)

  def __str__(self):
    return f"Square(side={self.width})"

  def set_side(self, length):
    self.height = length
    self.width = length

