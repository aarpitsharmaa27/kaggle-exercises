# Function cost_of_project(engraving, solid_gold) returns total ring price.
# Pricing:
# Gold plated: base $50 + $7 per engraved char
# Solid gold: base $100 + $10 per engraved char
# Spaces & punctuation count as engraved chars


def cost_of_project(engraving, solid_gold):
    if solid_gold == True:
        cost = 100 + (10 * len(engraving))
    else:
        cost = 50 + (7 * len(engraving))
    return cost
print(cost_of_project("engraved", True))