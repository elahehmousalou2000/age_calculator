name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age < 30:
    print(f"{name}, you will be 30 in {30 - age} years.")
elif age == 30:
    print(f"{name}, you are already 30.")
else:
    print(f"{name}, you were 30 {age - 30} years ago.")
