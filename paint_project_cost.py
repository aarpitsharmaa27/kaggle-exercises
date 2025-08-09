

# Q: Calculate the total cost of paint for given wall and ceiling area
# when partial gallons are allowed, then round up the cost to nearest gallon price.


def get_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    total_area = sqft_walls + sqft_ceiling
    gallons_needed = total_area / sqft_per_gallon
    total_cost = gallons_needed * cost_per_gallon
    return total_cost
project_cost = get_cost(432 , 144, 400, 15)
print(project_cost)

# The output of above code is 21.5999999998

# now we round off current answer by using ceil function

import math
new_value = math.ceil(project_cost)
print(new_value)




