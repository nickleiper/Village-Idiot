from Home import go_home


def market(home, inventory, sheet, storypath):
    print("You are in the market.")
    storypath.market.toggle_complete(True)
    storypath.market.toggle_available(False)
    go_home(home, inventory, sheet, storypath)
