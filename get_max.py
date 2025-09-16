a = int(input("Enter first number: "))
b = int(input("Anter second number: "))
c = int(input("enter third number: "))

if a > b:
    max = a
else:
    max = b
if c > max:
    max = c
print("Maximum is:", max)
