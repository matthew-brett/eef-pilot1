###########
Three girls
###########

.. code-links:: clear

Now we have the machinery we need to solve the three girls simulation.

Let's start with the problem of deciding whether the next child is a boy or a
girl.  We take a random number between 0 and 1, and if it is less than 0.5, we
will call that 1, where 1 means a girl.  Otherwise we will call it 0, where 0
means a boy.

We use the ``random`` module for that:

.. nbplot::

    >>> import random
    >>> type(random)
    <class 'module'>

The ``random`` function in the ``random`` module, returns a random number
between 0 and 1.

.. nbplot::
    :hide-from: all
    :show-to: doctest

    >>> random.seed(1966)

.. nbplot::

    >>> random.random()
    0.8899006007111...

Check what the function does with ``random.random?`` in a Notebook cell.

Now we'll decide if the next child is a boy or a girl.

.. nbplot::

    >>> # Get a random number, decide if it's a girl
    >>> random_no = random.random()
    >>> if random_no < 0.5:
    ...     # A girl
    ...     child = 1
    ... else:
    ...     # A boy
    ...     child = 0
    ...
    >>> child
    1

Run this a few times to make sure it produces 0 and 1 roughly the same number
of times.

********
Exercise
********

Now we want to make a function that returns 0 or 1, where 1 has a given
probability.  On our case we want 1 to have probability 0.5, but maybe we will
change our minds about that later.  Here's a template.  Fix it up to return 0
or 1 with the given probability.

.. nbplot::
    :hide-from: doctest

    >>> # In case you haven't done this already
    >>> import random

    >>> def get_0_or_1(prob_of_1):
    ...     # Return 0 or 1, where probability of 1 is given by prob_of_1
    ...     # To start with, we'll call this function setting prob_of_1 to 0.5
    ...     random_no = random.random()
    ...     if # What goes here?
    ...         result = 1
    ...     else:
    ...         result = 0
    ...     return result

.. nbplot::
    :hide-from: all
    :show-to: doctest

    >>> def get_0_or_1(prob_of_1):
    ...     # Return 0 or 1, where probability of 1 is given by prob_of_1
    ...     # To start with, we'll call this function setting prob_of_1 to 0.5
    ...     random_no = random.random()
    ...     if random_no < prob_of_1:
    ...         result = 1
    ...     else:
    ...         result = 0
    ...     return result

Here is a test cell.  It collects lots and lots of results, expecting the
average of all the results to add up to the given probability.

.. nbplot::

    >>> # Test cell for get_0_or_1, prob == 0.5
    >>> import numpy
    >>> prob = 0.5
    >>> samples = []
    >>> for i in range(10000):
    ...     samples.append(get_0_or_1(prob))
    >>> long_run_prob = numpy.mean(samples)
    >>> if abs(prob - long_run_prob) < 0.01:
    ...     print("Looks right")
    ... else:
    ...     print("Got", long_run_prob, "but expected something near", prob)

Now let's try when the ``prob_of_1`` is not 0.5 (below).

.. nbplot::

    >>> # Test cell for get_0_or_1, prob = 0.3
    >>> prob = 0.3
    >>> samples = []
    >>> for i in range(10000):
    ...     samples.append(get_0_or_1(prob))
    >>> long_run_prob = numpy.mean(samples)
    >>> if abs(prob - long_run_prob) < 0.01:
    ...     print("Looks right")
    ... else:
    ...     print("Got", long_run_prob, "but expected something near", prob)

Do you still get a good answer?  If not, try going to a piece of paper.  Draw
the interval 0 to 1 as a rectangle and shade in the part that you are looking
for in your function.

Do you agree that it is reasonable to check that the average of a large number
of 0 or 1 samples, with 1 having a given probability, will tend to be the
given probability?  For example, I'm checking the average of 10000 samples of
0, 1, with 1 having probability 0.3.  I'm testing that the average is about
0.3.  Is that reasonable?  How would you make that case to someone who didn't
believe you?

*************
Make a family
*************

Our task now is to make a ``for`` loop that collects four samples from
``get_0_or_1``, and counts how many of these values are 1. This is our number
of girls in the family.

.. nbplot::

    >>> children = []
    >>> for i in range(4):
    ...     child = get_0_or_1(0.5)
    ...     children.append(child)
    ...
    >>> n_girls = children.count(1)
    >>> n_girls

Exercise
========

Make a function called ``girls_in_family``, that takes no arguments.  The
function will make a series of children, just like the cell above, then count
the girls, and return the number of girls.  Like this:

.. nbplot::

    >>> def girls_in_family():
    ...     # Make a family of 4, return number of girls
    ...     # Your code here, likely from the cell above
    ...     return n_girls

.. nbplot::
    :hide-from: all
    :show-to: doctest

    >>> def girls_in_family():
    ...     # Make a family of 4, return number of girls
    ...     # Your code here, likely from the cell above
    ...     children = []
    ...     for i in range(4):
    ...         child = get_0_or_1(0.5)
    ...         children.append(child)
    ...     n_girls = children.count(1)
    ...     return n_girls

Call this function a few times to check you get some answer between 0 and 4:

.. nbplot::

    >>> girls_in_family()

Here's a test cell for your function.  When your function is right, this test
should pass.

.. nbplot::

    >>> # Test for girls_in_family
    >>> # Assumes the right answer is 0.25, on average
    >>> girl_counts = []
    >>> for i in range(10000):
    ...     girl_count = girls_in_family()
    ...     if girl_count < 0 or girl_count > 4:
    ...         print("Expecting number between 0 and 4, got", girl_count)
    ...     girl_counts.append(girl_count)
    ...
    >>> proportion = girl_counts.count(3) / 10000
    >>> if abs(proportion - 0.25) < 0.01:
    ...     print("Could well be right")
    ... else:
    ...     print("Expecting something near 0.25, got", proportion)

If you get that done quickly, try rewriting your ``girls_in_family`` function
to take two arguments, the probability of having a girl (up until now, 0.5),
and the number of children (up until now, 4).  It would start like this:

.. nbplot::
    :hide-from: doctest

    >>> def girls_in_family(prob_girl, n_chilren):
    ...     # Make a family of n_children, return number of girls
    ...     # Your code here
    ...     return n_girls

Modify the test cell above to use this new code, initially using a probability
of 0.5 and number of children of 4.  Try adapting the test to check for the
right answer with other probabilities and other numbers of children.

***************
How many girls?
***************

Now we take that code, and run it 10000 times.  We collect the "number of
girls" value in a list, for each time we go through the loop.

At the end, we calculate how many families had 3 girls.  Divide by the number
of families you made (10000).

Something like this:

.. nbplot::

    >>> girl_counts = []
    >>> for i in range(10000):
    ...     girl_count = girls_in_family()
    ...     girl_counts.append(girl_count)
    ...
    >>> proportion = girl_counts.count(3) / 10000
    >>> print("Estimate for probability of 3 girls is", proportion)

Run this a few times, to get an idea of the range of answers.

Exercise
========

Up until now, we've assumed that the chance that a child is a boy is 0.5.  Now
assume the proportion of boys born in the UK is 0.513 [#male-births]_.  Hence
the proportion of girls is 1-0.513 = 0.487.

Here is a working function to return the number of girls in a family of 4,
given a probability of having a girl of 0.5:

.. nbplot::

    >>> def girls_in_family():
    ...     # Make a family of 4, return number of girls
    ...     # Your code here, likely from the cell above
    ...     children = []
    ...     for i in range(4):
    ...         child = get_0_or_1(0.5)
    ...         children.append(child)
    ...     n_girls = children.count(1)
    ...     return n_girls

Here's the code cell we used above to calculate the number of families with 3
girls:

.. nbplot::

    >>> girl_counts = []
    >>> for i in range(10000):
    ...     girl_count = girls_in_family()
    ...     girl_counts.append(girl_count)
    ...
    >>> proportion = girl_counts.count(3) / 10000
    >>> print("Estimate for probability of 3 girls is", proportion)

Change the ``girls_in_family`` function above to use the actual probability of
having a girl.

When you've done that, run the cell above to get a more realistic estimate of
the chances of exactly 3 girls in a family of 4.

Do you expect the answer to be less or greater than the answer you got when
the probability was 0.5?

Given that the correct answer is 0.25, with a probability-of-having-girl of
0.5, what would be your guess at the correct answer, with a probability of
0.487?  Why?

.. [#male-births] `Official UK government statistics
   <https://www.gov.uk/government/statistics/gender-ratios-at-birth-in-great-britain-2010-to-2014>`_
   give the birth ratio as 105.3. This the number of boys born for every 100
   girls.  The proportion is therefore 105.3 / (100 + 105.3).
