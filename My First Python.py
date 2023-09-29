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

#Story game
print("A horde of goblin raided the Willow village unguarded. Now it's up to you to become a hero!!")
print("--------------------------------------------------------------------------------------------")
h1 = ("Rook")
h2 = ("Knight")
h3 = ("Bishop")
h4 = ("Queen")
h5 = ("King")
print("<",h1,"> ", "<",h2,"> ", "<",h3,"> ", "<",h4,"> ", "<",h5,"> ",)
hero = input(">Choose your hero:")

if (hero == "Rook"):
    print("/You chose <Rook>/")

elif (hero == "Knight"):
    print("/You chose <Knight>/")

elif (hero == "Bishop"):
    print("/You chose <Bishop>/")

elif (hero == "King"):
    print("/You chose <King>/")

elif (hero == "Queen"):
    print("/You chose <Queen>/")

else:
    print("/Please type the given above/")

print("--------------------------------------------------------------------------------------------")
w1 = ("Cronus' Flesh [Shield]")
w2 = ("Hade's touch [Scythe]")
w3 = ("Bolt of Zues [Crossbow]")
w4 = ("Poseidon's Arsenal [Trident]")
w5 = ("Last of Gladius [Broad sword]")
print("<w1>", w1)
print("<w2>", w2)
print("<w3>", w3)
print("<w4>", w4)
print("<w5>", w5)
weapon = input(">Choose a weapon:")

if (weapon == "w1"):
    print("/You chose <", w1, ">/")

elif (weapon == "w2"):
    print("/You chose <", w2, ">/")
  
elif (weapon == "w3"):
    print("/You chose <", w3, ">/")

elif (weapon == "w4"):
    print("/You chose <", w4, ">/")

elif (weapon == "w5"):
    print("/You chose <", w5, ">/")

else:
    print("/Please type the given above/")
    
print("--------------------------------------------------------------------------------------------")
a1 = ("Fire")
a2 = ("Heal")
a3 = ("Teleport")
a4 = ("Time")
a5 = ("Nature")
print("<",a1,"> ", "<",a2,"> ", "<",a3,"> ", "<",a4,"> ", "<",a5,"> ",)
ability = input("Now, Choose an ability:")

if ability == "Fire":
    print("--------------------------------------------------------------------------------------------")
    print("Your chosen hero is a", hero, "with a weapon of", weapon,",and an ability of", ability, "that ended up burning the village along with the goblins, turning you into a villain. HAHAHA!")

elif ability == "Heal":
    print("--------------------------------------------------------------------------------------------")
    print("Your chosen hero is a", hero, "with a weapon of", weapon,",and an ability of", ability,'.')
    print("You healed everyone in the village and executed every last of the goblins.")
  
elif ability == "Teleport":
    print("--------------------------------------------------------------------------------------------")
    print("Your chosen hero is a", hero, "with a weapon of", weapon,",and an ability of", ability,'.')
    print("After using your teleportation, you've ended up telepoting to another dimension where there is no life but only darkness")
    print("You died all alone. HAHAHA!")

elif ability == "Time":
    print("--------------------------------------------------------------------------------------------")
    print("Your chosen hero is a", hero, "with a weapon of", weapon,",and an ability of", ability,'.')
    print("You've traveled back in time to prepare before the horde of goblin leading to victory!")

elif ability == "Nature":
    print("--------------------------------------------------------------------------------------------")
    print("Your chosen hero is a", hero, "with a weapon of", weapon,",and an ability of", ability,'.')
    print("You,ve restored the village and made it better, but you didn't kill the goblins and ended up killing you")
    
print("--------------------------------------------------------------------------------------------")
print("Thanks for playing! And still in progress!")

