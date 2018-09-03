greeting = "Hello all!"
student_count = 300

print(greeting)
print("Students:", student_count)

greeting = "Hi"                     # value is changed
student_count = student_count + 2   # add 2

print(greeting)
print("Students:", student_count)

greeting += " students!"            # same as greeting = greeting + " .. "

print(greeting)


################


meaningful_variable = 10
print(meaningful_variable)  # 10
print(type(meaningful_variable))  # <class 'int'>

meaningful_variable = "hello"
print(meaningful_variable)  # hello
print(type(meaningful_variable))  # <class 'str'>

meaningful_variable = 9 / 2
print(meaningful_variable)  # 4.5
print(type(meaningful_variable))  # <class 'float'>
