# Задача № 26

# def f(a, b):
#     if b == 1:
#         return a
#     if b != 1:
#         return a * f(a, b-1)
# a = int(input())
# b = int(input())
# print(f(a, b))

# Задача № 28

def sum(a, b):
    
    if b == 0:
        return a
    if b != 0:
        return sum(a+1, b-1)
a = int(input())
b = int(input())
print(sum(a, b))
