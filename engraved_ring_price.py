

# Q: Create a Python function cost_of_project() to calculate the price of a custom engraved ring.
# The function takes:
#   - engraving (string): the text to engrave on the ring (spaces and punctuation count as characters)
#   - gold_ring (boolean): True if the ring is solid gold, False if the ring is gold plated


def cost_of_project(engraving, gold_ring):
    cost = gold_ring * (1000 + 50 * len(engraving)) + (not gold_ring) * (500 + 50 * len(engraving))
    return cost

print(cost_of_project("Arpit", True))



#-------------------- Q 2 -------------------------------------------------------------------------------#



def cost_of_project(engraving, gold_ring):
    cost = gold_ring * (1000 + 50 * len(engraving)) + (not gold_ring) * (500 + 50 * len(engraving))
    return cost

print(cost_of_project("Hey Marry Me", False))








