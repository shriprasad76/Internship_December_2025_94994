print("Question No 1:")
a=int(input("Enter First number:"))
b=float(input("Enter second number:"))
c=a+b
print(type(c))
print("******************************************************")
print("Question No 2:")

num=int(input("Enter number:"))
if(num%2==0):
    print(f"Given number is even")
else:
    print(f"given number is odd")

print("******************************************************")
print("Question No 3:")

marks=int(input("Enter marks of student:"))
if(marks>=75):
    print("Destinction")
elif(marks>=60):
    print("First class")
elif(marks>=50):
    print("Second class")
elif(marks>=30):
    print("Pass")
else:
    print("Fail")

print("******************************************************")
print("Question No 4:")

def sum(a,b):
    add=a+b
    sub=a-b
    div=a/b
    mul=a*b
    print(f"1.Addtion is {add}\n2.substraction is {sub}\n3.multiplication is {mul}\n4.Division is {div}")

a=int(input("Enter First number:"))
b=float(input("Enter second number:"))
sum(a,b)
print("******************************************************")
print("Question No 5:")

square=lambda n:n*n


a=int(input("Enter First number:"))
r=square(a)
print(f"Square is {r}")



