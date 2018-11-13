
a = [1, 2, 3]
b = [1, 2, 3]
c = b

print(id(a))   # 44058024
a.append(4)
print(id(a))   # 44058024 still the same
print(id(b))   # 44059184
print(id(c))   # 44059184 - same as b
b.pop()
print(id(b))   # 44059184 - still the same
print(id(c))   # 44059184 - and same



print("--------")

print(type(1))     # <class 'int'>
print(type(True))  # <class 'bool'>
print(type(1.2))   # <class 'float'>
print(type(None))  # <class 'NoneType'>
print(type(len))   # <class 'builtin_function_or_method'>
print(type(type))  # <class 'type'>


print("--------")

class Student:
    pass

s = Student()
print(type(s))  # <class '__main__.Student'>
print(id(s))    # 12448112

t = Student()
print(type(t))  # <class '__main__.Student'>
print(id(t))    # 12423408

# --------------
print("--------")

s1 = Student()
s2 = Student()
s3 = s1

print(s1 == s2)   # False
print(s1 == s3)   # True
print(s2 == s3)   # False

print("--------")


class Student:
    """Student class."""

    def hello(self):
        """Method (function) which just prints out "Hello!"."""
        print("Hello!")


s = Student()
s.hello()       # no "self" argument

print("----------")

class Student:
    def greet_friend(self, friend_name):
        print(f"Hello, {friend_name}")

s = Student()
s.greet_friend("Kaia")
Student.greet_friend(s, "Kaia")

print("---------")

class Student:
    def __init__(self):
        print("Initializing student..")


s = Student()  # Initializing student..

class Student:
    def __init__(self, name, title):
        self.name = name
        self.title = title

ago = Student("Ago", "Sir")
print(ago.name)

leela = Student("Leela", "Captain")
print(leela.title)

class Shop:
    def __init__(self, name, age, products_file=None):
        self.products = []
        self.name = name
        self.established = 2018 - age
        if products_file is not None:
            # open the file and read products from it
            pass

    def inventory(self):
        print(f"Inventory for {self.name} (est. {self.established}:")
        for p in self.products:
            print("product: ..")
            pass


class Point2D:
    """Point in (x, y) coordinate space)."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_point(self):
        print(f"({self.x:.2f}, {self.y:.2f})")


p1 = Point2D(1.234, 0.23456)
p2 = Point2D(-1, 3)

p1.print_point()   # (1.23, 0.23)
p2.print_point()   # (-1.00, 3.00)


p3 = Point2D(3, 3)
p4 = Point2D(3, 3)
p5 = p4

print(p3 == p4)   # False
print(p4 == p5)   # True

p3.x = 10
p3.print_point()   # (10.00, 3.00)

p4.x = 11
p4.print_point()   # (11.00, 3.00)
p5.print_point()   # (11.00, 3.00)

print(p5)

class Point2D:
    """Point in (x, y) coordinate space)."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_point(self):
        print(f"({self.x:.2f}, {self.y:.2f})")

    def __eq__(self, other):
        if isinstance(other, Point2D):
            return self.x == other.x and self.y == other.y
        return False

    def __str__(self):
        return f"({self.x:.2f}, {self.y:.2f})"
p1 = Point2D(1, 2)
print(p1)   # (1.00, 2.00)

p6 = Point2D(1, 2)
p7 = Point2D(1, 2)

print(p6 == p7)   # True
print(p6 is p7)   # False

p8 = p6
print(p6 is p8)   # True


class Doorbell:
    click_count = 0

    def __init__(self):
        self.click_count = 0

    def ring(self):
        #print("Ringing..")
        self.click_count += 1
        Doorbell.click_count += 1

d1 = Doorbell()
d2 = Doorbell()

for _ in range(10): d1.ring()
for _ in range(4): d2.ring()
print(d1.click_count)         # 10
print(d2.click_count)         # 4
print(Doorbell.click_count)   # 14


class Point3D(Point2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def __str__(self):
        return f"({self.x:.2f}, {self.y:.2f}, {self.z:.2f})"

p3d = Point3D(1, 2, 3)
print(p3d)     # (1.00, 2.00)
