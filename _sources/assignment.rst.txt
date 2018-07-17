##########
Assignment
##########

.. notes

    Started to seem long-winded.  About 15 minutes.

.. what we have to cover

   A variable as a name referring to something.
   LHS and RHS

.. code-links:: clear

Here are two assignment statements:

.. nbplot::

    >>> a = 10

.. nbplot::

    >>> p = "Matthew"

Assignment statements are very common in coding, and we'll spend some time
trying to understand them.

An assignment statement has two parts:

* The Left Hand Side (LHS) - to the left of the equals sign.  For the two
  statements above, the left hand sides are ``a`` and ``p``, respectively.
* The Right Hand Side (RHS) - to the right of the equals sign.  For the two
  statements above, the right hand sides are ``10`` and ``"Matthew"``
  respectively.

In an assignment statement, the LHS is the *name of a variable* - in this case
``a`` or ``p``.

The RHS is an *expression* - something that gives a value.  In this case the
code ``10`` is an expression returning the value 10, and the code
``"Matthew"`` returns the text *string* "Matthew".

When you learn programming, and even when you get a lot of experience, it is
useful to read to yourself what the code is doing.

In the cells above, we are *setting* a *variable* (named on the LHS) to have
a *value* (returned from the expression on the RHS).

It can be helpful to read the statement above in a verbose way to be clear
what they are doing. For example, we can read ``a = 10`` as "Make the name
``a`` refer to the number ``10``.  After this statement, we can say that
*variable* (name) ``a`` has *value* (refers to) the number ``10``.

Read ``p = "Matthew"`` as "Make the name ``p`` refer to the string "Matthew".
Variable ``p`` then has value "Matthew".

So far we have only used expressions that are simple values.  We can also use
more complicated expressions:

.. nbplot::

    >>> b = 2 + 3

Read this as "Make ``b`` refer to the result of adding 2 and 3".

The great advantage of variables, is that they can be used in expressions.
For example:

.. nbplot::

    >>> c = a

Read this as "Make ``c`` refer to the value in ``a``".

Or:

.. nbplot::

    >>> d = a + b

Read this as "Make ``d`` refer to the result of adding the value in ``a`` to
the value in ``b``".

Remember, an assignment consists of LHS ``=`` RHS, where LHS is the name of
a variable, and RHS is an expression returning a value.

If we just want to see the result of an expression, we can do this in Jupyter,
by putting the RHS expression on its own at the end of the cell.  For example,
here's the result of the expression ``15``:

.. nbplot::

    >>> 15
    15

The *expression* ``15`` returns the number 15.  Now we have set ``a`` to point
to the value 10, here is what we get with the *expression* ``a``:

.. nbplot::

    >>> a
    10

The expression ``a`` returns the value referred to by ``a``.

We can do assignments in the same cell, and follow them by a RHS expression on
its own, and we will still see the value:

.. nbplot::

    >>> d = 24 * 2
    >>> d
    48

To repeat, an assignment is a variable name on the LHS, followed by ``=``,
followed by an expression on the RHS.  Without typing this in, what do you
think you will see for these.  Explain why.

.. nbplot::

    >>> e = 3 * 10
    >>> e  #doctest: +SKIP

.. nbplot::

    >>> f = e * 3
    >>> f  #doctest: +SKIP

.. nbplot::

    >>> "g" = "Interesting"  #doctest: +SKIP

.. nbplot::

    >>> 5 = 3   #doctest: +SKIP
    >>> 5  #doctest: +SKIP
