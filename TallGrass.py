from Encounter import encounter
from Home import go_home
from random import randint

random_table = [[12, 10, 1, 1, 4, "You've started a bandit counting his gold"],
                [10, 8, 0, 2, 6, "An innocent deer looks up at you in horror"],
                [15, 5, 4, 1, 2, "A mangy coyote glares at you."],
                [7, 15, -3, 4, 6, "You've awoken the town drunk. With a mighty half-awake belch, he prepares to "
                                  "attack"]]


def tall_grass(home, sheet, inventory, storypath):
    beast = randint(0, 3)
    looper = True
    while looper:
        print(random_table[beast][5])
        print("What do you do?\nFIGHT - try and beat this thing to a pulp.\nFLEE - run away")
        if beast == 3:
            print("SNEAK - try and sneak around\nSTEAL - try and take his wallet without him noticing")
        elif beast == 0:
            print("TALK - 'my good sir, do you not think we would be better off if I simply walked away and said "
                  "nothing of this to anyone.'\n"
                  "STEAL - try and take the gold without him noticing\n")
        elif beast == 1:
            print("PET - pet this sweet critter and go home.")
        a = input()
        if a == "FIGHT":
            encounter(sheet, inventory, random_table[beast][0], random_table[beast][1], random_table[beast][2],
                      random_table[beast][3], random_table[beast][4])
            sheet.brawn.grow(1)
            go_home(home, sheet, inventory, storypath)
            looper = False
        elif a == "FLEE":
            print("Coward... You manage to get away.")
            go_home(home, sheet, inventory, storypath)
            looper = False
        elif a == "PET" and beast == 1:
            print("You pet the deer. It reluctantly accepts and scurries off.")
            sheet.will.grow(1)
            go_home(home, sheet, inventory, storypath)
            looper = False
        elif a == "TALK" and beast == 0:
            check = sheet.charm.value + randint(1, 20)
            if 13 <= check < 16:
                print(" Bandit: 'Very well, but I've seen that cabin of your's. You best not rat me out.'\nThe bandit "
                      "leaves with his gold.")
                sheet.charm.grow(1)
                go_home(home, sheet, inventory, storypath)
                looper = False
            elif check >= 16:
                print("Bandit: 'Ha! I should hardly think an upstanding individual like yourself would even dream of\n"
                      "contacting the authorities. Say, have my dagger as a sort of thank you. A fine piece of steel\n"
                      "that is.'\nThe bandit gives you his dagger and leaves.")
                inventory.dagger.acquire()
                sheet.charm.grow(1)
                go_home(home, sheet, inventory, storypath)
                looper = False
            else:
                print("Bandit: 'I'm going to carve you up knave.'\nThe bandit attacks!")
                encounter(sheet, inventory, random_table[beast][0], random_table[beast][1], random_table[beast][2],
                          random_table[beast][3], random_table[beast][4])
                sheet.charm.grow(1)
                go_home(home, sheet, inventory, storypath)
                looper = False
        elif a == "STEAL" and beast == 0:
            check = sheet.pickpocket.value + randint(1, 20)
            if check >= 18:
                sheet.pickpocket.grow(1)
                print("Well, I was quite certain that wasn't going to go well... but you've made off with the Bandit's "
                      "gold!")
                inventory.bandit_gold.acquire()
                go_home(home, sheet, inventory, storypath)
                looper = False
            else:
                print("That was rather ill-advised. The bandit draws and prepares to strike.")
                encounter(sheet, inventory, random_table[beast][0], random_table[beast][1], random_table[beast][2],
                          random_table[beast][3], random_table[beast][4])
                sheet.pickpocket.grow(1)
                go_home(home, sheet, inventory, storypath)
                looper = False
        elif a == "SNEAK" and beast == 3:
            check = sheet.stealth.value + randint(1, 20)
            if check >= 12:
                print("He's effectively asleep. It was never going to be that hard. You get by without problem.")
                sheet.stealth.grow(1)
                go_home(home, sheet, inventory, storypath)
                looper = False
            else:
                print("He sees and has decided to pummel you.")
                encounter(sheet, inventory, random_table[beast][0], random_table[beast][1], random_table[beast][2],
                          random_table[beast][3], random_table[beast][4])
                sheet.stealth.grow(1)
                go_home(home, sheet, inventory, storypath)
                looper = False
        elif a == "STEAL" and beast == 3:
            check = sheet.pickpocket.value + randint(1, 20)
            if check >= 14:
                print("You've got his wallet! He falls back asleep and you're free to go home.")
                sheet.pickpocket.grow(1)
                inventory.drunk_wallet.acquire()
                go_home(home, sheet, inventory, storypath)
                looper = False
            else:
                print("Oh no... he's just come to his senses with your hand in his ass pocket. He says 'I will kill "
                      "you.' maybe he's joking?")
                encounter(sheet, inventory, random_table[beast][0], random_table[beast][1], random_table[beast][2],
                          random_table[beast][3], random_table[beast][4])
                sheet.pickpocket.grow(1)
                go_home(home, sheet, inventory, storypath)
                looper = False
        else:
            print("Sorry, that's not an option right now.")
            looper = True



# sheet, inventory, ac, hit_points, bonus, damage_low, damage_high
