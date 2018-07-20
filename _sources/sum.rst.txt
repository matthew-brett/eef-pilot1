###
Sum
###

.. requires: if_for

It does what it says on the tin:

.. nbplot::

    >>> a_list = [-2, 1, 7, 8, 11]
    >>> total = 0
    >>> for value in a_list:
    ...     total = total + value
    ...
    >>> total
    25

We can do the same in one line with ``sum``:

.. nbplot::

    >>> sum(a_list)
    25
