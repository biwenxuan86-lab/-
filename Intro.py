name = "Jeff"
age = 27
city = "Cavan"
target = "AI Enginner"
print (f"Hello, my name is {name}. I'm {age} years old, from {city}, and my goal is to become an {target}.")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
if age >= 18:
    print(f"{name}, your are an adult.")
else:
    print(f"{name}, you are a teenager.")
print('You have lived for', age * 365 )
print('Your target is be become',target,', good choice!')

