from cs50 import get_int

while True:
    n = get_int("What is the height?\n")
    if  n >= 1  and n <= 8:
        break

for i in range(n):

    print((n - 1 - i) * " ", end="")
    print((i +1) * "#")



