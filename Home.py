'''Home is the central landing place between storylines. As the game progresses, home becomes nicer.'''


class Home:
    def __init__(self):
        self.progression = 1
        self.poor = "You are home. It is a pleasant enough place. There's a field in which a goat frolics, a large\n" \
                    "squash patch, and a log and thatch home with a stone foundation that contains your bedroom, \n" \
                    "kitchen, pantry, and living room. You are very poor."
        self.medium = "You are home. Having made your name as an adventure, there are now two goats frolicking in\n" \
                      "the field alongside an ox, a dairy cow, and a donkey which operates a mill. A small patch \n" \
                      "land has been dedicated to growing tomatoes, and your old squash patch is looking very \n" \
                      "healthy. Your home is now a two story affair with plank walls, a cobble foundation and two\n" \
                      "fireplaces. You now have a servant named Gretchen who will make you meals."
        self.wealthy = "You are home. You are now one of the most successful adventures in the land and you have a\n" \
                       "home to match, sturdy enough to last through the ages. In addition to Gretchen, a small team\n" \
                       "of servants is prepared to care for your wounds."

    def progress(self):
        self.progression += 1

    def what_do_you_do(self, storypath):
        print("What do you do? (Type command)")  # !!! forest is loading twice for some reason!!!
        if storypath.market.available:
            print(storypath.market.prompt)
        if storypath.forest.available:
            print(storypath.forest.prompt)
        if storypath.tall_grass.available:
            print(storypath.tall_grass.prompt)


def home_write_up(home, sheet, inventory, storypath):
    if home.progression == 1:
        print(home.poor)
    elif home.progression == 2:
        print(home.medium)
    elif home.progression == 3:
        print(home.wealthy)
    else:
        print(home.wealthy)
    looper = True
    healable = True
    while looper:
        home.what_do_you_do(storypath)
        if healable:
            if home.progression == 1:
                print("SQUASH - Grab a squash and eat it (+2 HP)")
            elif home.progression == 2:
                print("EAT - Have Gretchen prepare you a meal (+4 HP)")
            elif home.progression == 3:
                print("TREAT - Have your servants tend to you wounds (+8 HP")
        a = input()
        if a == "SQUASH":
            sheet.hp.heal(2)
            print("Yuck! Raw squash with a hint mildew. You have " + str(sheet.hp.value) + " HP.")
            healable = False
            looper = True
        elif a == "EAT" and home.progression > 1:
            sheet.hp.heal(4)
            print("A delicious dense feast. Put those calories to good use! You're neighbors are starving.You have "
                  + str(sheet.hp.value) + " HP.")
            healable = False
            looper = True
        elif a == "TREAT" and home.progression > 2:
            sheet.hp.heal(8)
            print("Ow! Did they just rub shit in your wounds? Science I guess...Y ou have " + str(sheet.hp.value) +
                  " HP.")
            healable = False
            looper = True
        elif a == "MARKET" and storypath.market.available:
            storypath.market.go_on_quest(home, inventory, sheet, storypath)
            looper = False
        elif a == "FOREST" and storypath.forest.available:
            storypath.forest.go_on_quest(home, inventory, sheet, storypath)
            looper = False
        elif a == "GRASS" and storypath.tall_grass.available:
            storypath.tall_grass.go_on_quest(home, inventory, sheet, storypath)
            looper = False
        else:
            print("You can't seem to do that right now...")
            healable = True
            looper = True


def go_home(home, sheet, inventory, storypath):
    print("Do you want to go home and keep playing?\nY - yes\nN - no")
    looper = True
    while looper:
        a = input()
        if a == "Y":
            home_write_up(home, sheet, inventory, storypath)
            looper = False
        elif a == "N":
            print("Thanks for playing!")
            looper = False
        else:
            print("Yes or no I'm afraid.")
            looper = True

