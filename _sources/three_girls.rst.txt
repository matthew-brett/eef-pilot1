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
    >>> if random_no > 0.5:
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

Now let's try when the ``prob_of_1`` is not 0.5.  Do you still get a good
answer?

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

Now make a for loop that collects four samples from ``get_0_or_1``, and
calculates the sum of those values.  The four values are four children.  The
sum is the number of girls.

Now take that code, and run it 10000 times.  Collect the "number of girls"
value in a list, for each time you go through the loop.

At the end, calculate how many families had 3 girls.  Divide by the number of
families you made (10000).
