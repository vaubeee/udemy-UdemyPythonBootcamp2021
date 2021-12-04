def build_student(name = "***Error: missing argument***", major = "***Error: missing argument***"):
    student = {"student_name" : name, "student_major" : major}
    return student

my_student = build_student("Volker", "Programming")
print(my_student)

def product(x, y):
    result = x * y
    return result
result_product = product(5, 10)
print(result_product)

def add(x, y):
    return x + y #short form
result_add = add(5, 10)
print(result_add)