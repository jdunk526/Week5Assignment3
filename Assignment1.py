i = int(input("Enter a number: "))
x = 0
while x < i:
    x = x+1
    if x%3 == 0 and x%5 == 0:
        print("fizzbuzz")
    elif x%3 == 00:
        print("fizz")
    elif x%5 == 0:
        print("buzz")
    else:
        print(x)

