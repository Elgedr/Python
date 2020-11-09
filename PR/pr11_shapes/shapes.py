"""Shapes."""


class Shape:
    """General shape class."""

    def __init__(self, color: str):
        """Constructor, sets the color."""
        self.color = color

    def set_color(self, color: str):
        """Set the color of the shape."""
        self.color = color

    def get_color(self) -> str:
        """Get the color of the shape."""
        return self.color

    def get_area(self) -> float:
        """Get area method which every subclass has to override."""
        print("Implement area")


class Circle(Shape):
    """Circle is a subclass of Shape."""

    def __init__(self, color: str, radius: float):
        """
        Constructor of the circle.

        The color is stored using superclass constructor:
        super().__init__(color)

        The radius value is stored here.
        """
        super().__init__(color)
        self.radius = radius

    def __repr__(self) -> str:
        """
        Return representation of the circle.

        For this exercise, this should return a string:
        Circle (r: {radius}, color: {color})
        """
        return f"Circle (r: {self.radius}, color: {self.color})"

    def get_area(self) -> float:
        """
        Calculate the area of the circle.

        Area of the circle is pi * r * r.
        """
        res = float(3.14) * self.radius * self.radius
        return res


class Square(Shape):
    """Square is a subclass of Shape."""

    def __init__(self, color: str, side: float):
        """
        Constructor of the square.

        The color is stored using superclass constructor:
        super().__init__(color)

        The side value is stored here.
        """
        super().__init__(color)
        self.side = side

    def __repr__(self) -> str:
        """
        Return representation of the square.

        For this exercise, this should return a string:
        Square (a: {side}, color: {color})
        """
        return f"Square (a: {self.side}, color: {self.color})"

    def get_area(self) -> float:
        """
        Calculate the area of the square.

        Area of the square is side * side.
        """
        res = self.side * self.side
        return res


class Rectangle(Shape):
    """Class."""

    def __init__(self, color: str, length: float, width: float):
        """Constructor."""
        super().__init__(color)
        self.length = length
        self.width = width

    def get_area(self) -> float:
        """Area."""
        res = self.width * self.length
        return res

    def __repr__(self) -> str:
        """Repr."""
        return f"Rectangle (l: {self.length}, w: {self.width}, color: {self.color})"


class Paint:
    """The main program to manipulate the shapes."""

    def __init__(self):
        """Constructor should create a list to store all the shapes."""
        self.shapes = []

    def add_shape(self, shape: Shape) -> None:
        """Add a shape to the program."""
        self.shapes.append(shape)

    def get_shapes(self) -> list:
        """
        Return all the shapes.
        """
        res = self.shapes
        return res

    def calculate_total_area(self) -> float:
        """
        Calculate total area of the shapes.
        """
        res = []
        for shape in self.shapes:
            res.append(shape.get_area())
        return sum(res)

    def get_circles(self) -> list:
        """Return only circles."""
        res = []
        for i in self.shapes:
            if isinstance(i, Circle):
                res.append(i)
        return res

    def get_squares(self) -> list:
        """Return only squares."""
        res = []
        for shape in self.shapes:
            if isinstance(shape, Square):
                res.append(shape)

        return res

    def get_rectangles(self) -> list:
        """Return only rectangles."""
        """Return only squares."""
        res = []
        for shape in self.shapes:
            if isinstance(shape, Rectangle):
                res.append(shape)
        return res


if __name__ == '__main__':
    paint = Paint()
    circle = Circle("blue", 10)
    square = Square("red", 11)
    paint.add_shape(circle)
    paint.add_shape(square)
    print(paint.get_shapes())
    print(paint.add_shape(square))
    print(paint.get_shapes())
    print(paint.calculate_total_area())
    print(paint.get_circles())
    print(paint.get_squares())
