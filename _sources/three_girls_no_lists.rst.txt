###########
Three girls
###########

We will use the ``choice`` function from the  ``random`` module.

.. nbplot::

    >>> import random

This is a module:

.. nbplot::

    >>> type(random)
    <class 'module'>

Use ``random.`` and then Tab to see the functions inside the module, from
within the Notebook.

We will use ``random.choice``, a function within the ``random`` module.

You can check the help with ``random.choice?`` in the Notebook.

Here we ask it to choose randomly between the two letters in the string,
``"HT"``:

.. nbplot::
    :hide-from: all
    :show-to: doctest

    >>> random.seed(1966)

.. nbplot::

    >>> random.choice('HT')
    'H'
    >>> random.choice('HT')
    'T'
    >>> random.choice('HT')
    'H'
    >>> random.choice('HT')
    'H'

A coin toss!

Now we have everything we need to solve the problem:

.. nbplot::

    >>> # Make a counter to store how many times we have 3 girls
    >>> counter_3girls = 0

    >>> # Make 10000 families
    >>> for i in range(10000):
    ...     # Make one family
    ...     # A counter to store how many girs in this family
    ...     counter_girls = 0
    ...     # Have 4 children
    ...     for j in range(4):
    ...         coin = random.choice('HT')
    ...         if coin == 'H':
    ...             counter_girls = counter_girls + 1
    ...
    ...     # Increase counter if this is a 3 girl family
    ...     if counter_girls == 3:
    ...         counter_3girls = counter_3girls + 1

    >>> proportion = counter_3girls / 10000

.. nbplot::

    >>> proportion
    0.2548
