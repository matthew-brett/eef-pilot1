##########################
Testing Brexit Proportions
##########################

.. code-links::

If you look back at :doc:`brexit_analysis`, we have:

* 541 people who said they voted to Leave the EU;
* 774 people who said they voted to remain.
* Therefore we have a total of 541 + 774 = 1315 people who voted and told us
  what they voted.

This gives us a proportion of Leave / (Leave + Remain) of:

.. nbplot::

    >>> #: brexit proportion in survey
    >>> 541 / (541 + 774)
    0.4114068441064639

We also know that the `final referendum proportion
<https://www.electoralcommission.org.uk/find-information-by-subject/elections-and-referendums/past-elections-and-referendums/eu-referendum/electorate-and-count-information>`_
of Leave / (Leave + Remain) was 0.519.

These proprtions seem very different?  But could such a difference have come
about by chance?

Now we need to formulate exactly what we mean by "come about by chance"?

Specifically, we need for formulate our null hypothesis.  The null hypothesis
is that the result did come about by chance.

So, what is the chance element here?

We could say it is the sampling.  That is, the survey has a sample of 1315
people.  By chance, the sample could have more or less Leave voters, and
therefore generate a higher or lower proportion.

Here's the null hypothesis: when the survey took its sample, it had the same
chance of picking a Leave voter as for the whole voting population.  The
proportion of 0.41 is within the bounds of the variations we might expect from
random sampling of voters.

The Leave proportion is our *statistic* calculated from the sample.

If we draw 1315 voters at random, and calculate this proportion, and do this
many times, the calculated proportion will have some distribution or spread.

This is called the *sampling distribution* of the statistic.

We will reject the null hypothesis if 0.411 would be very unusual given the
sampling distribution of the statistic.

So, how do we make this sampling distribution?

We assume that the probability of selecting a leave voter is actually 0.519.

We use our ``get_0_or_1`` function from :doc:`three_girls` to return a 1 (for
Leave voter) or 0 (for Remain voter):

.. nbplot::

    >>> #: The random module
    >>> import random

.. nbplot::
    :hide-from: all
    :show-to: doctest

    >>> #: keep this for exercise built page
    >>> random.seed(1966)

.. nbplot::

    >>> #: The random module
    >>> def get_0_or_1(prob_of_1):
    ...     # Return 0 or 1, where probability of 1 is given by prob_of_1
    ...     # To start with, we'll call this function setting prob_of_1 to 0.5
    ...     random_no = random.random()
    ...     if random_no < prob_of_1:
    ...         result = 1
    ...     else:
    ...         result = 0
    ...     return result

We call it with our desired probability of 1:

.. nbplot::

    >>> #: call the function
    >>> #: remember the brackets at the end
    >>> get_0_or_1(0.519)
    0

In :doc:`three_girls`, a single trial was four children.  In our case, a
single trial is 1315 Leave or Remain voters drawn at random. We calculate the
statistic for each trial:

.. nbplot::

    >>> #: The statistic value from a single trial
    >>> def one_proportion():
    ...     votes = []
    ...     for i in range(1315):
    ...         vote = get_0_or_1(0.519)
    ...         votes.append(vote)
    ...     # We add all the 1s together to get the number of Leave voters
    ...     brexits = sum(votes)
    ...     return brexits / len(votes)

Run a single trial:

.. nbplot::

    >>> #: Result of one trial
    >>> one_proportion()
    0.5239543726235741

Now we want the sampling distribution of this proportion.  So, we're going to
draw 10000 random samples, and look at the distribution of the statistic (the
proportion).  This is your job:

.. nbplot::

    >>> #: Number of trials
    >>> n_trials = 10000

.. nbplot::

    >>> #- Make a list to contain the proportion for each trial
    >>> proportions = []
    >>> #- Use a for loop to make 10000 trials.
    >>> #- For each trial, calculate the proportion and store it in the
    >>> #- "proportions" list.
    >>> #- You now have 10000 proportions.
    >>> for i in range(n_trials):
    ...     proportion = one_proportion()
    ...     proportions.append(proportion)

.. mpl-interactive::

.. nbplot::

    >>> #: The stuff you need for plotting a histogram
    >>> import matplotlib.pyplot as plt

Plot the histogram of the sampling distribution you have just collected:

.. nbplot::

    >>> #- plot the histogram of the sampling distribution
    >>> plt.hist(proportions)
    (...)

The value we found in our survey data was 0.411.   How likely do you think
that value is, given the sampling distribution you have just made?

Remember, your job was to get some hard evidence about whether the survey
company is right to claim that there was no bias in their survey.  So, they
are claiming that the proportion of 0.41 that they found was a reasonable one
that could have come about because they were somewhat unlucky in their random
sample.  How unlucky would they have to be?

Do you have evidence that they did not do a random sample?  That the
respondents did not answer honestly?  Both?   How can you be sure?
