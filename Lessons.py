# Задача № 2:

# n = input()
# print(int(n[0]) + int(n[1]) + int(n[2]))

# n = int(input())
# print(n % 10 + n //10 % 10 + n // 100)


# Задача № 4

# s = int(input())

# S1 = int(s / 6)
# S2 = S1 * 4
# S3 = S1

# print(S1, S2, S3)


# Задача № 6

# m = input()

# if int(m[0]) + int(m[1]) + int(m[2]) == int(m[3]) + int(m[4]) + int(m[5]):
#     print('YES')
# else:
#     print('NO')


# Задача № 8

n = int(input())
m = int(input())
k = int(input())

if k % n == 0 or k % m == 0:
    print('Yes')
else:
    print('No')