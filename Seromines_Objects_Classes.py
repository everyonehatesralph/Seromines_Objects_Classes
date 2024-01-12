while True:
    import math

    radius = eval(input("Enter the radius of the circle: ").strip())


    class Circle:
        def __init__(self, radius):
            self.radius = radius

        def area(self):
            result = math.pi * self.radius ** 2
            return result

        def perimeter(self):
            result = 2 * math.pi * self.radius
            return result


    my_circle = Circle(radius)

    print(f"Circle Area is, {my_circle.area():,.2f}\nCircle Perimeter is, {my_circle.perimeter():,.2f}.\n")