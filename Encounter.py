from random import randint


def roll(low, high, mod):
    return randint(low, high) + mod


def weapon_checker(inventory):
    print("What do you do? (type command)")
    if inventory.fists.possession:
        print("'PUNCH' - Punch em' with Fists")
    if inventory.club.possession:
        print("'CLUB' - Club em' with Club")
    if inventory.dagger.possession:
        print("'SHANK' - Shank em' with Dagger")
    if inventory.sword.possession:
        print("'STAB' - Stab em' with Sword")
    if inventory.great_sword.possession:
        print("'SLASH' - Slash em' with Great Sword")
    if inventory.war_axe.possession:
        print("'HACK' - Hack em' with War Axe")
    if inventory.slingshot.possession:
        print("'PING' - Ping em' with Slingshot")
    if inventory.bow_arrow.possession:
        print("'SHOOT' - Shoot em' with Bow and Arrow")
    if inventory.crossbow.possession:
        print("'SNIPE' - Snipe em' with Crossbow")
    if inventory.musket.possession:
        print("'BLAST' - Blast em' with musket")


def weapon_selector(inventory):
    looper = True
    while looper:
        a = input()
        if a == "PUNCH" and inventory.fists.possession:
            return inventory.fists
        elif a == "STAB" and inventory.sword.possession:
            return inventory.sword
        elif a == "CLUB" and inventory.club.possession:
            return inventory.club
        elif a == "SHANK" and inventory.dagger.possession:
            return inventory.dagger
        elif a == "SLASH" and inventory.great_sword.possession:
            return inventory.great_sword
        elif a == "HACK" and inventory.war_axe.possession:
            return inventory.war_axe
        elif a == "PING" and inventory.slingshot.possession:
            return inventory.slingshot
        elif a == "SHOOT" and inventory.bow_arrow.possession:
            return inventory.bow_arrow
        elif a == "SNIPE" and inventory.crossbow.possession:
            return inventory.crossbow
        elif a == "BLAST" and inventory.musket.possession:
            return inventory.musket
        else:
            print("You don't seem to be able to do that yet...")
            looper = True


def use_weapon(implement, sheet, ac):
    score = roll(1, 20, implement.bonus + sheet.melee_weapon.value)
    if score >= ac:
        print("You hit!")
        return roll(1, implement.damage, round((sheet.brawn.value-10)/2))
    else:
        print("You miss!")
        return 0


def encounter(inventory, sheet, ac, hit_points, bonus, damage_low, damage_high):
    hp = hit_points
    while hp > 0 and sheet.hp.value > 0:
        weapon_checker(inventory)
        use_weapon(weapon_selector(inventory), sheet, ac)
        counter = roll(1, 20, bonus)
        if counter >= sheet.quick.value:
            sheet.hp.value -= roll(damage_low, damage_high, 0)
            print("They hit you back!")
        else:
            print("They miss!")
    if sheet.hp.value <= 0:
        print("You're dead!")
    else:
        print("You've killed the beast!")


"""THIS CODE IS A SHITSHOW. I NEED TO FIGURE OUT HOW IT WORKS, BUT BASICALLY, weapon_checker JUST LISTS ALL THE WEAPONS
THE PLAYER POSSESSES, THEN weapon_selector PROMPTS THE PLAYER TO SELECT A WEAPON AND RETURNS WHICH WEAPON IS USED. 
use_weapon THEN USES THE WEAPON FROM weapon_selector AND roll FOR HIT AND DAMAGE. (ALL REFERENCING THE CLASS)

EVERY ATTACK FROM THE PLAYER OPENS THE PLAYER UP TO A COUNTER ATTACK. THAT'S ALL HANDLED IN THE ENCOUNTER FUNCTION"""
