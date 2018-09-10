def hello():
    print("Hello world!")

def hello_name(name):
    print(f"Hello {name}!")

print("Start")
hello()
print("Between")
hello_name("Karumõmm")
print("End")


def triangle_area(a, h):
    return a * h / 2

s = triangle_area(10, 10)
print(s)



def get_multipliers(eq):
    x2pos = eq.find("x2")
    a = int(eq[:x2pos].replace(" ", ""))
    b = int(eq[x2pos + 2:eq.find("x", x2pos + 1)].replace(" ", ""))
    c = int(eq[eq.find("x", x2pos + 1) + 1:].replace(" ", ""))
    return a, b, c

a, b, c = get_multipliers("3x2 + 3x - 4")
print(a, b, c)

multipliers = get_multipliers("2x2 - 12x + 3")
print(multipliers)


def get_university_name(abbreviation):
    if abbreviation == "TTU":
        return "Tallinna Tehnikaülikool"
    if abbreviation == "UT":
        return "Tartu Ülikool"
    if abbreviation == "TLU":
        return "Tallinna Ülikool"
    return "Unknown"


#

def triangle_area_print(a, h):
    print(a * h / 2)

area = triangle_area_print(10, 10)
print("area:", area)


def triangle_area(a, h):
    return a * h / 2

area = triangle_area(10, 10)
print("area:", area)


# -------

from time import sleep

def triangle_area(a, h):
    print(f"Got a: {a} and h: {h}")
    print("Calculating area...")
    sleep(1)
    area = a * h / 2
    print("Done!")
    print(f"Area is: {area}")
    return area

area = triangle_area(10, 10)
print(f"Area from function: {area}")
