
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
