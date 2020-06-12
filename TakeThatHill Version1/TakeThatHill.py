# "Take That Hill" Computer Assisted Instruction - Wargame
# Version 1.0
#
# Mark Flanagan 16/05/2020
# Wargame Simulation Engine
#
# Python Libraries needed
#
from random import *
#

# Global Lists:
dice_history = []
fire_history_red = []
fire_history_blue = []
rally_history_blue = []

# Range to Data Structures
hex_to_hex = [{ "section": "A4", "leader": "A", "range": 4, "rally": 5},
              { "section": "A3", "leader": "A", "range": 3, "rally": 4},
              { "section": "A2", "leader": "A", "range": 2, "rally": 3},
              { "section": "A1", "leader": "A", "range": 1, "rally": 2},
              { "section": "A",  "leader": "A", "range": 0, "rally": 0},
              { "section": "A4", "leader": "A1", "range": 3, "rally": 4},
              { "section": "A3", "leader": "A1", "range": 2, "rally": 3},
              { "section": "A2", "leader": "A1", "range": 1, "rally": 2},
              { "section": "A1", "leader": "A1", "range": 0, "rally": 0},
              { "section": "A",  "leader": "A1", "range": 1, "rally": 2},
              { "section": "A4", "leader": "A2", "range": 2, "rally": 3},
              { "section": "A3", "leader": "A2", "range": 1, "rally": 2},
              { "section": "A2", "leader": "A2", "range": 0, "rally": 0},
              { "section": "A1", "leader": "A2", "range": 1, "rally": 2},
              { "section": "A",  "leader": "A2", "range": 2, "rally": 3},
              { "section": "A4", "leader": "A3", "range": 1, "rally": 2},
              { "section": "A3", "leader": "A3", "range": 0, "rally": 0},
              { "section": "A2", "leader": "A3", "range": 1, "rally": 2},
              { "section": "A1", "leader": "A3", "range": 2, "rally": 3},
              { "section": "A",  "leader": "A3", "range": 3, "rally": 4},
              { "section": "A4", "leader": "A4", "range": 0, "rally": 0},
              { "section": "A3", "leader": "A4", "range": 1, "rally": 2},
              { "section": "A2", "leader": "A4", "range": 2, "rally": 3},
              { "section": "A1", "leader": "A4", "range": 3, "rally": 4},
              { "section": "A",  "leader": "A4", "range": 4, "rally": 5},
             ]


# Basic Dice Rolling Function
def dice_roll():
    # 1 Dice
    dice = randint(1,6)
    dice_history.append(dice)
    return dice

# Rally - Distance between Section and Leader
def score_to_rally(section_location, leader_location):
    to_rally_score_and_range = []
    # Set result values as "too high" to indicate processing error
    to_rally = 7
    the_range = 7
    # uppercase input
    section_location = section_location.upper()
    leader_location = leader_location.upper()
    if section_location == leader_location:
        # Auto Rally Scenario
        to_rally = 0
        the_range = 0
    else:
        for h in hex_to_hex:
            #print ("Can you find the range?")
            if (h["section"] == section_location) and (h["leader"] == leader_location):
                to_rally = h["rally"]
                the_range = h["range"]
                break 
    # Return values - Rally and Range
    to_rally_score_and_range.append(to_rally)
    to_rally_score_and_range.append(the_range)
    return to_rally_score_and_range

# Fire "Range" and "To Hit" to/from Hex B5
def score_to_hit(target, firer):
    to_hit_score_and_range = []
    target = target.upper()
    firer = firer.upper()
    the_range = 0
    to_hit = 0
    if (target == "A4") or (target=="B4") or (target=="C4"):
        the_range = 1
        to_hit = 2
    elif (target == "A3") or (target=="B3") or (target=="C3"):
        the_range = 2
        to_hit = 3
    elif (target == "A2") or (target=="B2") or (target=="C2"):
        the_range = 3
        to_hit = 4
    elif (target == "A1") or (target=="B1") or (target=="C1"):
        the_range = 4
        to_hit = 5
    elif (target == "A") or (target=="B") or (target=="C"):
        if firer == "BLUE":
            the_range = 5
            to_hit = 6
        elif firer == "RED":
            print("Are you in the Trees?")
            the_range = 5
            to_hit = 7
        else:
            print("Firer,", firer, "not known? [miss]")
            the_range = 7
            to_hit = 7
    else:
        print("Error: Target or Shooter hex", target, "not recognised! [miss]")
        the_range = 6
        to_hit = 7
    # Create a return value list [<to_hit_score>, <range>] 
    to_hit_score_and_range.append(to_hit)
    to_hit_score_and_range.append(the_range)
    return to_hit_score_and_range

# Print Game Board
def print_board(t):
    print("Turn", t)
    print("Row A")
    print("Row B")
    print("Row C")

# Dice History 
def print_dice_history():
    print()
    print("============================")
    print("        DICE HISTORY        ")
    print("============================")
    print()
#
    counter = 0
    for d in dice_history:
        print(d, " ", end = "")
        counter += 1
        if (counter%10)== 0:
            print()
    print()
    print("============================")
    print()
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
Red_status = "Active"
#
# Repeat Game Block while the "The hill has not been taken!"
#
# Game Board:
#
# Row 1: A, A1, A2, A3, A4
# Row 2: B, B1, B2, B3, B4, B5 
# Row 3: C, C1, C2, C3, C4
#
# Data Entry: Position of Blue Sections
#
print ("What are the Blue Starting Positions")
section1_location = input("Where is Section 1?[A, B or C]").upper()
section2_location = input("Where is Section 2?[A, B or C]").upper()
section3_location = input("Where is Section 3?[A, B or C]").upper()
leader_in_section = int(input("Which section is the leader with? [1, 2, or 3]"))
print ()
# Note: The Red Section is always in B5
Red_location = "B5"
#
# Main Game Loop
#
while True:
    print ("Blue Phase: Turn", turns_played)
    #
    # Show locations of Blue troops
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
    # Blue Sections 1..3
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
    # Game Turn Block
    # Sequence of Play for Turn
    #
    # Blue Phase
    # Blue Orders: THey will either Move or Fire
    # Move
    #
    print ()
    print ("Blue Move")
    #
    # Does the Leader Move?
    # Note: The Leader is always Active
    #
    # Apart from the first turn 
    # Ask if the Blue commander wants to hop between sections
    #
    if turns_played != 1: 
        ans0 = input ("Do you want to move the leader to another section? [1,2,3 or N]")
        # Unrecognised input is assumed to mean "N" 
        if ans0 not in ["1", "2", "3", "N"]:
            ans0 = "N"
        if ans0.upper() != "N":
            try:
                if int(ans0) in [ 1, 2, 3]:
                    # Which Section?
                    leader_in_section = int (ans0)
                    print ("The Leader has moved to Section", ans0)
                else:
                    print ("Unexpected Input", ans0, "the Leader stays where they are.")
            except ValueError as msg:
                print ("Unexpected input:", msg, "Leader stays where he is")
    #
    # Which Sections Move
    #
    if section1_status == "Active":
        #To Do: Calculate list of valid move hexes"
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
    print ("End of Blue Movement")
    print ()

    if (section1_location == "B5") or (section2_location == "B5") or (section3_location == "B5"):
        # Game Over
        break
    
    #
    # Blue Fire
    # Note to self: Make a "Blue Fire" function
    #
    print ("Blue Fire")
    if section1_status == "Active":
        fire1 = dice_roll()
        needs = score_to_hit(section1_location, "BLUE")
        to_hit = needs[0]
        at_range = needs[1]
        print("Section 1 Fires at B5 from hex", section1_location, \
              "rolling,", fire1, "requires a", to_hit, "to hit, at range", at_range)
        section1_status = "Spent"
        if fire1 >= to_hit:
            # Section 1 fires and hits the Reds in B5
            print ("Effective suppressive fire from Section 1")
            red_hits += 1
            Red_status = "Spent"
        else:
            print("Section 1 - Missed")
    if section2_status == "Active":
        fire2 = dice_roll()
        needs = score_to_hit(section2_location, "BLUE")
        to_hit = needs[0]
        at_range = needs[1]  
        print("Section 2 Fires at B5 from hex", section2_location, \
              "rolling,", fire2, "requires a", to_hit, "to hit, at range", at_range)
        section2_status = "Spent"
        if fire2 >= to_hit:
            # Section 2 fires and hits the Reds in B5
            print ("Effective suppressive fire from Section 2")
            red_hits += 1
            Red_status = "Spent"
        else:
            print("Section 2 - Missed")
    if section3_status == "Active":
        fire3 = dice_roll()
        needs = score_to_hit(section3_location, "BLUE")
        to_hit = needs[0]
        at_range = needs[1]
        print("Section 3 Fires at B5 from hex", section3_location, \
              "rolling,", fire3, "requires a", to_hit, "to hit, at range", at_range)
        section3_status = "Spent"
        if fire3 >= to_hit:
            # Section 2 fires and hits the Reds in B5
            print ("Effective suppressive fire from Section 3")
            red_hits += 1
            Red_status = "Spent"
        else:
            print("Section 3 - Missed")
    print ("End of Blue Fire Pase")
    print ()
    #
    # Blue Rally
    #
    # The Blue Leader is in which Hex?
    leader_location = ""
    if leader_in_section == 1:
        leader_location = section1_location
    elif leader_in_section == 2:
        leader_location = section2_location
    elif leader_in_section == 3:
        leader_location = section3_location
    else:
        print ("Exception: Don't know where the leader is!")
    
    print ("Blue Rally Attempt")
    if section1_status == "Spent":
        if section1_location == leader_location:
                print ("Leader in same Hex - Section 1 Auto Rally")
                section1_status = "Active"
        else: 
            rally1 = dice_roll()
            print("Leader is in hex", leader_location, "- Does Section 1 in hex,", section1_location, "Rally on a,", rally1)
            rally_data = score_to_rally(section1_location, leader_location)
            print("Rally roll needed for range", rally_data[1], "is", rally_data[0], "and we rolled a", rally1)
            #user_input = input("[Y or N]?")
            #if user_input.upper() == "Y":
            if rally1 >= rally_data[0]:
                # Section 1 is Rallied
                print ("Section 1 is rallied")
                section1_status = "Active"
    if section2_status == "Spent":
        if section2_location == leader_location:
            print ("Leader in same Hex - Section 2 Auto Rally")
            section2_status = "Active"
        else:
            rally2 = dice_roll()
            print("Leader is in hex", leader_location, "- Does Section 2 in hex,", section2_location, "Rally on a,", rally2)
            user_input = input("[Y or N]?")
            if user_input.upper() == "Y":
                # Section 2 is Rallied
                print ("Section 2 is rallied")
                section2_status = "Active"
    if section3_status == "Spent":
        if section3_location == leader_location:
            print ("Leader in same Hex - Section 3 Auto Rally")
            section3_status = "Active"
        else:
            rally3 = dice_roll()
            print("Leader is in hex", leader_location, "- Does Section 3 in hex,", section3_location, "Rally on a,", rally3)
            user_input = input("[Y or N]?")
            if user_input.upper() == "Y":
                # Section 3 is Rallied
                print ("Section 3 is rallied")
                section3_status = "Active"
    print ()
    #
    # Red Phase
    #
    print ("Red Phase: Turn", turns_played)
    # Fire
    if Red_status == "Spent":
        print ("Good Shooting by Blue! Effective suppressing fire is making the Reds hunkering down")
    elif (section1_location == "B5") or (section2_location == "B5") or (section3_location == "B5"):
        print ("The Reds cannot fire as their position is being overrun")
    else:
        Red_status = "Spent"
        brit_targets = []
        enemy = []
        enemy = input ("Who did you shoot at [1, 2, 3, C]?")
        for infantry in enemy:
            if infantry != " ":
                # print ("Add", infantry, "as a target")
                brit_targets.append(infantry)
        #print ("Blue Hit are:", brits_hit)
        print ("You are claiming", len(brit_targets), "targets")
        for target in brit_targets:
            print ("Target =", target)
            d1 = dice_roll()
            if target != "C":
                if target == "1":
                    print("** section one location**", section1_location)
                    needs = score_to_hit(section1_location, "RED")
                    to_hit = needs[0]
                    at_range = needs[1]
                    if at_range <= 6:
                        print ("The Reds are shooting at Section", target, "in hex", \
                               section1_location, "and rolled a", d1, "requiring a", to_hit, "at range", at_range)
                    else:
                        print ("Target at", section1_location, "is in the treeline and cannot be hit")
                elif target == "2":
                    needs = score_to_hit(section2_location, "RED")
                    to_hit = needs[0]
                    at_range = needs[1]
                    if at_range <= 6:
                        print ("The Reds are shooting at Section", target, "in hex", \
                               section2_location, "and rolled a", d1, "requiring a", to_hit, "at_range", at_range)
                    else:
                        print ("Target at", section2_location, "is in the treeline and cannot be hit")
                else:
                    needs = score_to_hit(section3_location, "RED")
                    to_hit = needs[0]
                    at_range = needs[1]
                    if at_range <= 6:
                        print ("The Reds are shooting at Section", target, "in hex", \
                               section3_location, "and rolled a", d1, "requiring a", to_hit, "at range", at_range)
                    else:
                        print ("Target at", section2_location, "is in the treeline and cannot be hit")
            else:
                needs = score_to_hit(leader_location, "RED")
                to_hit = needs[0]
                at_range = needs[1]
                if at_range <= 6:
                    print ("The Reds are shooting at the Commander in hex,", leader_location, \
                           "and rolled", d1, "requiring a", to_hit, "at range", at_range)
                else:
                    print ("Target at", leader_location, "is in the treeline and cannot be hit")
            if d1 >= to_hit:
                blue_hits += 1
                if target == "1":
                    section1_status = "Spent"
                elif target == "2":
                    section2_status = "Spent"
                elif target == "3":
                    section3_status = "Spent"
                elif target == "C":
                    print ("The commnder is under fire")
                else:
                    # Ignore spaces in string 
                    #print ("Unknown target - Hit ignored")
                    blue_hits -= 1
            elif d1 < to_hit:
                print ("The Red defensive fire was ineffective")
            else:
                print("You typed", d1, "which did not make any sense, so we are counting that as a MISS")
    #
    # Red Auto Rally
    #
    Red_status = "Active"
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
    # Base the end game decision being based on Blue Infantry location
    if (section1_location == "B5") or \
        (section2_location == "B5") or \
        (section3_location == "B5"):
        # Exit Game Block
        print ("The hill has been taken, as a Blue section has stormed the enemy position at B5")
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
#
# End of Game Analysis
#
# Dice Rolls were ...
print_dice_history()
#
# Write Game Log to File
print("Game Data saved ..")
print("Thank you for playing!") 
