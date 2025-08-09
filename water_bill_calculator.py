'''
Write a function get_water_bill(num_gallons) that calculates the water bill based on usage tiers:

0 to 8,000 gallons → $5 per 1000 gallons

8,001 to 22,000 gallons → $6 per 1000 gallons

22,001 to 30,000 gallons → $7 per 1000 gallons

Above 30,000 gallons → $10 per 1000 gallons  '''



def get_water_bill(num_gallons):
    if num_gallons >= 30001:
        amount = 10 * (num_gallons / 1000)
    elif num_gallons >= 22001:
        amount = 7 * (num_gallons / 1000)
    elif num_gallons >= 8001:
        amount = 6 * (num_gallons / 1000)
    elif num_gallons >= 0:
        amount = 5 * (num_gallons / 1000)
    return amount
print(get_water_bill(10000))
print(get_water_bill(25000))