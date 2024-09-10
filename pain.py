
exp = input("Please choose a operation (+, -, *, /) = ")
n1, n2 = int(input("Please choose the first number = ")), int(input("Please choose the second number = "))


if exp == "+":
    print(n1+n2)
elif exp == "-":
    print(n1-n2)
elif exp == "*":
    print(n1*n2)
elif exp == "/":
    print(n1/n2)