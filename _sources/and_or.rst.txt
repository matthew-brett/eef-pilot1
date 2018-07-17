######################
and, or in expressions
######################

.. code-links:: clear

Imagine I had these variables:

.. nbplot::

    >>> my_number = 10
    >>> my_name = "Matthew"

We are already familiar with expressions like these:

.. nbplot::

    >>> my_number == 10
    True
    >>> my_number == 9
    False
    >>> my_name == "Matthew"
    True

We can combine expressions like these with ``and`` and ``or``.

Consider ``and``. Here is an example:

.. nbplot::

    >>> my_number == 10 and my_name == "Matthew"
    True

``and`` takes a expression on the left and evaluates it.  If that statement is
True, it then evaluates the statement on the right.  If both are True, the
``and`` expression results in True.  If either are False, it results in False.

This is the same logic as we use in speech.  If I say "jump if the table is
brown and the floor is gray", when do you jump?  You only jump both of these
are true: "the table is brown" and "the floor is gray".  You don't jump if the
table is red and the floor is gray, or if the table is brown and the floor is
white.  Both clauses have to be true.

.. nbplot::

    >>> # Both clauses are True so the "and" is True
    >>> my_number == 10 and my_name == "Matthew"
    True
    >>> # Only the left clause is True so the "and" is False
    >>> my_number == 10 and my_name == "John"
    False
    >>> # Only the right clause is True so the "and" is False
    >>> my_number == 9 and my_name == "Matthew"
    False

Now consider ``or``.  Here is an example:

.. nbplot::

    >>> my_number == 9 or my_name == "Matthew"
    True

``or`` takes an expression on the left and evalualates it.  If it is True, it
stops and returns True.  Otherwise it continues and evaluates the experession
on the right.  If this is True, it returns True, otherwise it returns False.

This is also the same logic as we use in speech.  If I say "jump if the table
is red or the floor is gray", you jump *either* if the table is red, *or* if
the floor is gray.  Only one of the two clauses has to be true.

.. nbplot::

    >>> # Just the right clause is True, but that makes the "or" True
    >>> my_number == 9 or my_name == "Matthew"
    True
    >>> # Just the left clause is True, but that makes the "or" True
    >>> my_number == 10 or my_name == "John"
    True
    >>> # Both of these are True, so the "or" is True
    >>> my_number == 10 or my_name == "Matthew"
    True
    >>> # Neither of these are True, so the "or" is False
    >>> my_number == 9 or my_name == "John"
    False
