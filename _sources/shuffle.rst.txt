#######
Shuffle
#######

.. code-links:: clear

Sometimes we want to take the elements in a list, and put them into a random
order.

Luckily, Python thought of that for us.

.. nbplot::

    >>> import random

.. nbplot::
    :hide-from: all
    :show-to: doctest

    >>> random.seed(1966)

.. nbplot::

    >>> my_list = [5, 1, 3, 2, 7]
    >>> my_list
    [5, 1, 3, 2, 7]

Now we shuffle the elements to a random order:

.. nbplot::

    >>> random.shuffle(my_list)
    >>> my_list
    [1, 7, 3, 2, 5]
    >>> random.shuffle(my_list)
    >>> my_list
    [2, 5, 3, 1, 7]
    >>> random.shuffle(my_list)
    >>> my_list
    [7, 3, 2, 5, 1]
