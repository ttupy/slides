s = "Hello"
print(type(s))  # <class 'str'>
print(id(s))
print(id(s.replace("H", "h")))
print(id(s.replace("i", "")))
print(id("hello"))
print(id("hello"))
s2 = "hello"
print(id(s2))
s3 = str("hello")
print(id(s3))

s = "hi"
print(id(s))
print(id(s.replace("h", "o")))