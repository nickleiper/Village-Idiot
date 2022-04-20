from CharacterAttribute import Sheet
from CharacterBuilder import build_me_a_pc
from Inventory import Inventory
from Encounter import encounter


def main():
    pc = Sheet()
    inventory = Inventory()
    build_me_a_pc(pc, inventory)
    encounter(inventory, pc, 10, 10, 0, 5, 8)


if __name__ == '__main__':
    main()
