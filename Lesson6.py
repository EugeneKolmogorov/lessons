# Задача № 30

# a1 = int(input())
# razn = int(input())
# vol = int(input())
# list1 = list()

# for i in range(vol):
#     list1.append(a1)
#     a1 += razn

# print(*list1)

# Задача № 32

list1 = list()
x = int(input())
list2 = list()
min1 = int(input())
max1 = int(input())
count = 0
for i in range(x):
    list1.append(int(input()))

for i in list1:
    if min1 <= i <= max1:
        list2.append(count)
    count += 1
print(list2)