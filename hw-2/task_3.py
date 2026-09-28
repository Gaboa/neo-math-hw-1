import math

# Dream Team
# Positions: 2 Back, 2 Front, 1 UI
# Candidates: 8 Back, 6 Front, 4 UI

back_combinations = math.comb(8, 2)
front_combinations = math.comb(6, 2)
ui_combinations = math.comb(4, 1)

total_combinations = back_combinations * front_combinations * ui_combinations
print(f"Back End combinations: {back_combinations}")
print(f"Front End combinations: {front_combinations}")
print(f"UI combinations: {ui_combinations}")
print(f"Team combinations: {total_combinations}")