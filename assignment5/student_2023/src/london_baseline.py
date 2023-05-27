# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.
import utils

with open("birth_dev.tsv", "r") as f:
    num_lines = sum(1 for _ in f)

print(utils.evaluate_places('birth_dev.tsv', ["London"]*num_lines))

