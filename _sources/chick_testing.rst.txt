################
Permuting chicks
################

.. code-links:: clear

.. note::

    This page uses Python 3 - the most recent version of Python.  If you've
    got Python 2, start by running this line, to make Python 2 work more like
    Python 3.

    .. nbplot::

        >>> from __future__ import division

In a moment we are going to compare some measures we collected from two
different groups.

The data we are going to compare is from an experiment in which domestic
chicks were fed a feed supplement (``with_supplement``), or were fed a normal
diet without supplements (``no_supplement``). They were weighed after 2 weeks
on these diets to test whether the supplement increases chick weight.

Here are the chick weights for the two groups:

.. nbplot::

    >>> no_supplement = [179, 160, 136, 227, 217, 168, 108, 124, 143, 140]
    >>> with_supplement = [309, 229, 181, 141, 260, 203, 148, 169, 213, 257, 244, 271]

``no_supplement`` and ``with_supplement`` are lists.

We can get the number of items in the list using ``len``. For example, there
are 10 chicks in the ``no_supplement`` group:

.. nbplot::

    >>> len(no_supplement)
    10

We can get the sum of the values in the list with ``sum``:

.. nbplot::

    >>> sum(no_supplement)
    1602

.. nbplot::

    >>> # Checking that the sum is the addition of all the elements.
    >>> 179 + 160 + 136 + 227 + 217 + 168 + 108 + 124 + 143 + 140
    1602

The *mean* of the values in the list is defined as the sum divided by
the number of items. For example, here is the mean of the weights in the
``no_supplement`` group:

.. nbplot::

    >>> sum(no_supplement) / len(no_supplement)
    160.2

Here is a function to calculate the mean, like this:

.. nbplot::

    >>> def mean(some_list):
    ...     """ Calculates the mean of the values in `some_list`
    ...     """
    ...     return sum(some_list) / len(some_list)

Now we can get the mean with:

.. nbplot::

    >>> mean(no_supplement)
    160.2

The mean is greater for the ``with_supplement`` group:

.. nbplot::

    >>> mean(with_supplement)
    218.75

The difference between the means is:

.. nbplot::

    >>> observed_difference = mean(with_supplement) - mean(no_supplement)
    >>> observed_difference
    58.55000000000001

We see that the means of the two groups are different - but can we be
confident that this difference did not come about by chance?

Here's the function from :doc:`brexit_ages`.  It permutes the values between
the two lists.

.. nbplot::

    >>> # Just in case you haven't imported this already
    >>> import random

    >>> def join_shuffle_split(first_list, second_list):
    ...     # Pool the lists, shuffle, split into lists of original length
    ...     first_len = len(first_list)
    ...     pooled = first_list + second_list
    ...     random.shuffle(pooled)
    ...     both = [pooled[:first_len], pooled[first_len:]]
    ...     return both

Here's a function from :doc:`brexit_ages` that uses ``join_shuffle_split`` to
get fake groups, and calculates the mean difference on those groups:

.. nbplot::

    >>> def difference_in_means(first_list, second_list):
    ...     """ Shuffle values across lists, calculate difference in means.
    ...     """
    ...     fake_lists = join_shuffle_split(first_list, second_list)
    ...     group_A = fake_lists[0]
    ...     group_B = fake_lists[1]
    ...     return mean(group_B) - mean(group_A)

********
Exercise
********

Build up the *sampling distribution* of the difference in means.

Make an empty list called ``differences``.

Make a ``for`` loop that runs 10000 times.

In the ``for`` loop, make a new mean difference using ``difference_in_means``.

Append this mean difference to ``differences``.

``differences`` now contains an estimate of the sampling distribution.

Show a histogram of the distribution.

Maybe using the code from the end of :doc:`brexit_ages`, count how many of
values in ``differences`` (the sampling distribution) are greater than, or
equal to ``observed_difference``.

Divide by 10000 to get the proportion of the sampling distribution that is
greater than or equal to ``observed_difference``.

Do you think ``observed_difference`` is likely, if the null hypothesis is
true?
