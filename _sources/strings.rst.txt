#######################################
Strings, functions, and types of things
#######################################

So far (in :doc:`assignment`) our expressions have all used numbers.

.. nbplot::

    >>> a = 10
    >>> a
    10

We read this as "``a`` gets the value 10".

*******
Strings
*******

There are other types of values.  One very common type of value is a string.
A string contains text, instead of numbers.

.. nbplot::

    >>> my_name = "Matthew"
    >>> my_name
    'Matthew'

Notice the quotes around `"Matthew"`.  The quotes tell Python that I mean to
define a string here.  What would happen if I missed off the quotes?

.. nbplot::

    >>> my_name = Matthew  # doctest: +SKIP

Remember your debugging Fu (that's like Kung Fu, but for debugging).   Look at
the message.  See if you can understand what it means.  Python does not think
that ``Matthew`` is a string, but what does Python think that it is.

Let's define another string:

.. nbplot::

    >>> your_name = "Yogi"
    >>> your_name
    'Yogi'

What do you think would happen if I did this?

.. nbplot::

    >>> both_names = my_name + your_name

*********
Functions
*********

Here we use a *function* for the first time.  The function is called ``len``.
What do you think it does?

.. nbplot::

    >>> how_long = len(my_name)
    >>> how_long
    7

A function is something that we can *call*.  We *call* a function, by giving
the function name - here ``len`` - followed by open parenthesis - ``(`` -
followed by the *function arguments* - here ``my_name`` - followed by close
parenthesis ``)``.  The function may return calculated and return a value. In
this case ``len(my_name)`` returns the number of characters in the string.

.. warning::

    Python is super fussy about its brackets.  ``(`` and ``)`` (parentheses)
    are not at all the same thing as ``[`` and ``]`` (*square brackets*) or
    ``{`` and ``}`` (*curly brackets*).  Try using square brackets and curly
    brackets in the expression above.  Does it work?

Here's another function you will see a lot - ``print``.  It has the same
pattern - the function name ``print`` followed by ``(`` followed by the
arguments (the things to print), followed by ``)``.

.. nbplot::

    >>> print(my_name)
    Matthew

.. nbplot::

    >>> print(10)
    10

********
Exercise
********

Get into pairs.  Allocate the driver and the navigator.  Get a piece of paper
and a pen or pencil, and put it next to you.

Make a variable ``driver_name`` that has the value of the driver's name, (as a
string).

Make a variable ``navigator_name`` that has the value of the driver's name, (as a
string).

Make a variable ``team_name`` that has the value of the concatenation of the
driver's name and the navigators name.

Make a variable ``team_len`` that is the length of ``team_name``.

Use ``print`` to print ``team_len`` and ``team_name``.

See if you can work out how to make a variable ``nicer_team_name`` that is the
driver's name followed by a space, followed by the navigator's name.
