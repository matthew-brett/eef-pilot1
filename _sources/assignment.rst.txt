##########
Assignment
##########

.. notes

   Started to seem long-winded.  About 15 minutes.

.. what we have to cover

   A variable as a name referring to a value.
   LHS and RHS

.. code-links:: clear


A statement is an instruction that the Python interpreter can execute.

We are going to start with an *assignment* statement.

*********************
Assignment statements
*********************

Here is an assignment statement:

.. nbplot::

    >>> a = 10

Prese shift-Return in the Notebook to execute this statement.

An assignment statement has two parts:

* The Left Hand Side or LHS - to the left of the equals sign - here ``a``.
* The Right Hand Side or RHS - the right of the equals sign - here ``10``.

The LHS - ``a`` is a *variable name*.

The RHS - ``10`` is an *expression*.  When we *evaluate* the expression, we
return a *value*.

When you learn programming, and even when you get a lot of experience, it is
useful to read to yourself what the code is doing.

Read the statement above as ``a gets the value 10``.

To repeat: an assignment statement is

    A variable name, followed by ``=`` followed by an expression.

    It should be read as "the <variable name> gets the value <value from
    evaluating the expression>".

For ``a = 10`` the expression ``10`` is very simple, but we can make the
expression more complicated, like this:

.. nbplot::

    >>> b = 2 + 3

Read this as "``b`` gets the value from evaluating ``2 and 3``".

While we are here, you can also use ``*`` for *multiply* and ``/`` for divide.
For example:

.. nbplot::

    >>> e = 2 * 3

.. nbplot::

    >>> f = 6 / 3

**************
Variable names
**************

Variable names can contain any letters or numbers, or the ``_`` character, but
they can't begin with a number.  Are these valid variable names?

.. nbplot::

    >>> c3 = 5 + 6

.. nbplot::

    >>> my_variable = 11 - 2

.. nbplot::

    >>> _Dr_Strange = 42 / 7

.. nbplot::

    >>> 3_little_piggies = 3

You can see what value a variable has in the jupyter notebook, by entering the
variable name on a line on its own:

.. nbplot::

    >>> b
    5

********************
Syntax in assignment
********************

Remember, Python is a *language*.  For a statement to be *valid* in the
language, it has to match the rules.  These are called *syntax rules*.  You
already know that an assignment statement is:

    A variable name, followed by ``=`` followed by an expression.

Are these valid assignment statements?

.. nbplot::

    >>> e = 3 + 10
    >>> e  #doctest: +SKIP

.. nbplot::

    >>> f = e + 3
    >>> f  #doctest: +SKIP

.. nbplot::

    >>> 5 = 3   #doctest: +SKIP
    >>> 5  #doctest: +SKIP

************************
Variables in expressions
************************

The great advantage of variables, is that they can be used in expressions.
For example:

.. nbplot::

    >>> a = 10

.. nbplot::

    >>> c = a

Read this as "``c`` gets the value from evaluating ``a``".  What is the result
from evaluating ``a``?

.. nbplot::

    >>> b = 5

.. nbplot::

    >>> d = a + b

Read this as "``d`` gets the value from evaluating ``a + b``".  What do you
get from evaluating ``a + b``?

How about this statement?

.. nbplot::

    >>> d = d + 1

Is it a valid assignment statement?  How would you read it?  What would you
get for:

.. nbplot::

    >>> d  # doctest: +SKIP

This assignment statement can be called an *update* assignment, because the
value in ``d`` gets *updated* to the previous value in ``d``, plus 1.

********
Exercise
********

Get into pairs.  Allocate the driver and the navigator.  Get a piece of paper
and a pen or pencil, and put it next to you.  Now try these.

Make a variable called ``my_variable`` that is set to have the value 23.

Make a variable called ``another_variable`` that is set to have the value 9.

Add one to the variable ``another_variable``.  After you have done this,
``another_variable`` should have the value 10.

Make a variable called ``third_variable`` that gets the value of
``another_variable`` multiplied by ``my_variable``.

Show the value that ``third_variable`` has.

Have a look at this set of assignments.  What did I do wrong?

.. nbplot::

    >>> p = 10
    >>> q = 21
    >>> r = p + s  # doctest: +SKIP
