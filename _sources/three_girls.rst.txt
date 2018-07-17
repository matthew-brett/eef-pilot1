###########
Three girls
###########

.. code-links:: clear

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

    >>> # Make list to store counts of girls in each family
    >>> girl_counts = []

    >>> # Make 10000 families
    >>> for i in range(10000):
    ...     # Make one family
    ...     family = []
    ...     # Have 4 children
    ...     for j in range(4):
    ...         child = random.choice('GB')
    ...         family.append(child)
    ...     # Store the number of girls in this family
    ...     n_girls = family.count('G')
    ...     girl_counts.append(n_girls)
    ...
    >>> # Get the number of families with 3 girls
    >>> n_with_3 = girl_counts.count(3)
    >>> proportion = n_with_3 / 10000

.. nbplot::

    >>> proportion
    0.2548
