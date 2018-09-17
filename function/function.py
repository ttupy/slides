import math


def secret(x, y):
    return x ** 2 + math.sqrt(y)

def secret(x, y):
    z = x ** 2 + math.sqrt(y)
    return z

print(secret(1, 2) + 3)

result = secret(1, 2) + secret(7, secret(1, 2))

def print_full_name(name, lastname):
    print("Hello", name, lastname)

print_full_name("Mati", "Kaal")

print_full_name(lastname="Kaal", name="Mati")

def greet_animal(name, type="Human"):
    print("Greetings", name, "of type", type)

greet_animal("Mari")
greet_animal("Mari", "Squirrel")


def greet_person(firstname, lastname, country="Estonia", phone=None, email=None):
    print("Hi,", firstname, lastname)
    print("You live in", country)
    if phone: print("phone:", phone)
    if email: print("email:", email)

greet_person("Mati", "Kaal")

greet_person("Kati", "Kaal", phone="112", email="kati@kaal.ee")

greet_person("Donald", "Duck", "USA", "+1 202-456-1111", "president@usa.com")

# ---

def person_data(name, *args, country="Estonia", **kwargs):
    print("Hi", name)
    print("Country", country)
    print("args:", args)
    print("kwargs:", kwargs)
    for key in kwargs:
        print(key, "=>", kwargs[key])

person_data("Pierre", "von", "Smith", age=15, city="Tallinn", country="Latvia")

person_data("Pierre", middlename="von", lastname="Smith", age=15, city="Tallinn")

# ---

nums = [1, 3, 14, 27, 15, 100, 151, 9, 2]
filtered = filter(lambda x: x % 3 == 0 or x % 5 == 0, nums)
print(list(filtered))