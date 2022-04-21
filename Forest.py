from Encounter import encounter
from Home import go_home


def forest(home, sheet, inventory, storypath):
    print("You are in the forest. A bear attacks you!")
    encounter(sheet, inventory, 10, 20, 0, 1, 8)
    sheet.brawn.grow(1)
    sheet.brain.shrink(1)
    go_home(home, sheet, inventory, storypath)

