from Encounter import encounter
from Home import go_home


def forest(home, inventory, sheet, storypath):
    print("You are in the forest. A bear attacks you!")
    encounter(inventory, sheet, 10, 20, 0, 1, 8)
    sheet.brawn.grow(1)
    sheet.brain.shrink(1)
    go_home(home, sheet, inventory, storypath)

