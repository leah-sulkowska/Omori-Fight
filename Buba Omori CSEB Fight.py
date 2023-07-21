import random

# --- Omori Fight Simulator - Space Ex-Boyfriend Fight --- #

Omori = {"name": "Omori", "hp": 125, "skill": 200, "atk": 100, "heal": 10, "skill_count": 1}
Aubrey = {"name": "Aubrey", "hp": 115, "skill": 175, "atk": 100, "heal": 10, "skill_count": 1}
Kel = {"name": "Kel", "hp": 85, "skill": 125, "atk": 75, "heal": 10, "skill_count": 1}
Hero = {"name": "Hero", "hp": 100, "skill": 120, "atk": 60, "heal": 100, "skill_count": 1}

all_characters = [Omori, Aubrey, Kel, Hero]
all_characters_named = {"Omori": Omori, "Aubrey": Aubrey, "Kel": Kel, "Hero": Hero}

CaptSpaceExBoyfriend = {"hp": 1500, "skill": 60, "atk": 80}

food = {"apple": 20, "ramen": 50, "juice": 1}
num = {"apple": 10, "ramen": 3, "juice": 3}

round_count = 1

def fix_user_input(user_dirty_input):
    user_inpt_upper = user_dirty_input.upper()
    fixed_name = user_inpt_upper[0]

    user_inpt_lower = user_dirty_input.lower()
    fixed_name += user_inpt_lower[1:]
    return fixed_name


def character_move(character):
    character_name = character['name']

    if character["hp"] <= 0:
        character["hp"] = 0

    print(f"------")

    while True:
        print(f"--{character_name}'s Turn--")
        user_dirty_input = input(f"What will {character['name']} do...?  ")
        turn = fix_user_input(user_dirty_input)
        # turn = input(f"What will {character_name} do...?  ")

        if turn == "Fight":
            Boss_hp = CaptSpaceExBoyfriend["hp"] - character["atk"]
            print(f"{character_name} deals", character["atk"], " damage")
            CaptSpaceExBoyfriend["hp"] = Boss_hp
            print("Capt.SpaceExBoyfriend's hp is now: ", CaptSpaceExBoyfriend["hp"])
            return

        elif turn == "Heal":
            healed_name = input(f"Who will {character_name} heal...?  ")

            for healed in all_characters:
                if healed["name"] == healed_name:
                    New_Hp = (healed["hp"]) + (character["heal"])
                    print(f"{character_name} healed", healed_name, character["heal"], "hp")
                    print(healed_name, "'s hp is now: ", New_Hp)
                    healed["hp"] = New_Hp
                    return

            print("Selected not existing character's name, returning to the beginning...")

        elif turn == "Skill":
            if character["skill_count"] <= 0:  # if skill count 0 or less don't deal dmg
                print(character["name"], "needs more juice!")

            elif character_name == 'Hero':
                healed_name = input("Who will Hero heal...?  ")
                for healed in all_characters:
                    if healed["name"] == healed_name:
                        New_Hp = (healed["hp"]) + (character["skill"])
                        print(f"{character_name} healed", healed_name, character["skill"])
                        print(healed_name, "'s hp is now:", New_Hp)
                        healed["hp"] = New_Hp
                        new_count = character["skill_count"] - 1
                        character["skill_count"] = new_count
                        print(character["name"], "'s juice is now", character["skill_count"])
                        return
            else:
                Boss_hp = CaptSpaceExBoyfriend["hp"] - character["skill"]
                print(f"{character_name} deals", character["skill"], " damage")
                CaptSpaceExBoyfriend["hp"] = Boss_hp
                if CaptSpaceExBoyfriend["hp"] <= 0:
                    CaptSpaceExBoyfriend["hp"] = 0
                new_count = character["skill_count"] - 1
                character["skill_count"] = new_count
                print(character["name"], "'s juice is now", character["skill_count"])
                print("Capt.SpaceExBoyfriend's hp is now: ", CaptSpaceExBoyfriend["hp"])

                return

        elif turn == "Food":  # food function
            user_dirty_input = input(f"What will {character['name']} use? ")  # what food will be used
            food_used = fix_user_input(user_dirty_input)

            user_dirty_input = input(f"Who will {character['name']} use food on? ")  # who will food be used on
            fed_name = fix_user_input(user_dirty_input)
            if fed_name in all_characters_named:
                fed = all_characters_named[fed_name]
                # user_dirty_input = input(f"What will {character['name']} use? ")  # what food will be used
                # food_used = fix_user_input(user_dirty_input)
                if food_used == "Apple":
                    if num["apple"] <= 0:
                        print("Not enough ramen. (", num["apple"], ")")
                    else:
                        fed["hp"] += food["apple"]
                        new_num = num["apple"] - 1
                        num["apple"] = new_num
                        print(num["apple"], " apples left")
                        print(f"{fed['name']}'s hp is now {fed['hp']}")
                        return

                elif food_used == "Ramen":
                    if num["ramen"] <= 0:
                        print("Not enough ramen. (", num["ramen"], ")")

                    else:
                        fed["hp"] += food["ramen"]
                        new_num = num["ramen"] - 1
                        num["ramen"] = new_num
                        print(num["ramen"], " ramen left")
                        print(f"{fed['name']}'s hp is now {fed['hp']}")
                        return

                # elif food_used == "Juice":
                #     if juice_num >= 1:
                #         fed["skill_count"] += food["juice"]
                #         juice_num -= 1
                #         print(f"{fed['name']}'s juice is now {fed['skill_count']}")
                #         return
                #     else:
                #         print("Not enough juice.")

                elif food_used == "Juice":
                    if num["juice"] <= 0:
                        print("Not enough juice. (", num["juice"], ")")

                    else:
                        fed["skill_count"] += food["juice"]
                        new_num = num["juice"] - 1
                        num["juice"] = new_num
                        print(num["juice"], " juice left")
                        print(f"{fed['name']}'s juice is now {fed['skill_count']}")
                        return

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
        if c["hp"] > 0:
            return True

    return False


def boss_turn():
    # CaptSpaceExBoyfriend
    print("------")
    print("", "--CaptSpaceExBoyfriend's Turn--")

    rng1 = random.randint(1, 5)
    # print("rng1 =", rng1)
    rng2_number = random.randint(0, 3)
    rng2 = all_characters[rng2_number]
    # print("rng2 =", rng2)

    if rng1 == 1 or rng1 == 2:
        print("CaptSpaceExBoyfriend deals", CaptSpaceExBoyfriend["atk"], " damage to", rng2["name"])
        rng2["hp"] = rng2["hp"] - CaptSpaceExBoyfriend["atk"]
        for character in all_characters:
            if character["hp"] <= 0:
                character["hp"] = 0
        print(rng2["name"], "'s hp is now: ", rng2["hp"])

    elif rng1 == 3 or rng1 == 4:
        print("CaptSpaceExBoyfriend deals", CaptSpaceExBoyfriend["skill"], " damage to Omori and friends")
        # Omori_New_Hp = Omori["hp"] - CaptSpaceExBoyfriend["skill"]
        # Omori["hp"] = Omori_New_Hp
        # Aubrey_New_Hp = Aubrey["hp"] - CaptSpaceExBoyfriend["skill"]
        # Aubrey["hp"] = Aubrey_New_Hp
        # Kel_New_Hp = Kel["hp"] - CaptSpaceExBoyfriend["skill"]
        # Kel["hp"] = Kel_New_Hp
        # Hero_New_Hp = Hero["hp"] - CaptSpaceExBoyfriend["skill"]
        # Hero["hp"] = Hero_New_Hp

        for character in all_characters:
            new_hp = character["hp"] - CaptSpaceExBoyfriend["skill"]
            character["hp"] = new_hp

        for character in all_characters:
            if character["hp"] <= 0:
                character["hp"] = 0
        for character in all_characters:
            print(character["name"], "'s hp is now:", character["hp"])

        # print("Omori's hp is now: ", Omori["hp"])
        # print("Aubrey's hp is now: ", Aubrey["hp"])
        # print("Kel's hp is now: ", Kel["hp"])
        # print("Hero's hp is now: ", Hero["hp"])
    else:
        if CaptSpaceExBoyfriend["atk"] >= 125:
            New_atk = CaptSpaceExBoyfriend["atk"] + 20
            CaptSpaceExBoyfriend["atk"] = New_atk
            print("CaptSpaceExBoyfriend has flexed and his damage is now", CaptSpaceExBoyfriend["atk"])
        else:
            print("CaptSpaceExBoyfriend deals", CaptSpaceExBoyfriend["atk"], " damage to", rng2["name"])
            rng2["hp"] = rng2["hp"] - CaptSpaceExBoyfriend["atk"]
            for character in all_characters:
                if character["hp"] <= 0:
                    character["hp"] = 0
            print(rng2["name"], "'s hp is now: ", rng2["hp"])



def character_dead(character):
    print("------")
    print("--", character["name"], "'s Turn--")
    print(character["name"], "is toast.")

def game(round_count):
    while any_character_alive(all_characters):
        print("-------")
        print("")
        print("")
        print(f"--- Round {round_count} ---")
        for character in all_characters:
            if character["hp"] > 0:
                character_move(character)
            elif character["hp"] == 0:
                character_dead(character)

            if CaptSpaceExBoyfriend["hp"] <= 0:
                return

        boss_turn()
        round_count += 1


#========================================


game(round_count)

if CaptSpaceExBoyfriend["hp"] == 0:
    print("Capt. Space ExBoyfriend has been Defeated!")
else:
    print("Omori and friends have been Defeated!")