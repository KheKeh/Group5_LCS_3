#!/usr/bin/python3
m = int(input("Enter a number: "))
if (m % 2) == 0:
    print("Weird")
elif m in range(2, 6):
    print("Not weird")
elif m in range(6, 21):
    print("Weird")
elif m > 20:
    print("Not Weird")
