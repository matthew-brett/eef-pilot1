#################
Print, If and For
#################

.. code-links:: clear

*****
Print
*****

``print`` is useful function:

.. nbplot::

    >>> type(print)
    <class 'builtin_function_or_method'>

It prints out the values that you pass it, such as strings or numbers.

.. nbplot::

    >>> print(10)
    10
    >>> my_name = "Matthew"
    >>> print(my_name)
    Matthew

This can be useful in the Notebook to show values as we execute things within
a cell.

.. for as "do something N times"
   if

**
If
**

We have already seen *assignment* statements (:doc:`assignment`).  We saw that
they have the form: LHS ``=`` RHS, where the LHS is a variable name and the
RHS is an expression.

We saw expressions on their own at the end of Notebook cells, to show us a
value.

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

    >>> for i in range(10):
    ...     print(i)
    ...
    0
    1
    2
    3
    4
    5
    6
    7
    8
    9

There are several new things here.  Notice ``range(10)``.  This looks like a
function, and it looks like it returns 10 numbers, starting at 0 and
continuing through to 9.   That's good enough for our purposes.

Next we see that the for statement is rather like the ``if`` statement.  It
has form:

* ``for`` followed by
* a variable name (in this case ``i``, called the *loop variable*) followed
  by:
* an expression that retuns a series of things (``range(10)`` returns a series
  of numbers from 0 through 9) followed by:
* ``:`` (a colon) followed by
* an indented *block* of code (``    print(i)``)

For statments are just a little more complicated than `if` statements, and it
is worth going through the logic carefully.  Read the for statement above like
this:

* in the first iteration of the loop, set ``i`` to have value 0.  Then print
  ``i``;
* in the second iteration of the loop, set ``i`` to have value 1.  Then print
  ``i``;
* in the third iteration of the loop, set ``i`` to have value 2.  Then print
  ``i``;

and so on.

Let's try some exercises.

Use a ``for`` loop to add up all the numbers between 0 and 10.

Use a ``for`` loop to count how many numbers from 0 through 99 that are
divisible by both 7 and 4.
