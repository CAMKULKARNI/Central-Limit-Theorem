import random
import matplotlib.pyplot as plt
from tqdm import tqdm

# Define the weighted dice as a dictionary
dice_weights = {1: 0.40, 2: 0.5, 3: 0.5, 4: 0.5, 5: 0.5, 6: 0.40}

# Roll the dice and add up the sum
sums = []
for i in tqdm(range(10000)):
    dice_rolls = [random.choices(list(dice_weights.keys()), list(
        dice_weights.values()), k=1)[0] for _ in range(6)]
    sums.append(sum(dice_rolls))

# Plot a histogram of the sum of rolls
plt.hist(sums, bins=range(6, 37), align='left')
plt.xlabel('Sum of 6 dice rolls')
plt.ylabel('Frequency')
plt.show()
