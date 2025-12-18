print("Question No 1:")
list1 = [1, 2, 3, 4, 5]
print(f"List before: {list1}")
list1.append(6)

print(f"List after: {list1}")

print("******************************************************")

print("Question No 2:")
tuple1 = ("Shri", 94994, "3rd Year", 98)
print(tuple1)

print("******************************************************")

print("Question No 3:")
set1 = {1, 2, 2, 3, 4}
print(set1)
set1.add(5)       # add() takes only one element
set1.remove(1)
print(set1)

print("******************************************************")

print("Question No 4:")
dict1 = {
    "name": "Shri",
    "Roll Number": 94994,
    "Standard": "3rd Year",
    "Marks": 98
}
print(dict1)
dict1["name"] = "Shriprasad"   # correct way to update
print(dict1)

print("******************************************************")

print("Question No 5:")
list2 = [
    ["Sarthak", 99, 98, 97],
    ["Shri", 98, 97, 96]
]
print(list2)
print(f"Second student marks: {list2[1]}")
print(f"Marks in 3rd subject of first student: {list2[0][3]}")

print("******************************************************")

print("Question No 6:")
list3 = [1,2,3,4,5,6,7,8,9,10]
total = 0
for i in range(0, 10):
    print(list3[i])
    total += list3[i]

print(f"Sum is {total}")

print("******************************************************")

print("Question No 7:")
import math
a = 100
sr = math.sqrt(a)
print(f"The square root is {sr}")

b = 10
fc = math.factorial(b)
print(f"The factorial is {fc}")

print("******************************************************")

print("Question No 8:")
from operations import add , subtract

a = 10
b = 5
print("Addition:", add(a, b))
print("Subtraction:", subtract(a, b))

print("******************************************************")

print("Question No 9:")
marks = {
    "Maths": [85, 90, 88],
    "Science": [78, 82, 80],
    "English": [92, 89, 94]
}

for subject, marks_list in marks.items():
    print(subject, ":", marks_list)