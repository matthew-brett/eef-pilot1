#############################
Comparisions, True, and False
#############################

.. code-links:: clear

We have seen expressions returning values that are numbers, and strings.  Now
we come across a new type of value, called *boolean* values.

These are values of ``True`` and ``False``.

.. nbplot::

    >>> a = 10
    >>> # Is a less than 15?
    >>> a < 15
    True
    >>> a < 8
    False

We can test exact equality with double equals - ``==``:

.. nbplot::

    >>> a == 15
    False
    >>> a == 10
    True

We can test for inequality (not exactly equal) with ``!=`` (read as "not
equal"):

.. nbplot::

    >>> a != 15
    True
    >>> a != 10
    False
