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

***
And
***

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

********
Exercise
********


Start with this code fragment.  Click the triple arrows button at the top right
to turn off the ``>>>`` at the front of each line, then copy the code into a cell in a
Notebook.

Run the cell.  It should return False.  Modify the variables ``my_name`` and
``your_name`` until the expression returns True.

.. nbplot::

    >>> # Change my_name and your_name to make the expression below True
    >>> my_name = "Matthew"
    >>> your_name = "Yogi"
    >>> len(my_name) == 5 and len(your_name) == 5
    False

Now try the code cell below.  Write your expression.  Evaluate the expression
with the variables below.  It should return True.  Change ``name`` so that,
when you evaluate again, it returns False.  Change it back, so it returns True
again. Now change ``a`` so that it returns False again.

.. nbplot::

    >>> # Make expression that is True only when a is less than 5 and
    >>> # number of characters in name is greater than 5.
    >>> a = 4
    >>> name = "Yogi"
    >>> # Your expression here

In the cell below, I wanted to return True if ``x`` is less than 10 and ``y``
is greater than, or equal to ``x``.  It isn't working right.  Copy the code
into a cell, and fix it until it works. Check it works right for other values
of ``x`` and ``y``.

.. nbplot::

    >>> x = 9
    >>> y = 9
    >>> # Here's my expression - I was expecthing this to be True
    >>> x < 10 and x >= x  # doctest: +SKIP

**
Or
**

Now consider ``or``.  Here is an example:

.. nbplot::

    >>> my_number == 9 or my_name == "Matthew"
    True

``or`` takes an expression on the left and evaluates it.  If it is True, it
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

********
Exercise
********

.. nbplot::

    >>> # Change the table_colour variable to make the expression True.
    >>> # Change it back to "red" again to make it false again.
    >>> # Change the floor_colour to make the expression True.
    >>> table_colour = "red"
    >>> floor_colour = "brown"
    >>> table_colour == "brown" or floor_colour == "gray"
    False

Make an expression that evaluates to True if either of the following are True:

* ``x`` is less than 21
* ``y`` is greater than 42

Start with the values below, and confirm that your expression evaluates to
True.  Now try different values of ``x`` and ``y`` to show that it behaves
correctly in all possible combinations.

.. nbplot::

    >>> # Evaluate to True if either of the following are True:
    >>> #   x is less than 21
    >>> #   y is greater than 42
    >>> x = 20
    >>> y = 50
    >>> # Your expression here
