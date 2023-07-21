import random

# --- Omori Fight Simulator - Space Ex-Boyfriend Fight --- #

class Character:
    def __init__(self, name, hp, skill, atk, heal):
        self.name = name
        self.hp = hp
        self.skill = skill
        self.atk = atk
        self.heal = heal
        self.skill_count = 1


class Food:
    def __init__(self, healed, count):
        self.healed = healed
        self.count = count

    def apply(self, character):
        character.hp += self.healed
        self.count -= 1


class Juice:
    def __init__(self, count):
        self.count = count

    def apply(self, character):
        character.skill_count += 1
        self.count -= 1


Omori = Character("Omori", 125, 200, 100, 10)
Aubrey = Character("Aubrey", 115, 175, 100, 10)
Kel = Character("Kel", 85, 125, 75, 10)
Hero = Character("Hero", 100, 120, 60, 100)

all_characters = [Omori, Aubrey, Kel, Hero]
all_characters_named = {"Omori": Omori, "Aubrey": Aubrey, "Kel": Kel, "Hero": Hero}

CaptSpaceExBoyfriend = {"hp": 1500, "skill": 60, "atk": 80}

all_food = {"Apple": Food(20, 10), "Ramen": Food(50, 3), "Juice": Juice(3)}


def fix_user_input(user_dirty_input):
    user_inpt_upper = user_dirty_input.upper()
    fixed_name = user_inpt_upper[0]

    user_inpt_lower = user_dirty_input.lower()
    fixed_name += user_inpt_lower[1:]
    return fixed_name


def character_move(character):
    character_name = character.name

    if character.hp <= 0:
        character.hp = 0

    print(f"------")

    while True:
        print(f"--{character_name}'s Turn--")
        user_dirty_input = input(f"What will {character.name} do...?  ")
        turn = fix_user_input(user_dirty_input)
        # turn = input(f"What will {character_name} do...?  ")

        if turn == "Fight":
            Boss_hp = CaptSpaceExBoyfriend["hp"] - character.atk
            print(f"{character_name} deals {character.atk} damage")
            CaptSpaceExBoyfriend["hp"] = Boss_hp
            print("Capt.SpaceExBoyfriend's hp is now: ", CaptSpaceExBoyfriend["hp"])
            return

        elif turn == "Heal":
            healed_name = input(f"Who will {character_name} heal...?  ")

            for healed in all_characters:
                if healed.name == healed_name:
                    New_Hp = healed.hp + character.heal
                    print(f"{character_name} healed {healed_name} {character.heal} hp")
                    print(healed_name, "'s hp is now: ", New_Hp)
                    healed.hp = New_Hp
                    return

            print("Selected not existing character's name, returning to the beginning...")

        elif turn == "Skill":
            if character.skill_count <= 0:  # if skill count 0 or less don't deal dmg
                print(character.name, "needs more juice!")

            elif character_name == 'Hero':
                healed_name = input("Who will Hero heal...?  ")
                for healed in all_characters:
                    if healed.name == healed_name:
                        New_Hp = healed.hp + character.skill
                        print(f"{character_name} healed", healed_name, character.skill)
                        print(healed_name, "'s hp is now:", New_Hp)
                        healed.hp = New_Hp
                        character.skill_count -= 1
                        print(character.name, "'s juice is now", character.skill_count)
                        return
            else:
                Boss_hp = CaptSpaceExBoyfriend["hp"] - character.skill
                print(f"{character_name} deals", character.skill, " damage")
                CaptSpaceExBoyfriend["hp"] = Boss_hp
                if CaptSpaceExBoyfriend["hp"] <= 0:
                    CaptSpaceExBoyfriend["hp"] = 0
                character.skill_count -= 1
                print(character.name, "'s juice is now", character.skill_count)
                print("Capt.SpaceExBoyfriend's hp is now: ", CaptSpaceExBoyfriend["hp"])

                return

        elif turn == "Food":  # food function
            user_dirty_input = input(f"What will {character.name} use? ")  # what food will be used
            food_used_name = fix_user_input(user_dirty_input)
            food_used = all_food[food_used_name]

            user_dirty_input = input(f"Who will {character.name} use food on? ")  # who will food be used on
            fed_name = fix_user_input(user_dirty_input)
            fed = all_characters_named[fed_name]
            if food_used.count <= 0:
                print(f"Not enough {food_used_name}. {food_used.count}")
            else:
                food_used.apply(fed)
                print(f"{food_used.count} {food_used_name} left")

        elif turn == "Kill":  # FOR DEBUGGING ONLY
            new_hp = CaptSpaceExBoyfriend["hp"] - 2000
            CaptSpaceExBoyfriend["hp"] = new_hp
            print("Boss has taken 2000 damage...")
            print("The boss's hp is now", CaptSpaceExBoyfriend["hp"])
            return

        else:
            print(f"{character_name} was unable to do that action...")

# end char move #


def any_character_alive(characters):
    for c in characters:
        if c.hp > 0:
            return True
    return False


def boss_turn():
    # CaptSpaceExBoyfriend
    print("------")
    print("", "--CaptSpaceExBoyfriend's Turn--")

    rng_boss_action = random.randint(1, 5)
    # print("rng1 =", rng1)
    rng2_number = random.randint(0, 3)
    rng_character = all_characters[rng2_number]
    # print("rng2 =", rng2)

    if rng_boss_action in [1, 2]:
        print("CaptSpaceExBoyfriend deals", CaptSpaceExBoyfriend["atk"], " damage to", rng_character.name)
        rng_character.hp = rng_character.hp - CaptSpaceExBoyfriend["atk"]
        for character in all_characters:
            if character.hp <= 0:
                character.hp = 0
        print(rng_character.name, "'s hp is now: ", rng_character.hp)

    elif rng_boss_action in [3, 4]:
        print("CaptSpaceExBoyfriend deals", CaptSpaceExBoyfriend["skill"], " damage to Omori and friends")

        for character in all_characters:
            character.hp -= CaptSpaceExBoyfriend["skill"]
            if character.hp <= 0:
                character.hp = 0
            print(character.name, "'s hp is now:", character.hp)
    else:
        if CaptSpaceExBoyfriend["atk"] >= 125:
            New_atk = CaptSpaceExBoyfriend["atk"] + 20
            CaptSpaceExBoyfriend["atk"] = New_atk
            print("CaptSpaceExBoyfriend has flexed and his damage is now", CaptSpaceExBoyfriend["atk"])
        else:
            print("CaptSpaceExBoyfriend deals", CaptSpaceExBoyfriend["atk"], " damage to", rng_character.name)
            rng_character.hp = rng_character.hp - CaptSpaceExBoyfriend["atk"]
            for character in all_characters:
                if character.hp <= 0:
                    character.hp = 0
            print(f"{rng_character.name}'s hp is now: {rng_character.hp}")


def character_dead(character):
    print("------")
    print("--", character.name, "'s Turn--")
    print(f"{character.name} is toast.")


def game():
    round_count = 1
    while any_character_alive(all_characters):
        print("-------")
        print("")
        print("")
        print(f"--- Round {round_count} ---")
        for character in all_characters:
            if character.hp > 0:
                character_move(character)
            elif character.hp == 0:
                character_dead(character)

            if CaptSpaceExBoyfriend["hp"] <= 0:
                return

        boss_turn()
        round_count += 1


#========================================


game()

if CaptSpaceExBoyfriend["hp"] == 0:
    print("Capt. Space ExBoyfriend has been Defeated!")
else:
    print("Omori and friends have been Defeated!")