""" Testing Brexit Proportions
"""
#: brexit proportion in survey
541 / (541 + 774)

#: The random module
import random

#: keep this for exercise built page
random.seed(1966)

#: The random module
def get_0_or_1(prob_of_1):
    # Return 0 or 1, where probability of 1 is given by prob_of_1
    # To start with, we'll call this function setting prob_of_1 to 0.5
    random_no = random.random()
    if random_no < prob_of_1:
        result = 1
    else:
        result = 0
    return result

#: call the function
#: remember the brackets at the end
get_0_or_1(0.519)

#: The statistic value from a single trial
def one_proportion():
    votes = []
    for i in range(1315):
        vote = get_0_or_1(0.519)
        votes.append(vote)
    # We add all the 1s together to get the number of Leave voters
    brexits = sum(votes)
    return brexits / len(votes)

#: Result of one trial
one_proportion()

#: Number of trials
n_trials = 10000

#- Make a list to contain the proportion for each trial
#- Use a for loop to make 10000 trials.
#- For each trial, calculate the proportion and store it in the
#- "proportions" list.
#- You now have 10000 proportions.

#: The stuff you need for plotting a histogram
import matplotlib.pyplot as plt

#- plot the histogram of the sampling distribution
