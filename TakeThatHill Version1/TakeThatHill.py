# "Take That Hill" Computer Assisted Wargame
# Version 1.0
#
# Mark Flanagan 16/05/2020
# Simulation Engine
#
# Libraries
#
from random import *
#
def dice_roll():
    # Dice 1
    dice = randint(1,6)
    return dice
#
#
print ()
print ("This is Take That Hill")
print ()
#
# Variable Initialisation
#
turns_played = 1
blue_hits = 0
red_hits = 0
#
# Troop Status
#
section1_status = "Active"
section2_status = "Active"
section3_status = "Active"
german_status = "Active"
#
# Repeat Game Block while the "The hill has not been taken!"
#
# Game Board:
#
# Row 1: A, A1, A2, A3, A4
# Row 2: B, B1, B2, B3, B4, B5 
# Row 3: C, C1, C2, C3, C4
#
# Data Entry: Position of British Sections
#
print ("What are the British Starting Positions")
section1_location = input("Where is Section 1?[A, B or C]").upper()
section2_location = input("Where is Section 2?[A, B or C]").upper()
section3_location = input("Where is Section 3?[A, B or C]").upper()
leader_in_section = int(input("Which section is the leader with? [1, 2, or 3]"))
print ()
# Note: The German Section is always in B5
german_location = "B5" 
while True:
    print ("British Phase: Turn", turns_played)
    #
    # Show locations of British troops
    # Reset Leader Hex as the Leader could always jump between squads
    #
    leader_hex = None
    if leader_in_section == 1:
        leader_hex = section1_location
    elif leader_in_section == 2:
        leader_hex = section2_location
    elif leader_in_section == 3:
        leader_hex = section3_location
    else:
        # Report [Logic Error] Undefined Leader Position so assign leader back to Section 1  
        leader_hex = section1_location
        print ("Reporting program bug - Leader not Assigned to Section")
    #
    # British Sections 1..3
    #
    # Section 1
    if leader_in_section == 1:
        print ("Section 1 is", section1_status, "being located in hex:", section1_location, "with the Platoon Leader")
    else:
        print ("Section 1 is", section1_status, "being located in hex:", section1_location)
    # Section 2
    if leader_in_section == 2:
        print ("Section 2 is", section2_status, "being located in hex:", section2_location, "with the Platoon Leader")
    else:
        print ("Section 2 is", section2_status, "being located in hex:", section2_location)
    # Section 3
    if leader_in_section == 3:
        print ("Section 3 is", section3_status, "being located in hex:", section3_location, "with the Platoon Leader")
    else:
        print ("Section 3 is", section3_status, "being located in hex:", section3_location)     
    print ()
    #
    # Game Block
    # Sequence of Play for Turn
    #
    # British Phase
    # British Orders: THey will either Move or Fire
    # Move
    print ()
    print ("British Move")
    #
    # Does the Leader Move?
    # Note: The Leader is always Active
    ans0 = input ("Do you want to move the leader to another section? [1,2,3 or N]")
    if ans0.upper() != "N":
        try:
            if int(ans0) in [ 1, 2, 3]:
                # Which Section?
                leader_in_section = int (ans0)
                print ("The Leader has moved to Section", ans0)
            else:
                prinf ("Unexpected Input", ans0, "the Leader stays where they are.")
        except ValueError as msg:
            print ("Unexpected input:", msg, "Leader stays where he is")
    #
    # Which Sections Move
    #
    if section1_status == "Active":
        ans1 = input ("Do you want to move Section 1 [Hex or N]?")
        ans1.upper()
        if ans1 != "N":
            # Section used its action to move
            section1_location = ans1
            section1_status = "Spent"
    if section2_status == "Active":
        ans2 = input ("Do you want to move Section 2 [Hex or N]?")
        ans2 = ans2.upper()
        if ans2 != "N":
            # Section used its action to move
            section2_location = ans2
            section2_status = "Spent"
    if section3_status == "Active":
        ans3 = input ("Do you want to move Section 3 [Hex or N]?")
        ans3 = ans3.upper()
        if ans3 != "N":
            # Section used its action to move
            section3_location = ans3
            section3_status = "Spent"
    print ("End of British Movement")
    print ()
    #
    # British Fire
    #
    print ("British Fire")
    if section1_status == "Active":
        fire1 = input ("Section 1 Fires at B5, does it hit?")
        section1_status = "Spent"
        if fire1.upper() == "Y":
            # Section 1 fires and hits the Germans in B5
            print ("Good shot- Section 1")
            red_hits += 1
            german_status = "Spent"
    if section2_status == "Active":
        fire2 = input ("Section 2 Fires at B5, does it hit?")
        section2_status = "Spent"
        if fire2.upper() == "Y":
            # Section 2 fires and hits the Germans in B5
            print ("Good shot - Section 2")
            red_hits += 1
            german_status = "Spent"
    if section3_status == "Active":
        fire3 = input ("Section 3 Fires at B5, does it hit?")
        section3_status = "Spent"
        if fire3.upper() == "Y":
            # Section 2 fires and hits the Germans in B5
            print ("Good Shot - Section 3")
            red_hits += 1
            german_status = "Spent"
    print ("End of British Fire")
    print ()
    #
    # British Rally
    #
    # The British Leader is in which Hex?
    leader_location = ""
    if leader_in_section == 1:
        leader_location = section1_location
    elif leader_in_section == 2:
        leader_location = section2_location
    elif leader_in_section == 3:
        leader_location = section3_location
    else:
        print ("Exception: Don't know where the leader is!")
    
    print ("British Rally Attempt")
    if section1_status == "Spent":
        if section1_location == leader_location:
                print ("Leader in same Hex - Section 1 Auto Rally")
                section1_status = "Active"
        else: 
            rally1 = input ("Does Section 1 Rally[Y or N]?")
            if rally1.upper() == "Y":
                # Section 1 is Rallied
                print ("Huzzah - Section 1 is rallied")
                section1_status = "Active"
    if section2_status == "Spent":
        if section2_location == leader_location:
            print ("Leader in same Hex - Section 2 Auto Rally")
            section2_status = "Active"
        else:
            rally2 = input ("Does Section 2 Rally[Y or N]?")
            if rally2.upper() == "Y":
                # Section 2 is Rallied
                print ("Huzzah - Section 2 is rallied")
                section2_status = "Active"
    if section3_status == "Spent":
        if section3_location == leader_location:
            print ("Leader in same Hex - Section 3 Auto Rally")
            section3_status = "Active"
        else:
            rally3 = input ("Does Section 3 Rally[Y or N]?")
            if rally3.upper() == "Y":
                # Section 3 is Rallied
                print ("Huzzah - Section 3 is rallied")
                section3_status = "Active"
    print ()
    #
    # German Phase
    print ("German Phase: Turn", turns_played)
    # Fire
    if german_status == "Spent":
        print ("Good Shooting! Effective suppressing fire is making the Germans hunkering down")
    elif (section1_location == "B5") or (section2_location == "B5") or (section3_location == "B5"):
        print ("The Germans cannot fire as their position is being overrun")
    else:
        german_status = "Spent"
        brit_targets = []
        enemy = input ("Who did you shoot at [1, 2, 3, C]?")
        for infantry in enemy:
            if infantry != " ":
                print ("Add", infantry, "as a target")
                brit_targets.append(infantry)
        #print ("British Hit are:", brits_hit)
        print ("You are claiming", len(brit_targets), "hits")
        for target in brit_targets:
            d1 = dice_roll()
            if target != "C":
                print ("The Germans are shooting at Section", target, "and rolled", d1, "did that hit? [Hit (H) or Miss (M)]")
            else:
                print ("The Germans are shooting at the Commander and rolled", d1, "id that hit? [Hit (H) or Miss (M)]")
            # Accept player response
            fire_result = input (">>")
            fire_result = fire_result.upper()
            #print ("Hit=", hit,":", sep="")
            if fire_result == "H": 
                blue_hits += 1
                if target == "1":
                    section1_status = "Spent"
                elif target == "2":
                    section2_status = "Spent"
                elif target == "3":
                    section3_status = "Spent"
                elif target == "C":
                    print ("The commnder nearly copped it")
                else:
                    # Ignore spaces in string 
                    #print ("Unknown target - Hit ignored")
                    blue_hits -= 1
            elif fire_result == "M":
                print ("The German defensive fire was ineffective")
            else:
                print("You typed", fire_result, "which did not make any sense, so we are counting that as a MISS")

    #
    # German Auto Rally
    #
    german_status = "Active"
    #
    # End Turn Housekeeping
    # Keep Audit Trail
    #
    # End State Output
    #
    if (section1_location == "B5") or (section2_location == "B5") or (section3_location == "B5"):
        # Exit Game Block
        break
    
    #finished = input( "Has the hill been taken?")
    #if finished.lower() == "yes":
    # Base the end game decision being based on British Infantry location
    if (section1_location == "B5") or (section2_location == "B5") or (section3_location == "B5"):
        # Exit Game Block
        print ("The hill has been taken, as a British section has stormed the enemy position at B5")
        break
    else:
        # Increment Game Turn
        turns_played += 1
        print ()
#
# End of Game Summary
# The Game has now finished and the hill has been taken
#
print ()
print ("End of Game")
print ()
print ("Result")
if turns_played == 1:
    print ("You played", turns_played, "turn to Take That Hill")
else:
    print ("You played", turns_played, "turns to Take That Hill")
print ("Blue took ", blue_hits, "hits")
print ("Red took", red_hits, "hits")
print ("Well done!")
print ()
print ("Thank you for playing!") 
