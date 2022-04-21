def question1(sheet):
    looper = True
    while looper:
        a = input("1. How do your parents make a living?\n"
                  "(A) Town guards - Brawn +1\n"
                  "(B) Clergy members - Brain +1\n"
                  "(C) Small time crooks - Quick +1\n"
                  "(D) Merchants - Charm +1\n"
                  "(E) Cabbage Farmers - Will +1\n")
        if a == "A":
            sheet.brawn.grow(1)
            print("uggg... fuckin' pigs. Well,\n")
            looper = False
        elif a == "B":
            sheet.brain.grow(1)
            print("boooorrrringggg.\n")
            looper = False
        elif a == "C":
            sheet.quick.grow(1)
            print("I like it! Everybody's gotta hustle.\n")
            looper = False
        elif a == "D":
            sheet.charm.grow(1)
            print("Ha! overglorified fishmongers.\n")
            looper = False
        elif a == "E":
            sheet.will.grow(1)
            print("A respectable, if bland, living. Tell me,\n")
            looper = False
        else:
            looper = True


def question2(sheet):
    looper = True
    while looper:
        a = input("2. How did you spend your youth?\n"
                  "(A) Wrestling - Brawn +1\n"
                  "(B) Climbing trees - Quick +1\n"
                  "(C) Chess - Brain +1\n"
                  "(D) Flirting - Charm +1\n"
                  "(E) Drinking - Will +1\n")
        if a == "A":
            sheet.brawn.grow(1)
            print("Meathead... well, I have one last question for you.\n")
            looper = False
        elif a == "B":
            sheet.quick.grow(1)
            print("Little trouble maker... well, I have one last question for you.\n")
            looper = False
        elif a == "C":
            sheet.brain.grow(1)
            print("Yep... you're pretty boring... either way, I have one last question for you.\n")
            looper = False
        elif a == "D":
            sheet.charm.grow(1)
            print("Gross. oh well, what's done is done. I have one last question for you.\n")
            looper = False
        elif a == "E":
            sheet.will.grow(1)
            print("Ah! Someone after my own heart. Just one more question.\n")
            looper = False
        else:
            looper = True


def question3(sheet, inventory):
    looper = True
    while looper:
        a = input("3. How did you survive the last plague?\n"
                  "(A) I beat away the sick with a large stick - Brawn +1\n"
                  "(B) I stayed in the shadows and avoided all human contact - Quick +1\n"
                  "(C) I developed an elaborate herbal remedied that served as a cure - Brain +1\n"
                  "(D) I tricked a local doctor in giving me medicine - Charm +1\n"
                  "(E) I simply willed away the sickness from my body - Will +1\n")
        if a == "A":
            sheet.brawn.grow(1)
            inventory.club.acquire()
            print("Ooga booga, caveman smash. Well, let's got on with this... this seems positive.\n")
            looper = False
        elif a == "B":
            sheet.quick.grow(1)
            print("Smart. That's how you avoid a plague, all there is to do really.\n")
            looper = False
        elif a == "C":
            sheet.brain.grow(1)
            print("I'm quite positive your remedy was useless! but luck is worth something.\n")
            looper = False
        elif a == "D":
            sheet.charm.grow(1)
            print("Clever! Doctors are mostly useless, what with their herbs and whiskey, but that shows cunning!\n")
            looper = False
        elif a == "E":
            sheet.will.grow(1)
            print("Alright... if you say so. Well, let get on with this.")
            looper = False
        else:
            looper = True


def build_me_a_pc(sheet, inventory):
    # Sets all pc stats at 8
    sheet.brawn.grow(8)
    sheet.brain.grow(8)
    sheet.quick.grow(8)
    sheet.charm.grow(8)
    sheet.will.grow(8)
    # Background builder
    print("Welcome to village... It's the worst. Either way... I guess you'll learn that soon enough...\n")
    question1(sheet)
    question2(sheet)
    question3(sheet, inventory)
    sheet.hp.grow(sheet.brawn.value)
    sheet.melee_weapon.grow(round((sheet.brawn.value-10)/2))
    sheet.ranged_weapon.grow(round((sheet.quick.value-10)/2))
    sheet.talk.grow(round((sheet.charm.value-10)/2))
    sheet.intimidate.grow(round((sheet.charm.value-10)/2))
    sheet.retreat.grow(round((sheet.quick.value-10)/2))
    sheet.stealth.grow(round((sheet.quick.value-10)/2))
    sheet.acrobat.grow(round((sheet.quick.value-10)/2))
    sheet.force.grow(round((sheet.brawn.value-10)/2))
    sheet.athlete.grow(round((sheet.brawn.value-10)/2))
    sheet.know.grow(round((sheet.brain.value-10)/2))
    sheet.detect.grow(round((sheet.brain.value-10)/2))
    sheet.brave.grow(round((sheet.will.value-10)/2))
