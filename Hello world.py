name = input("What's your name? ")
age = int(input("How old are you? "))

age_next_year = age + 1
modulo = 5%3
pi = 3.14

print(f"Hello, {name.title()}", end = " & ")
print(f"Hello, " +name.title())
print(f"Hello, ", name.title(), sep = "%%%%")
print(f"My age next year is {age_next_year} years old")
print(f"The value of pi is {pi}")
print(f"5 modulo 3 is {modulo}")

