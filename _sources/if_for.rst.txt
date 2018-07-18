##########
If and For
##########

.. code-links:: clear

**
If
**

We have already seen *assignment* statements (:doc:`assignment`).  We saw that
they have the form: LHS ``=`` RHS, where the LHS is a variable name and the
RHS is an expression.

Now we add a couple of essential statements you will use all the time: ``if``
statements and ``for`` statements.

Here is an ``if`` statement:

.. nbplot::

    >>> x = 3
    >>> if x == 3:
    ...     print("x does equal 3")
    ...
    x does equal 3

There are a few new things here.  This ``if`` statement has the form:

* ``if`` followed by
* an expression (``x == 3``) followed by
* ``:`` (a colon) followed by
* an indented *block* of code (``    print("x does equal 3")``)

Remeber that an expression evaluates to a result.  The trick of the ``if``
statement, is that it will only run the indented block of code above, if the
expression evaluates to True.  Try it.  Run the code above.  Now try:

.. nbplot::

    >>> x = 4
    >>> if x == 3:
    ...     print("x does equal 3")
    ...

It doesn't print anything because ``x == 3`` is False.

Next notice that Python knows which code to run, when ``x == 3`` is True,
because of the *indentation*.   It runs all the code that is indented, when
``x == 3`` is True, and ignores that code otherwise.  There can be several
lines in the indented block, but they all have to be indented the same amount:

.. nbplot::

    >>> x = 3
    >>> if x == 3:
    ...     print("Here in the if block")
    ...     print("x does equal 3")
    ...     print("Still in if block")
    ...
    Here in the if block
    x does equal 3
    Still in if block

Now an exercise.  For this exercise, you will need the *modulo* operator:
``%``.  In an expression it returns the remainder of dividing the number on
the left by the number on the right.  Here are some examples:

.. nbplot::

    >>> 3 % 2
    1
    >>> 4 % 2
    0
    >>> 13 % 3
    1
    >>> 13 % 13
    0

You can test if one number is divisible by another number, like this:

.. nbplot::

    >>> x = 12
    >>> # Is x divisible by 4?
    >>> # If it is, then x % 4 will be 0
    >>> x % 4 == 0
    True

.. nbplot::

    >>> x = 13
    >>> # Now x % 4 gives 1
    >>> x % 4 == 0
    False

The exercise is to write an ``if`` statement that prints "yes" if the number
``x`` is exactly divisible by 7, and prints nothing otherwise.  Test your code
by setting various values of ``x``, and running the cell.

What happens if you forget the colon ``:`` at the end of the ``if`` line?

What happens if you forget to indent the block?

*********
For loops
*********

As we've seen by now, we often want to repeat the same thing multiple times.
The way we usually do this in Python is using a ``for`` loop.  A for loop
looks like this:

.. nbplot::

    >>> my_list = [1, 3, 5]
    >>> for value in my_list:
    ...     print(i)
    ...
    1
    3
    5

We see that the for statement is rather like the ``if`` statement.  It
has form:

* ``for`` followed by
* a variable name (in this case ``i``, called the *loop variable*) followed
  by:
* an expression that evaluates to a sequence of things - in our case, the list
  ``[1, 3, 5]``;
* ``:`` (a colon) followed by
* an indented *block* of code (``    print(i)``)

For statments are just a little more complicated than `if` statements, and it
is worth going through the logic carefully.  Read the for statement above like
this:

* in the first iteration of the loop, set ``value`` to have value 1.  Then print
  ``value``;
* in the second iteration of the loop, set ``value`` to have value 3.  Then
  print ``value``;
* in the third iteration of the loop, set ``value`` to have value 5.  Then
  print ``value``;

Put another way, the ``for`` loop above does exactly the same as:

.. nbplot::

    >>> # First time through the loop
    >>> value = 1
    >>> print(value)
    >>> # Second time through the loop
    >>> value = 1
    >>> print(value)
    >>> # Third time through the loop
    >>> value = 1
    >>> print(value)

********
Exercise
********

Make a list of all the odd numbers between 1 and 9 inclusive.

Use a ``for`` loop to print out each of these numbers.

Use a ``for`` loop to print out the sum of all these numbers.  Your loop will
look something like this::

    >>> # A variable to hold the running total of the numbers
    >>> total = 0
    >>> for value in odd_numbers:
    ...     "Do something here"
    ...
    >>> total
    25

Use a ``for`` loop to count how many odd numbers between 1 and 9 inclusive are
divisible by 3.

*****
Range
*****

Sometimes we want to use many more than a few goes round the for loop.  For
example, maybe I want to do the same thing 100 times.  I could type in a huge
list with 100 elements, as in ``my_list = [0, 1, 2, 3, 4, .. ]`` and so on.
That seems pretty boring.  Is there an automatic way to do this?

Yes!  It's the ``range`` function.

Here is ``range`` in action:

.. nbplot::

    >>> my_range = range(5)
    >>> my_range
    range(0, 5)

This is a slightly odd type of value, that will give me all the numbers
starting a 0, and going up to, but not including, 5.  We can convert this
thing into a list to show these numbers:

.. nbplot::

    >>> my_numbers = list(my_range)
    >>> my_numbers
    [0, 1, 2, 3, 4]

Notice the 4 - up to *but not including* 5.

********
Exercise
********

Use a ``for`` loop to print out the sum of the numbers from 0 to 40,
inclusive.  Your loop will look something like this::

    >>> # A variable to hold the running total of the numbers
    >>> total = 0
    >>> for value in ?
    ...     "Do something here"
    ...
    >>> total
    820
