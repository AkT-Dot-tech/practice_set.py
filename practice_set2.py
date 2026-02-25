# Practice Set 2 Solutions

# 1
print(1+2+3+4+5)


# 2
N = 1
S = 1


# 3
n = int(input("Enter an integer: "))
if n % 2 == 0:
    print("n is even")
else:
    print("n is odd")


# 4
print('*' * 5)
print(('#' + ' ') * 5)


# 5
name = "Akshat Sharma"
address = "Greater Noida, Uttar Pradesh"

print(name)
print(address)


# 6
x = 1
y = 0
print(x and y)
print(x or y)
print(not x)
print(not y)


# 7
a = int(input())
b = int(input())

if a < b:
    print(a, b)
else:
    print(b, a)


# 8
num = int(input())

if num == 0 or num == 1:
    if num == 0:
        print("Zero")
    else:
        print("One")
else:
    print("Invalid")


# 9
for i in range(2, 13):
    for j in range(2, i):
        if i % j == 0:
            print(i, "Composite")
            break
    else:
        print(i, "Prime")


# 10
for i in range(100, 1000):
    a = i // 100
    b = (i // 10) % 10
    c = i % 10
    if i == a**3 + b**3 + c**3:
        print(i)


# 11
l1 = ['A', 'B', 'C']
l2 = ['1', '2', '3']

for i in l1:
    for j in l2:
        print(i + j)


# 12
person = {'Name': 'Jane', 'Age': 25}
person['Father'] = 'John Doe'
print(person)


# 13
lst = [4, 2, 9, 1, 7]

for i in range(len(lst)-1):
    if lst[i] > lst[i+1]:
        lst[i], lst[i+1] = lst[i+1], lst[i]

print(lst)


# 14
a = [[1, 2], [3, 4], [5, 6]]
b = []

for i in a:
    for j in i:
        b.append(j)

print(b)


# 15
maria = {'korean': 90, 'english': 85, 'math': 92, 'science': 90}

avg = sum(maria.values()) / len(maria)
print(avg)


# 16
import copy

school = {'class1': {'student1': 'A'}, 'class2': {'student2': 'B'}}
school2 = copy.deepcopy(school)

print(school is school2)


# 17
scores = (
    ('Hyun', 88, 95, 90),
    ('Soo', 90, 92, 88),
    ('Min', 85, 89, 91),
    ('Jin', 92, 94, 93)
)

names, eng, math, sci = zip(*scores)
avg = sum(math) / len(math)
print(avg)
