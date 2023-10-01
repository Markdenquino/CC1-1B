#Story game
import sys
import time

print("A horde of goblin raided the Willow village unguarded. Now it's up to you to become a hero!!")
print("--------------------------------------------------------------------------------------------")

start = input("Do you wish to start your quest (yes/no)? ").lower().strip()

if start == "yes":
    print("--------------------------------------------------------------------------------------------")

    def hero_display(h1, h2, h3, h4, h5):
        print(h1, h2, h3, h4, h5)
        
    hero_display("<Rook>", "<Knight>", "<Bishop>", "<Queen>", "<King>")
    hero_opt = ("Rook", "Knight", "Bishop", "Queen", "King")
    hero = None
    
    while hero not in hero_opt:
        hero = input("Choose your Hero: ").capitalize().strip()
        
        if hero not in hero_opt:
            print("Invalid Hero!")
        else:
            print(f"Your chosen Hero is {hero}")

    arsenal = {"w1": "Cronus' Flesh [Shield]", "w2": "Hade's touch [Scythe]", "w3": "Bolt of Zues [Crossbow]", "w4": "Poseidon's Arsenal [Trident]", "w5": "Last of Gladius [Broad sword]",}
    
    arsenal_display = ["<w1> Cronus' Flesh [Shield]", "<w2> Hade's touch [Scythe]", "<w3> Bolt of Zues [Crossbow]", "<w4> Poseidon's Arsenal [Trident]", "<w5> Last of Gladius [Broad sword]",]
    print("--------------------------------------------------------------------------------------------")

    for x in arsenal_display:
        print(x)
        
    weapon_opt = ("w1", "w2", "w3", "w4", "w5")
    weapon = None
    
    while weapon not in weapon_opt:
        weapon = input("Select a weapon: ").lower().strip()
        
        if weapon not in weapon_opt:
            print("Invalid weapon!")
        else:
            print(f"Your chosen weapon is {arsenal.get(weapon)})")
        print("--------------------------------------------------------------------------------------------")
    def skill_display(a1, a2, a3, a4, a5):
        print(a1, a2, a3, a4, a5)
    
    skill_display("<Fire>", "<Heal>", "<Time>", "<Teleport>", "<Freeze>")
    skill_opt = ("Fire", "Heal", "Time", "Teleport", "Freeze")
    ability = None
    
    while ability not in skill_opt:
        ability = input("Choose your skill: ").capitalize().strip()
        
        if ability not in skill_opt:
            print("Invalid Skill!")
        else:
            print(f"Your chosen skill is <{ability}>")
        print("--------------------------------------------------------------------------------------------")
        
        if ability == "Fire":
            def story1(s1):
                for c in s1:
                    sys.stdout.write(c)
                    sys.stdout.flush()
                    time.sleep(.1)
            story1(f"{hero} used his/her {arsenal.get(weapon)} killing the ruthless king of goblins. Then he/she used {ability} to burn down the remaining goblins. But due to your carelessness, you've ended up burning everyone and the village. Flame is neither your friend or enemy")
        
        elif ability == "Heal":
            def story2(s2):
                for c in s2:
                    sys.stdout.write(c)
                    sys.stdout.flush()
                    time.sleep(.1)
            story2(f"{hero} used his/her {arsenal.get(weapon)} killing the ruthless king of goblins. Then he/she {ability} everyone in the village. During the process, one of a goblin stab your back leading to your death. A sacrifice was made to protect the lives of many")
        
        elif ability == "Time":
            def story3(s3):
                for c in s3:
                    sys.stdout.write(c)
                    sys.stdout.flush()
                    time.sleep(.1)
            story3(f"{hero} used his/her {arsenal.get(weapon)} killing the ruthless king of goblins. But a horde of goblins kept coming so he/she traveled back in time to prevent the raid. After activating his/her {ability}, he/she went back in time and planned a succesful victory. A person who thinks a head of time becomes undefeated")
        
        elif ability == "Teleport":
            def story4(s4):
                for c in s4:
                    sys.stdout.write(c)
                    sys.stdout.flush()
                    time.sleep(.1)
            story4(f"{hero} used his/her {arsenal.get(weapon)} killing the ruthless king of goblins. He/She keeps abusing hi/her teleportaion back and forth but ended up teleporting to unknown dimension. A place where there's no physical, mental, or spiritual that ended up being part of it. Focus on one thing or ended up self-destructing")
        
        elif ability == "Freeze":
            def story5(s5):
                for c in s5:
                    sys.stdout.write(c)
                    sys.stdout.flush()
                    time.sleep(.1)
            story5(f"{hero} used his/her {arsenal.get(weapon)} killing the ruthless king of goblins. Using her/his {ability} become useful and powerful in any circumstances. But when a horde of goblins approached, he/she lost her/his mentality from fear and ending up freezing the whole continent. Calmness overcome everything.")

else:
    print("Okay😢")
      