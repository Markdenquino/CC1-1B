#lbs to kg converter
lbs = int(input("Enter weight in lbs:"))
kg = (lbs)/2.205
print("The weight in kilograms is",round(kg, 2))
print("=================================================")

#mi to km converter
mi = int(input("Enter length in mi:"))
km = (mi)*1.61
print("The length in kilometers is",round(km, 2))
print("=================================================")

#f to c converter
F = int(input("Enter temperature in F:"))
C = (F-32)*5/9
print("The temperature in celcius is",round(C, 2))
print("=================================================")

#
a = int(input("Age of student 1:"))
b = int(input("Age of student 2:"))
c = int(input("Age of student 3:"))
d = int(input("Age of student 4:"))
e = int(input("Age of student 5:"))
f = int(input("Age of student 6:"))
g = int(input("Age of student 7:"))
h = int(input("Age of student 8:"))
i = int(input("Age of student 9:"))
j = int(input("Age of student 10:"))
add = a + b + c + d + e + f + g + h + i + j
print("Total age = ",add)
average = add / 10
print("The Average age of the students = ",round(average, 2))
print("=================================================")
