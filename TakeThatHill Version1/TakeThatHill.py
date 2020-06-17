# "Take That Hill" Computer Assisted Instruction - Wargame
# Version 1.0
#
# Mark Flanagan 16/05/2020
# Wargame Simulation Engine
#
# Python Libraries needed
#
from random import *

# Taking matplotlib out to see if it gets round Ian's runtime issue
#import matplotlib.pyplot as plt
#

# Global Lists:
dice_history = []
fire_history_red = []
fire_history_blue = []
rally_history_blue = []

# Rally - Range Section to Leader - Data Structures
hex_to_hex = [
            #
            # A Hex Row
            # 
              { "section": "A4", "leader": "A", "range": 4, "rally": 5},
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
            #
              { "section": "A4", "leader": "B", "range": 5, "rally": 6},
              { "section": "A3", "leader": "B", "range": 4, "rally": 5},
              { "section": "A2", "leader": "B", "range": 3, "rally": 4},
              { "section": "A1", "leader": "B", "range": 2, "rally": 3},
              { "section": "A",  "leader": "B", "range": 1, "rally": 2},
              { "section": "A4", "leader": "B1", "range": 4, "rally": 5},
              { "section": "A3", "leader": "B1", "range": 3, "rally": 4},
              { "section": "A2", "leader": "B1", "range": 2, "rally": 3},
              { "section": "A1", "leader": "B1", "range": 1, "rally": 2},
              { "section": "A",  "leader": "B1", "range": 1, "rally": 2},
              { "section": "A4", "leader": "B2", "range": 3, "rally": 4},
              { "section": "A3", "leader": "B2", "range": 2, "rally": 3},
              { "section": "A2", "leader": "B2", "range": 1, "rally": 2},
              { "section": "A1", "leader": "B2", "range": 1, "rally": 2},
              { "section": "A",  "leader": "B2", "range": 2, "rally": 3},
              { "section": "A4", "leader": "B3", "range": 2, "rally": 3},
              { "section": "A3", "leader": "B3", "range": 1, "rally": 2},
              { "section": "A2", "leader": "B3", "range": 1, "rally": 2},
              { "section": "A1", "leader": "B3", "range": 2, "rally": 3},
              { "section": "A",  "leader": "B3", "range": 3, "rally": 4},
              { "section": "A4", "leader": "B4", "range": 1, "rally": 2},
              { "section": "A3", "leader": "B4", "range": 1, "rally": 2},
              { "section": "A2", "leader": "B4", "range": 2, "rally": 3},
              { "section": "A1", "leader": "B4", "range": 3, "rally": 4},
              { "section": "A",  "leader": "B4", "range": 4, "rally": 5},
              { "section": "A4", "leader": "B5", "range": 1, "rally": 2},
              { "section": "A3", "leader": "B5", "range": 2, "rally": 3},
              { "section": "A2", "leader": "B5", "range": 3, "rally": 4},
              { "section": "A1", "leader": "B5", "range": 4, "rally": 5},
              { "section": "A",  "leader": "B5", "range": 5, "rally": 6},
            #
              { "section": "A4", "leader": "C", "range": 5, "rally": 6},
              { "section": "A3", "leader": "C", "range": 4, "rally": 5},
              { "section": "A2", "leader": "C", "range": 3, "rally": 4},
              { "section": "A1", "leader": "C", "range": 2, "rally": 3},
              { "section": "A",  "leader": "C", "range": 2, "rally": 3},
              { "section": "A4", "leader": "C1", "range": 4, "rally": 5},
              { "section": "A3", "leader": "C1", "range": 3, "rally": 4},
              { "section": "A2", "leader": "C1", "range": 2, "rally": 3},
              { "section": "A1", "leader": "C1", "range": 2, "rally": 3},
              { "section": "A",  "leader": "C1", "range": 2, "rally": 3},
              { "section": "A4", "leader": "C2", "range": 3, "rally": 4},
              { "section": "A3", "leader": "C2", "range": 2, "rally": 3},
              { "section": "A2", "leader": "C2", "range": 2, "rally": 3},
              { "section": "A1", "leader": "C2", "range": 2, "rally": 3},
              { "section": "A",  "leader": "C2", "range": 3, "rally": 4},
              { "section": "A4", "leader": "C3", "range": 2, "rally": 3},
              { "section": "A3", "leader": "C3", "range": 2, "rally": 3},
              { "section": "A2", "leader": "C3", "range": 2, "rally": 3},
              { "section": "A1", "leader": "C3", "range": 3, "rally": 4},
              { "section": "A",  "leader": "C3", "range": 4, "rally": 5},
              { "section": "A4", "leader": "C4", "range": 2, "rally": 3},
              { "section": "A3", "leader": "C4", "range": 2, "rally": 3},
              { "section": "A2", "leader": "C4", "range": 3, "rally": 4},
              { "section": "A1", "leader": "C4", "range": 4, "rally": 5},
              { "section": "A",  "leader": "C4", "range": 5, "rally": 6},
            #
            # B Hex Row
            #
              { "section": "B5", "leader": "A", "range": 5, "rally": 6},
              { "section": "B4", "leader": "A", "range": 4, "rally": 5},
              { "section": "B3", "leader": "A", "range": 3, "rally": 4},
              { "section": "B2", "leader": "A", "range": 2, "rally": 3},
              { "section": "B1", "leader": "A", "range": 1, "rally": 2},
              { "section": "B",  "leader": "A", "range": 1, "rally": 2},
              { "section": "B5", "leader": "A1", "range": 4, "rally": 5},        
              { "section": "B4", "leader": "A1", "range": 3, "rally": 4},
              { "section": "B3", "leader": "A1", "range": 2, "rally": 3},
              { "section": "B2", "leader": "A1", "range": 1, "rally": 2},
              { "section": "B1", "leader": "A1", "range": 1, "rally": 2},
              { "section": "B",  "leader": "A1", "range": 2, "rally": 3},
              { "section": "B5", "leader": "A2", "range": 5, "rally": 6},
              { "section": "B4", "leader": "A2", "range": 2, "rally": 3},
              { "section": "B3", "leader": "A2", "range": 1, "rally": 2},
              { "section": "B2", "leader": "A2", "range": 1, "rally": 2},
              { "section": "B1", "leader": "A2", "range": 2, "rally": 3},
              { "section": "B",  "leader": "A2", "range": 3, "rally": 4},
              { "section": "B5", "leader": "A3", "range": 2, "rally": 3},
              { "section": "B4", "leader": "A3", "range": 1, "rally": 2},
              { "section": "B3", "leader": "A3", "range": 1, "rally": 2},
              { "section": "B2", "leader": "A3", "range": 2, "rally": 3},
              { "section": "B1", "leader": "A3", "range": 3, "rally": 4},
              { "section": "B",  "leader": "A3", "range": 4, "rally": 5},
              { "section": "B5", "leader": "A4", "range": 1, "rally": 2},
              { "section": "B4", "leader": "A4", "range": 1, "rally": 2},
              { "section": "B3", "leader": "A4", "range": 2, "rally": 3},
              { "section": "B2", "leader": "A4", "range": 3, "rally": 4},
              { "section": "B1", "leader": "A4", "range": 4, "rally": 5},
              { "section": "B",  "leader": "A4", "range": 5, "rally": 6},
            #
              { "section": "B5", "leader": "B", "range": 5, "rally": 6},
              { "section": "B4", "leader": "B", "range": 4, "rally": 5},
              { "section": "B3", "leader": "B", "range": 3, "rally": 4},
              { "section": "B2", "leader": "B", "range": 2, "rally": 3},
              { "section": "B1", "leader": "B", "range": 1, "rally": 2},
              { "section": "B",  "leader": "B", "range": 0, "rally": 0},
              { "section": "B5", "leader": "B1", "range": 4, "rally": 5},  
              { "section": "B4", "leader": "B1", "range": 3, "rally": 4},
              { "section": "B3", "leader": "B1", "range": 2, "rally": 3},
              { "section": "B2", "leader": "B1", "range": 1, "rally": 2},
              { "section": "B1", "leader": "B1", "range": 0, "rally": 0},
              { "section": "B",  "leader": "B1", "range": 1, "rally": 2},
              { "section": "B5", "leader": "B2", "range": 3, "rally": 4},
              { "section": "B4", "leader": "B2", "range": 2, "rally": 3},
              { "section": "B3", "leader": "B2", "range": 1, "rally": 2},
              { "section": "B2", "leader": "B2", "range": 0, "rally": 0},
              { "section": "B1", "leader": "B2", "range": 1, "rally": 2},
              { "section": "B",  "leader": "B2", "range": 2, "rally": 3},
              { "section": "B5", "leader": "B3", "range": 2, "rally": 3},
              { "section": "B4", "leader": "B3", "range": 1, "rally": 2},
              { "section": "B3", "leader": "B3", "range": 0, "rally": 0},
              { "section": "B2", "leader": "B3", "range": 1, "rally": 2},
              { "section": "B1", "leader": "B3", "range": 2, "rally": 3},
              { "section": "B",  "leader": "B3", "range": 3, "rally": 4},
              { "section": "B5", "leader": "B4", "range": 1, "rally": 2},
              { "section": "B4", "leader": "B4", "range": 0, "rally": 0},
              { "section": "B3", "leader": "B4", "range": 1, "rally": 2},
              { "section": "B2", "leader": "B4", "range": 2, "rally": 3},
              { "section": "B1", "leader": "B4", "range": 3, "rally": 4},
              { "section": "B",  "leader": "B4", "range": 4, "rally": 5},
              { "section": "B5", "leader": "B5", "range": 0, "rally": 0},
              { "section": "B4", "leader": "B5", "range": 1, "rally": 2},
              { "section": "B3", "leader": "B5", "range": 2, "rally": 3},
              { "section": "B2", "leader": "B5", "range": 3, "rally": 4},
              { "section": "B1", "leader": "B5", "range": 4, "rally": 5},
              { "section": "B",  "leader": "B5", "range": 5, "rally": 6},
            #
              { "section": "B5", "leader": "C", "range": 5, "rally": 6},   
              { "section": "B4", "leader": "C", "range": 4, "rally": 5},
              { "section": "B3", "leader": "C", "range": 3, "rally": 4},
              { "section": "B2", "leader": "C", "range": 2, "rally": 3},
              { "section": "B1", "leader": "C", "range": 1, "rally": 2},
              { "section": "B",  "leader": "C", "range": 1, "rally": 2},
              { "section": "B5", "leader": "C!", "range": 4, "rally": 5},
              { "section": "B4", "leader": "C1", "range": 3, "rally": 4},
              { "section": "B3", "leader": "C1", "range": 2, "rally": 3},
              { "section": "B2", "leader": "C1", "range": 1, "rally": 2},
              { "section": "B1", "leader": "C1", "range": 1, "rally": 2},
              { "section": "B",  "leader": "C1", "range": 2, "rally": 3},
              { "section": "B5", "leader": "C2", "range": 3, "rally": 4},
              { "section": "B4", "leader": "C2", "range": 2, "rally": 3},
              { "section": "B3", "leader": "C2", "range": 1, "rally": 2},
              { "section": "B2", "leader": "C2", "range": 1, "rally": 2},
              { "section": "B1", "leader": "C2", "range": 2, "rally": 3},
              { "section": "B",  "leader": "C2", "range": 3, "rally": 4},
              { "section": "B5", "leader": "C3", "range": 2, "rally": 3},
              { "section": "B4", "leader": "C3", "range": 1, "rally": 2},
              { "section": "B3", "leader": "C3", "range": 1, "rally": 2},
              { "section": "B2", "leader": "C3", "range": 2, "rally": 3},
              { "section": "B1", "leader": "C3", "range": 3, "rally": 4},
              { "section": "B",  "leader": "C3", "range": 4, "rally": 5},
              { "section": "B5", "leader": "C4", "range": 1, "rally": 2},
              { "section": "B4", "leader": "C4", "range": 1, "rally": 2},
              { "section": "B3", "leader": "C4", "range": 2, "rally": 3},
              { "section": "B2", "leader": "C4", "range": 3, "rally": 4},
              { "section": "B1", "leader": "C4", "range": 4, "rally": 5},
              { "section": "B",  "leader": "C4", "range": 5, "rally": 6},
            #
            # C Hex Row
            #
              { "section": "C4", "leader": "A", "range": 5, "rally": 6},
              { "section": "C3", "leader": "A", "range": 4, "rally": 5},
              { "section": "C2", "leader": "A", "range": 3, "rally": 4},
              { "section": "C1", "leader": "A", "range": 2, "rally": 3},
              { "section": "C",  "leader": "A", "range": 2, "rally": 3},
              { "section": "C4", "leader": "A1", "range": 4, "rally": 5},
              { "section": "C3", "leader": "A1", "range": 3, "rally": 4},
              { "section": "C2", "leader": "A1", "range": 2, "rally": 3},
              { "section": "C1", "leader": "A1", "range": 2, "rally": 3},
              { "section": "C",  "leader": "A1", "range": 2, "rally": 3},
              { "section": "C4", "leader": "A2", "range": 3, "rally": 4},
              { "section": "C3", "leader": "A2", "range": 2, "rally": 3},
              { "section": "C2", "leader": "A2", "range": 2, "rally": 3},
              { "section": "C1", "leader": "A2", "range": 2, "rally": 3},
              { "section": "C",  "leader": "A2", "range": 3, "rally": 4},
              { "section": "C4", "leader": "A3", "range": 2, "rally": 3},
              { "section": "C3", "leader": "A3", "range": 2, "rally": 3},
              { "section": "C2", "leader": "A3", "range": 2, "rally": 3},
              { "section": "C1", "leader": "A3", "range": 3, "rally": 4},
              { "section": "C",  "leader": "A3", "range": 4, "rally": 5},
              { "section": "C4", "leader": "A4", "range": 2, "rally": 3},
              { "section": "C3", "leader": "A4", "range": 2, "rally": 3},
              { "section": "C2", "leader": "A4", "range": 3, "rally": 4},
              { "section": "C1", "leader": "A4", "range": 4, "rally": 5},
              { "section": "C",  "leader": "A4", "range": 5, "rally": 6},
            #
              { "section": "C4", "leader": "B", "range": 5, "rally": 6},
              { "section": "C3", "leader": "B", "range": 4, "rally": 5},
              { "section": "C2", "leader": "B", "range": 3, "rally": 4},
              { "section": "C1", "leader": "B", "range": 2, "rally": 3},
              { "section": "C",  "leader": "B", "range": 1, "rally": 2},
              { "section": "C4", "leader": "B1", "range": 4, "rally": 5},
              { "section": "C3", "leader": "B1", "range": 3, "rally": 4},
              { "section": "C2", "leader": "B1", "range": 2, "rally": 3},
              { "section": "C1", "leader": "B1", "range": 1, "rally": 2},
              { "section": "C",  "leader": "B1", "range": 1, "rally": 2},
              { "section": "C4", "leader": "B2", "range": 3, "rally": 4},
              { "section": "C3", "leader": "B2", "range": 2, "rally": 3},
              { "section": "C2", "leader": "B2", "range": 1, "rally": 2},
              { "section": "C1", "leader": "B2", "range": 1, "rally": 2},
              { "section": "C",  "leader": "B2", "range": 2, "rally": 3},
              { "section": "C4", "leader": "B3", "range": 2, "rally": 3},
              { "section": "C3", "leader": "B3", "range": 1, "rally": 2},
              { "section": "C2", "leader": "B3", "range": 1, "rally": 2},
              { "section": "C1", "leader": "B3", "range": 2, "rally": 3},
              { "section": "C",  "leader": "B3", "range": 3, "rally": 4},
              { "section": "C4", "leader": "B4", "range": 1, "rally": 2},
              { "section": "C3", "leader": "B4", "range": 1, "rally": 2},
              { "section": "C2", "leader": "B4", "range": 2, "rally": 3},
              { "section": "C1", "leader": "B4", "range": 3, "rally": 4},
              { "section": "C",  "leader": "B4", "range": 4, "rally": 5},
              { "section": "C4", "leader": "B5", "range": 1, "rally": 2},
              { "section": "C3", "leader": "B5", "range": 2, "rally": 3},
              { "section": "C2", "leader": "B5", "range": 3, "rally": 4},
              { "section": "C1", "leader": "B5", "range": 4, "rally": 5},
              { "section": "C",  "leader": "B5", "range": 5, "rally": 6},
            #
              { "section": "C4", "leader": "C", "range": 4, "rally": 5},
              { "section": "C3", "leader": "C", "range": 3, "rally": 4},
              { "section": "C2", "leader": "C", "range": 2, "rally": 3},
              { "section": "C1", "leader": "C", "range": 1, "rally": 2},
              { "section": "C",  "leader": "C", "range": 0, "rally": 0},
              { "section": "C4", "leader": "C1", "range": 3, "rally": 4},
              { "section": "C3", "leader": "C1", "range": 2, "rally": 3},
              { "section": "C2", "leader": "C1", "range": 1, "rally": 2},
              { "section": "C1", "leader": "C1", "range": 0, "rally": 0},
              { "section": "C",  "leader": "C1", "range": 1, "rally": 2},
              { "section": "C4", "leader": "C2", "range": 2, "rally": 3},
              { "section": "C3", "leader": "C2", "range": 1, "rally": 2},
              { "section": "C2", "leader": "C2", "range": 0, "rally": 0},
              { "section": "C1", "leader": "C2", "range": 1, "rally": 2},
              { "section": "C",  "leader": "C2", "range": 2, "rally": 3},
              { "section": "C4", "leader": "C3", "range": 1, "rally": 2},
              { "section": "C3", "leader": "C3", "range": 0, "rally": 0},
              { "section": "C2", "leader": "C3", "range": 1, "rally": 2},
              { "section": "C1", "leader": "C3", "range": 2, "rally": 3},
              { "section": "C",  "leader": "C3", "range": 3, "rally": 4},
              { "section": "C4", "leader": "C4", "range": 0, "rally": 0},
              { "section": "C3", "leader": "C4", "range": 1, "rally": 2},
              { "section": "C2", "leader": "C4", "range": 2, "rally": 3},
              { "section": "C1", "leader": "C4", "range": 3, "rally": 4},
              { "section": "C",  "leader": "C4", "range": 4, "rally": 5}            
             ]


# Basic Dice Rolling Function
def dice_roll():
    # 1 Dice
    dice = randint(1,6)
    dice_history.append(dice)
    return dice

# Section Legal Move Generator
def section_legal_moves(section_hex):
    legal_moves_list = []
    for h in hex_to_hex:
        if (section_hex == h["section"]) and (h["range"] == 1):
            legal_moves_list.append(h["leader"])
    return legal_moves_list

# Leader Legal Move Generator
def leader_legal_moves(leader_location, troops):
    legal_moves_list = []
    possible_hexes = []
    for h in hex_to_hex:
        if (leader_location == h["section"]) and (h["range"] == 1):
            possible_hexes.append(h["leader"])
    #print("Possible Hexes =", possible_hexes )
    for p in possible_hexes:
        if p in troops:
            legal_moves_list.append(p)
    #print("Final list of legal moves = ", legal_moves_list)
    return legal_moves_list

# Distance d between a and b
def a_to_b(a, b):
    # Set result values as "too high" to indicate processing error
    d = 7
    # uppercase input
    a = a.upper()
    b = b.upper()
    if a == b:
        # Same Hex
        d = 0
    else:
        for h in hex_to_hex:
            #print ("Can you find the range?")
            if (h["section"] == a) and (h["leader"] == b):
                d = h["range"]
                break 
    return d

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

# What are the valid Blue targets for Red?
def get_blue_targets(section1, section2, section3, leader_section):
    #
    # Assign leader location to section
    #
    if leader_section == 1:
        leader = section1
        #print("Assign Leader to Squad 1 in location", section1)
    elif leader_section == 2:
        leader = section2
        #print("Assign Leader to Squad 2 in location", section2)
    elif leader_section == 3:
        leader = section3
        #print("Assign Leader to Squad 3 in location", section3)
    else:
        print("Error: Unknown section associated with leader", )
    target_list = []
    #
    # Is there a single hex Mega Cluster?
    #
    if (section1 == section2) and (section2 == section3):
        # Everyone in the same hex so return a Mega-Cluster of targets
        target_list = [ ["1", "2", "3", "C"] ]
        return target_list
    # Otherwise figure out the targets
    # First set singleton flags to true
    s1 = True
    s2 = True
    s3 = True
    #
    # There are three sections and a Commander to consider
    # Is any section adjacent to another signify a cluster of targets?
    #
    # Calculate distances between sections
    # Units in base line hexes [A, B, C] are immune from Red defensive fire
    #
    # Distance between sections 1 and 2
    s1_to_s2 = a_to_b(section1, section2)
    #print ("The range between section 1 and section 2 is,", s1_to_s2)
    # Distance between sections 1 and 3
    s1_to_s3 = a_to_b(section1, section3)
    #print ("The range between section 1 and section 3 is,", s1_to_s3)

    s2_to_s3 = a_to_b(section2, section3)
    #print ("The range between section 2 and section 3 is,", s2_to_s3)
    #
    # Is there a multi-hex Mega-Cluster of targets
    # Situation 1 where section 1 and section 2 are stacked together
    # and section 3 is adjacent
    if (section1 == section2) and (s2_to_s3 == 1):
        target_list = [ ["1", "2", "3", "C"] ]
        return target_list
    # Situation 2 where section 2 and section 3 are stacked together
    # and section 1 is adjacent
    if (section2 == section3) and (s1_to_s2 == 1):
        target_list = [ ["1", "2", "3", "C"] ]
        return target_list
    
    # What about combinations with section 1?
    # If section 1 to section 2 = range <= 1 there is a cluster
    if (s1_to_s2 <= 1) and ((section1 not in [ "A", "B", "C" ]) or (section2 not in [ "A", "B", "C" ])):
        s1 = False
        s2 = False
        if (leader == section1) or (leader == section2):
            target_list.append(["1", "2", "C"])
        else:
            target_list.append(["1", "2"])
    # if section 1 to section 3 = range <= 1 there is a cluster
    if (s1_to_s3 <= 1) and ((section1 not in [ "A", "B", "C" ]) or (section3 not in [ "A", "B", "C" ])):
        s1 = False
        s3 = False
        if (leader == section1) or (leader == section3):
            target_list.append(["1", "3", "C"])
        else:
            target_list.append(["1", "3"])

    # Has section 1 not appeared in the target list part of a cluster        
    if (s1 == True) and (section1 not in [ "A", "B", "C" ]):
        # Add section 1 as a singleton target
        if leader == section1:
            target_list.append(["1", "C"])
        else:
            target_list.append(["1"])

    # If section 2 to section 3 = range <= 1 there is a cluster
    if (s2_to_s3 <=1 ) and ((section2 not in [ "A", "B", "C"]) or (section3 not in [ "A", "B", "C"])):
        s2 = False
        s3 = False
        if (leader == section2) or (leader == section3):
            target_list.append(["2", "3", "C"])
        else:
            target_list.append(["2", "3"])       

    # Has section 2 not appeared in the target list part of a cluster        
    if (s2 == True) and (section2 not in [ "A", "B", "C" ]):
        print("Section 2 is a singleton")
        # Add section 2 as a singleton target
        print("Leader with section 2,", leader)
        if leader == section2:
            target_list.append(["2", "C"])
        else:
            target_list.append(["2"])

    # Has section 3 not appeared in the target list part of a cluster        
    if (s3 == True) and (section3 not in [ "A", "B", "C" ]):
        # Add section 1 as a singleton target
        if leader == section3:
            target_list.append(["3", "C"])
        else:
            target_list.append(["3"])
    
    return target_list
#
#==================================================
# Functions to Display Information back to the User
#==================================================
#
# Print Game Board
#
def print_game_board(turn, s1, s2, s3, leader):
    print()
    commander = ""
    # Hexes
    A = "....A"
    B = "....B"
    C = "....C"
    A1 = A2 = A3 = A4 = B1 = B2 = B3 = B4 = C1 = C2 = C3 = C4 = "...."
    B5 = ".XX."
    # Where is the leader/commander?
    if leader == 1:
        commander = s1
    elif leader == 2:
        commander = s2
    elif leader == 3:
        commander = s3
    else:
        print("Cannot see where the commander is!", leader)
    # Work out where the troops are:
    troops = [ s1, s2, s3, commander]
    hexes = [ {"hex":"A", "graphic":A}, \
              {"hex":"A1", "graphic":A1}, {"hex":"A2", "graphic":A2}, {"hex":"A3", "graphic":A3},{"hex":"A4", "graphic":A4}, \
              {"hex":"B", "graphic":B}, \
              {"hex":"B1", "graphic":B1}, {"hex":"B2", "graphic":B2}, {"hex":"B3", "graphic":B3}, {"hex":"B4", "graphic":B4},{"hex":"B5", "graphic":B5},\
              {"hex":"C", "graphic":C}, \
              {"hex":"C1", "graphic":C1}, {"hex":"C2", "graphic":C2}, {"hex":"C3", "graphic":C3},{"hex":"C4", "graphic":C4}, \
              ]
    counter = 0
    for t in troops:
        #print("t =", t)
        counter += 1
        #print("Counter =", counter)
        for h in hexes:
            # print("h[hex] =", h["hex"])
            if t == h["hex"]:
                if counter == 1:
                    h["graphic"] = 's'+ h["graphic"][1:5]
                elif counter == 2:
                    h["graphic"] = h["graphic"][0:1] + 's' + h["graphic"][2:5]
                elif counter == 3:
                    h["graphic"] = h["graphic"][0:2] + 's' + h["graphic"][3:5]
                else:
                    h["graphic"] = h["graphic"][0:3] + 'c' + h["graphic"][4:5]
                #print("h[graphic]=", h["graphic"])
    # Rows
    #rowA = "Row A:     " + A + " " + A1 + " " + A2 + " " + A3 + " " + A4
    rowA = "Row A:     " + hexes[0]["graphic"] + " " + hexes[1]["graphic"] + " " + hexes[2]["graphic"] + " " + hexes[3]["graphic"] + " " + hexes[4]["graphic"]
    rowB = "Row B:    " +  hexes[5]["graphic"] + " " + hexes[6]["graphic"] + " " + hexes[7]["graphic"] + " " + hexes[8]["graphic"] + " " + hexes[9]["graphic"] + " " + hexes[10]["graphic"]
    rowC = "Row C:     " + hexes[11]["graphic"] + " " + hexes[12]["graphic"] + " " + hexes[13]["graphic"] + " " + hexes[14]["graphic"] + " " + hexes[15]["graphic"]
    # Print Board 
    print("Turn", turn)
    print()
    print(rowA)
    print(rowB)
    print(rowC)
    print()
#
# Dice History 
#
def print_dice_history():
    print()
    print("============================")
    print("        DICE HISTORY        ")
    print("============================")
    print()
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
# Information on the Blue forces staus
#
def blue_sections_display(leader_in_section, \
                          section1_status, section2_status, section3_status, \
                          section1_location, section2_location, section3_location):
        #
        # Blue Sections 1..3
        # Where are they?
        #
        # Section 1
        print()
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
#==============
# Main Program
#==============
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
# Row 1:  A, A1, A2, A3, A4
# Row 2: B, B1, B2, B3, B4, B5 
# Row 3:  C, C1, C2, C3, C4
#
# Data Entry: Position of Blue Sections
#
# Data initialisation
#
section1_location = ""
section2_location = ""
section3_location = ""
leader_in_section = 0
#
# Get values from user: Starting Locations
#
print ("What are the Blue Starting Positions")
while section1_location not in ["A", "B", "C"]:
    section1_location = input("Where is Section 1?[A, B or C]").upper()
while section2_location not in ["A", "B", "C"]:
    section2_location = input("Where is Section 2?[A, B or C]").upper()
while section3_location not in ["A", "B", "C"]:
    section3_location = input("Where is Section 3?[A, B or C]").upper()
while leader_in_section not in [1, 2, 3]:
    leader_in_section = int(input("Which section is the leader with? [1, 2, or 3]"))
print ()
#
# Note: The Red Section is always in B5
#
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
    # Display Game Board
    #
    print_game_board(turns_played, section1_location, section2_location, section3_location, leader_in_section)    
    blue_sections_display(leader_in_section, section1_status, section2_status, section3_status, \
                          section1_location, section2_location, section3_location)
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
        leader_legal_moves_list = [ 'N' ]
        troop_locations = [ section1_location, section2_location, section3_location]
        leader_legal_moves_list.extend(leader_legal_moves(leader_location, troop_locations))
        if len(leader_legal_moves_list) > 1:
            print("Leader Legal Moves =", leader_legal_moves_list)
            ans0 = ""
            while ans0.upper() not in leader_legal_moves_list:
                ans0 = input ("Do you want to move the leader to another section? [Hex or N]")
                ans0 = ans0.upper()
            # Unrecognised input is assumed to mean "N" 
            if ans0.upper() != "N":
                try:
                    leader_location = ans0.upper()
                    for t in troop_locations:
                        # Which Section?
                        if ans0.upper() == section1_location:
                            leader_in_section = 1
                            #print ("The Leader has moved to Section", leader_in_section)
                        elif ans0.upper() == section2_location:
                            leader_in_section = 2
                            #print ("The Leader has moved to Section", leader_in_section)
                        else:
                            leader_in_section = 3
                            #print ("The Leader has moved to Section", leader_in_section)
                    else:
                        print ("Unexpected Input", ans0, "the Leader stays where they are.")
                except ValueError as msg:
                    print ("Unexpected input:", msg, "Leader stays where he is")
    #
    # Section - Legal Move Lists
    # Default: N omplies "No Move" meaning "Fire" instead
    #
    section1_legal_moves = [ 'N' ]
    section2_legal_moves = [ 'N' ]
    section3_legal_moves = [ 'N' ]
    #
    # Which Sections Move?
    #
    if section1_status == "Active":
        # Calculate list of valid move hexes"
        section1_legal_moves.extend(section_legal_moves(section1_location))
        print("Section 1 in",section1_location, "has Legal Moves of:", section1_legal_moves)
        ans1 = input ("Do you want to move Section 1 [Hex or N]?")
        ans1.upper()
        while ans1.upper() not in section1_legal_moves:
            print(ans1, "is not a valid legal hex, please retry")
            ans1 = input ("Do you want to move Section 1 [Hex or N]?")
            ans1 = ans1.upper()
        if ans1 != "N":
            # Section used its action to move
            section1_location = ans1
            section1_status = "Spent"
    if section2_status == "Active":
        # Calculate list of valid move hexes"
        section2_legal_moves.extend(section_legal_moves(section2_location))
        print("Section 2 in", section2_location, "has Legal Moves of:", section2_legal_moves)
        ans2 = input ("Do you want to move Section 2 [Hex or N]?")
        ans2 = ans2.upper()
        while ans2.upper() not in section2_legal_moves:
            print(ans2, "is not a valid legal hex, please retry")
            ans2 = input ("Do you want to move Section 2 [Hex or N]?")
            ans2 = ans2.upper()
        if ans2 != "N":
            # Section used its action to move
            section2_location = ans2
            section2_status = "Spent"
    if section3_status == "Active":
        # Calculate list of valid move hexes"
        section3_legal_moves.extend(section_legal_moves(section3_location))
        print("Section 3 in", section3_location, "has Legal Moves: of", section3_legal_moves)
        ans3 = input ("Do you want to move Section 3 [Hex or N]?")
        ans3 = ans3.upper()
        while ans3.upper() not in section3_legal_moves:
            print(ans3, "is not a valid legal hex, please retry")
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
            else:
                print ("Section 1 has not rallied")
    if section2_status == "Spent":
        if section2_location == leader_location:
            print ("Leader in same Hex - Section 2 Auto Rally")
            section2_status = "Active"
        else:
            rally2 = dice_roll()
            print("Leader is in hex", leader_location, "- Does Section 2 in hex,", section2_location, "Rally on a,", rally2)
            rally_data = score_to_rally(section2_location, leader_location)
            print("Rally roll needed for range", rally_data[1], "is", rally_data[0], "and we rolled a", rally2)         
            #user_input = input("[Y or N]?")
            #if user_input.upper() == "Y":
            if rally2 >= rally_data[0]:
                # Section 2 is Rallied
                print ("Section 2 is rallied")
                section2_status = "Active"
            else:
                print ("Section 2 has not rallied")
    if section3_status == "Spent":
        if section3_location == leader_location:
            print ("Leader in same Hex - Section 3 Auto Rally")
            section3_status = "Active"
        else:
            rally3 = dice_roll()
            print("Leader is in hex", leader_location, "- Does Section 3 in hex,", section3_location, "Rally on a,", rally3)
            rally_data = score_to_rally(section3_location, leader_location)
            print("Rally roll needed for range", rally_data[1], "is", rally_data[0], "and we rolled a", rally3)    
            #user_input = input("[Y or N]?")           
            #if user_input.upper() == "Y":
            if rally3 >= rally_data[0]:
                # Section 3 is Rallied
                print ("Section 3 is rallied")
                section3_status = "Active"
            else:
                print ("Section 3 has not rallied")
    print ()
    #
    # Red Phase
    #
    print ("Red Phase: Turn", turns_played)
    #
    # Show the state of play to the Red Player
    #
    print_game_board(turns_played, section1_location, section2_location, section3_location, leader_in_section)
    blue_sections_display(leader_in_section, section1_status, section2_status, section3_status, \
                          section1_location, section2_location, section3_location)    
    #
    # Red Fire Combat
    #
    if Red_status == "Spent":
        print ("Good Shooting by Blue! Effective suppressing fire is making the Reds hunkering down")
    elif (section1_location == "B5") or (section2_location == "B5") or (section3_location == "B5"):
        print ("The Reds cannot fire as their position is being overrun")
    else:
        Red_status = "Spent"
        blue_targets = get_blue_targets(section1_location, section2_location, \
                             section3_location, leader_in_section)
        print("Valid tagets are:")
        for bt in blue_targets:
            print(bt)
        print()
        shooting_at = []
        enemy = []
        while enemy == []:
            # This step is necessary to avoid counting spaces in the input string
            enemy = input ("Who did you shoot at [1, 2, 3, C - see your options above]?")                
            for infantry in enemy:
                if infantry != " ":
                    # print ("Add", infantry, "as a target")
                    shooting_at.append(infantry)
            if shooting_at in blue_targets:
                print("That is a valid target combination", shooting_at)
            else:
                print("Sorry that is an invalid combination", shooting_at)
                # Reset the enemy variable
                enemy = []
                shooting_at = []
        #print ("You are claiming", len(shooting_at), "targets")
        for target in shooting_at:
            #print ("Target =", target)
            d1 = dice_roll()
            if target != "C":
                if target == "1":
                    #print("** section one location**", section1_location)
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
                    print ("The commander is under fire")
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
numbers = range(1,7)
bars = [dice_history.count(n) for n in numbers]
#plt.bar(numbers,bars)
#plt.show()
#
# Still to do - Write Game Log to File
#
print("Game Data saved ..")
print("Thank you for playing!") 
