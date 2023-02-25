# Space ExBoyfriend fight?

Omori = {"hp": 125, "skill": 200, "atk": 100, "heal": 10}
Aubrey = {"hp": 115, "skill": 175, "atk": 100, "heal": 10}
Kel = {"hp": 85, "skill": 125, "atk": 75, "heal": 10}
Hero = {"hp": 100, "skill": 120, "atk": 60, "heal": 100}
CaptSpaceExBoyfriend = {"hp": 1500, "skill": 60, "atk": 80}

while CaptSpaceExBoyfriend["hp"] >= 1 or Omori["hp"] + Aubrey["hp"] + Kel["hp"] + Hero["hp"] == 0:

    ################################################
    # Omori
        print("--Omori's Turn--")
        Omoris_turn = input("What will Omori do...?  ")
        if Omoris_turn == "Fight":
            Boss_hp = CaptSpaceExBoyfriend["hp"] - Omori["atk"]
            print("Omori deals", Omori["atk"], " damage")
            CaptSpaceExBoyfriend["hp"] = Boss_hp
            print("Capt.SpaceExBoyfriend's hp is now: ", CaptSpaceExBoyfriend["hp"])

        elif Omoris_turn == "Heal":

                Omori_heal = input("Who will Omori heal...?  ")
                if Omori_heal == "Aubrey":
                    New_Hp = (Aubrey["hp"]) + (Omori["heal"])
                    print("Omori healed", Omori_heal, Omori["heal"])
                    print(Omori_heal, "'s hp is now: ", New_Hp)
                    Aubrey["hp"] = New_Hp

                elif Omori_heal == "Kel":
                    New_Hp = (Kel["hp"]) + (Omori["heal"])
                    print("Omori healed", Omori_heal, Omori["heal"])
                    print(Omori_heal, "'s hp is now: ", New_Hp)
                    Kel["hp"] = New_Hp

                elif Omori_heal == "Hero":
                    New_Hp = (Hero["hp"]) + (Omori["heal"])
                    print("Omori healed", Omori_heal, Omori["heal"])
                    print(Omori_heal, "'s hp is now: ", New_Hp)
                    Hero["hp"] = New_Hp

                elif Omori_heal == "x":
                    print("You have decided to return")
                else:
                    print("Omori was unable to do that action...")

        elif Omoris_turn == "Skill":
            Boss_hp = CaptSpaceExBoyfriend["hp"] - Omori["skill"]
            print("Omori deals", Omori["skill"], " damage")
            CaptSpaceExBoyfriend["hp"] = Boss_hp
            print("Capt.SpaceExBoyfriend's hp is now: ", CaptSpaceExBoyfriend["hp"])

        elif Omoris_turn == "x":
            print("You have decided to return")
        else:
            print("Omori was unable to do that action...")

    #################################################
    # Aubrey

        print("--Aubrey's Turn--")
        Aubreys_turn = input("What will Aubrey do...?  ")
        if Aubreys_turn == "Fight":
            Boss_hp = CaptSpaceExBoyfriend["hp"] - Aubrey["atk"]
            print("Aubrey deals", Aubrey["atk"], " damage")
            CaptSpaceExBoyfriend["hp"] = Boss_hp
            print("Capt.SpaceExBoyfriend's hp is now: ", CaptSpaceExBoyfriend["hp"])

        elif Aubreys_turn == "Heal":
                Aubrey_heal = input("Who will Aubrey heal...?  ")
                if Aubrey_heal == "Omori":
                    New_Hp = (Omori["hp"]) + (Aubrey["heal"])
                    print("Aubrey healed", Aubrey_heal, Aubrey["heal"])
                    print(Aubrey_heal, "'s hp is now: ", New_Hp)
                    Aubrey["hp"] = New_Hp

                elif Aubrey_heal == "Kel":
                    New_Hp = (Kel["hp"]) + (Aubrey["heal"])
                    print("Aubrey healed", Aubrey_heal, Aubrey["heal"])
                    print(Aubrey_heal, "'s hp is now: ", New_Hp)
                    Kel["hp"] = New_Hp

                elif Aubrey_heal == "Hero":
                    New_Hp = (Hero["hp"]) + (Aubrey["heal"])
                    print("Aubrey healed", Aubrey_heal, Aubrey["heal"])
                    print(Aubrey_heal, "'s hp is now: ", New_Hp)
                    Hero["hp"] = New_Hp

                elif Aubrey_heal == "x":
                    print("You have decided to return")
                else:
                    print("Aubrey was unable to do that action...")

        elif Aubreys_turn == "Skill":
            Boss_hp = CaptSpaceExBoyfriend["hp"] - Aubrey["skill"]
            print("Aubrey deals", Aubrey["skill"], " damage")
            CaptSpaceExBoyfriend["hp"] = Boss_hp
            print("Capt.SpaceExBoyfriend's hp is now: ", CaptSpaceExBoyfriend["hp"])

        elif Aubreys_turn == "x":
             print("You have decided to return")

        else:
             print("Aubrey was unable to do that action...")

#############

        print("--Kel's Turn--")
        Kels_turn = input("What will Kel do...?  ")
        if Kels_turn.lower() == "Fight":
                Boss_hp = CaptSpaceExBoyfriend["hp"] - Kel["atk"]
                print("Kel deals", Kel["atk"], " damage")
                CaptSpaceExBoyfriend["hp"] = Boss_hp
                print("Capt.SpaceExBoyfriend's hp is now: ", CaptSpaceExBoyfriend["hp"])

        elif Kels_turn == "Heal":

                    Kel_heal = input("Who will Kel heal...?  ")
                    if Kel_heal == "Omori":
                        New_Hp = (Omori["hp"]) + (Kel["heal"])
                        print("Kel healed", Kel_heal, Kel["heal"])
                        print(Kel_heal, "'s hp is now: ", New_Hp)
                        Kel["hp"] = New_Hp

                    elif Kel_heal == "Aubrey":
                        New_Hp = (Aubrey["hp"]) + (Kel["heal"])
                        print("Kel healed", Kel_heal, Kel["heal"])
                        print(Kel_heal, "'s hp is now: ", New_Hp)
                        Aubrey["hp"] = New_Hp

                    elif Kel_heal == "Hero":
                        New_Hp = (Hero["hp"]) + (Kel["heal"])
                        print("Kel healed", Kel_heal, Kel["heal"])
                        print(Kel_heal, "'s hp is now: ", New_Hp)
                        Hero["hp"] = New_Hp

                    elif Kel_heal == "x":
                        print("You have decided to return")
                    else:
                        print("Kel was unable to do that action...")

        elif Kels_turn == "Skill":
                Boss_hp = CaptSpaceExBoyfriend["hp"] - Kel["skill"]
                print("Kel deals", Kel["skill"], " damage")
                CaptSpaceExBoyfriend["hp"] = Boss_hp
                print("Capt.SpaceExBoyfriend's hp is now: ", CaptSpaceExBoyfriend["hp"])

        elif Kels_turn == "x":
                print("You have decided to return")
        else:
                print("Kel was unable to do that action...")


    ########################################################
    # Hero

        print("--Hero's Turn--")
        Heros_turn = input("What will Hero do...?  ")
        if Heros_turn == "Fight":
            Boss_hp = CaptSpaceExBoyfriend["hp"] - Hero["atk"]
            print("Hero deals", Hero["atk"], " damage")
            CaptSpaceExBoyfriend["hp"] = Boss_hp
            print("Capt.SpaceExBoyfriend's hp is now: ", CaptSpaceExBoyfriend["hp"])

        elif Heros_turn == "Heal":
            while True:
                Hero_heal = input("Who will Hero heal...?  ")
                if Hero_heal == "Omori":
                    New_Hp = (Omori["hp"]) + (Hero["heal"])
                    print("Hero healed", Hero_heal, Hero["heal"])
                    print(Hero_heal, "'s hp is now: ", New_Hp)
                    Hero["hp"] = New_Hp
                    break
                elif Hero_heal == "Aubrey":
                    New_Hp = (Aubrey["hp"]) + (Hero["heal"])
                    print("Hero healed", Hero_heal, Hero["heal"])
                    print(Hero_heal, "'s hp is now: ", New_Hp)
                    Aubrey["hp"] = New_Hp
                    break
                elif Hero_heal == "Kel":
                    New_Hp = (Kel["hp"]) + (Hero["heal"])
                    print("Hero healed", Hero_heal, Hero["heal"])
                    print(Hero_heal, "'s hp is now: ", New_Hp)
                    Kel["hp"] = New_Hp
                    break
                elif Hero_heal == "x":
                    print("You have decided to return")
                else:
                    print("Hero was unable to do that action...")
                    break

        elif Heros_turn == "Skill":
            Hero_skill = input("Who will Hero heal...?  ")
            if Hero_skill == "Omori":
                New_Hp = (Omori["hp"]) + (Hero["skill"])
                print("Hero healed", Hero_skill, Hero["skill"])
                print(Hero_skill, "'s hp is now: ", New_Hp)
                Hero["hp"] = New_Hp
            elif Hero_skill == "Aubrey":
                New_Hp = (Aubrey["hp"]) + (Hero["skill"])
                print("Hero healed", Hero_skill, Hero["skill"])
                print(Hero_skill, "'s hp is now: ", New_Hp)
                Aubrey["hp"] = New_Hp
            elif Hero_skill == "Kel":
                New_Hp = (Kel["hp"]) + (Hero["skill"])
                print("Hero healed", Hero_skill, Hero["skill"])
                print(Hero_skill, "'s hp is now: ", New_Hp)
                Kel["hp"] = New_Hp
            else:
                print("Hero was unable to do that action...")

        else:
            print("Hero was unable to do that action...")

    ##########################################################
    # CaptSpaceExBoyfriend

        print("--CaptSpaceExBoyfriend's Turn--")
        import random
        rng1 = random.randint(1, 3)
        # print("rng1 =", rng1)
        rng2 = random.randint(1, 4)
        # print("rng2 =", rng2)

        if rng2 == 1:
            rng2 = "Omori"
        elif rng2 == 2:
            rng2 = "Aubrey"
        elif rng2 == 3:
            rng2 = "Kel"
        else:
            rng2 = "Hero"

        if rng1 == 1:
            CSEBs_turn = "Fight"
            print("CaptSpaceExBoyfriend deals", CaptSpaceExBoyfriend["atk"], " damage to", rng2)
            rng2["hp"] = rng2["hp"] - CaptSpaceExBoyfriend["atk"]
            print(rng2, "'s hp is now: ", rng2["hp"])
        elif rng1 == 2:
            CSEBs_turn = "Skill"
            print("CaptSpaceExBoyfriend deals", CaptSpaceExBoyfriend["skill"], " damage to Omori and friends")
            Omori["hp"] - CaptSpaceExBoyfriend["skill"]
            Aubrey["hp"] - CaptSpaceExBoyfriend["skill"]
            Kel["hp"] - CaptSpaceExBoyfriend["skill"]
            Hero["hp"] - CaptSpaceExBoyfriend["skill"]
            print("Omori's hp is now: ", Omori["hp"])
            print("Aubrey's hp is now: ", Aubrey["hp"])
            print("Kel's hp is now: ", Kel["hp"])
            print("Hero's hp is now: ", Hero["hp"])
        else:
            CSEBs_turn = "Buff"
            New_atk = CaptSpaceExBoyfriend["atk"] + 20
            CaptSpaceExBoyfriend["atk"] = New_atk
            print("CaptSpaceExBoyfriend has flexed and his damage is now", CaptSpaceExBoyfriend["atk"])


#######################
if CaptSpaceExBoyfriend["hp"] <= 0:
    print("Capt. Space ExBoyfriend has been Defeated!")
if Omori["hp"] + Aubrey["hp"] + Kel["hp"] + Hero["hp"] == 0:
    print("Omori and friends have been Defeated!")