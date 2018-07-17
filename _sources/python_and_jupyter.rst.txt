###################################
Introduction to Python, via Jupyter
###################################

.. notes

    Too long.  Need breaks for exercises.  Even then, doesn't seem motivated
    properly.  Considered not teaching this, and going straight to Pandas /
    Brexit, but that feels too rushed and magical.

    In fact needed a) lists (for data frame indexing, to get columns) and !=
    for boolean vector.

.. code-links:: clear

This is a Jupyter Notebook.

For the moment, I'll introduce the Notebook, and then get on to how Python
works.

********************
A Notebook has cells
********************

As you can see, the Jupyter Notebook runs in your web browser.

It consists of *cells*. This is a text cell.  The cell below is a code cell.

You can mix code and text cells in any order.

We won't pay much attention to text cells for now, but they are very useful to
weave explanation and code, to justify and explain your analysis.

To move from one cell to the next, you can use Shift-Enter. When you do
this inside a code cell, it will execute, and move to the next cell.

******
Python
******

What follows is a code cell.  In fact, it is Python code.  Press Shift-Enter
to move out of this cell into the code cell, and Shift-Enter again to execute
the code cell.

.. nbplot::

    >>> a = 10

Now you've executed the code cell, it doesn't look as if anything has
happened, but when you did Shift-Enter in the cell above, the Jupyter Notebook
sent the code off to be executed by `Python <https://python.org>`_.  Python is
a programming language with a easy-to-read syntax that is widely used for
teaching, and for data analysis.  It's very popular in academia, and in
industry, especially for data analysis.

.. what we have to cover

   The type of a thing
   Numbers
   Strings
   # Lists
   True and False
   Functions
   # Sum

***********************************************
Output when the last statement is an expression
***********************************************

Remember, from :doc:`assignment`, that an expression is a piece of code that
returns a value.

When working on code, we often want to see the values of expressions, and
particularly, we often want to see the contents of variables. The Notebook
makes it easy to do that.  If the last statement in a code cell is an
expression (like the Right Hand Side of an assignment), the Notebook will show
us the value returned from that expression, as *Output* from the cell.

For example, let's say we wanted to see the value of the variable ``a``.  The
code ``a`` is an expression, that returns the value of the variable ``a``.
So, to see the value of ``a`` in the Notebook, we can do this:

.. nbplot::

    >>> a
    10

Notice that the Notebook made a new type of display after the cell, with the
prompt in red, and starting with ``Out[``.

Our code cells can have lines that do some work, followed by a variable on its
own, so we can see its value. Like this:

.. nbplot::

    >>> b = 5
    >>> b
    5

****************************
The Notebook as a calculator
****************************

The code cell shows output, when it ends with an expression (a RHS without
a LHS).  The expression can be a number, or a variable, as we have seen before, but
it can also be something more complicated:

.. nbplot::

    >>> (10 + 5 + 1) / 4
    4.0

Notice, we didn't use any variables. The RHS, on its own, is ``(10 + 5 + 1) /
4`` is an expression - some code that returns a value.

This means that we can use the Notebook as a simple calculator. You've
already seen ``+`` and ``/`` and the parentheses. You also have ``*`` for
multiply, and ``-`` for subtract, and ``**`` for to-the-power-of.  For
example, here's :math:`10^4`:

.. nbplot::

    >>> 10 ** 4
    10000

Try calculating :math:`6 (2^3) / 4` (it should equal 12):

Try :math:`1024^2 / 2^{16}` (it should equal 16).

***************
Using variables
***************

The great value of variables is that we can use them in calculations. For
example, we might be interested in the result of :math:`2 x^2 + 3x + 10`. We
want to calculate what answer we get for :math:`x = 2`.

.. nbplot::

    >>> x = 2
    >>> x
    2

.. nbplot::

    >>> 2 * x ** 2 + 3 * x + 10
    24

Now we can simply get the answer for :math:`x = 7`, or any other value
of :math:`x`:

.. nbplot::

    >>> x = 7
    >>> 2 * x ** 2 + 3 * x + 10
    129

******************************
Comments begin with a hash (#)
******************************

The code cells in this Notebook, and all the Notebooks we'll use in the class,
will be in the Python programming language. In that language (and many
others), a line beginning with ``#`` is a *comment*, which means that Python
does not do anything with that line, and it just serves to explain the code.

.. nbplot::

    >>> # This is a comment.  It doesn't do anything.
    >>> # This is another comment.  It is just for your reading pleasure.
    >>> # The line below sets the variable c to have value 10.
    >>> c = 10
    >>> # The last line is an expression, and so we see an output of this expression
    >>> # after the cell.
    >>> c
    10

********************
Strings contain text
********************

So far we have only seen numbers. Another type of information that Python can
store and use, is text. Python calls text data: *strings*. For example, here I
set the variable ``my_name`` to the *string* ``'Matthew'``. Notice the quotes
around the string. The quotes tell Python that this is text (string) data:

.. nbplot::

    >>> my_name = 'Matthew'
    >>> my_name
    'Matthew'

What happens when I miss off the quotes in the line above?

You can use single quotes (``'``) to go round strings, or double quotes
(``"``). It doesn't matter to Python, it recognizes you want to make a string.

.. nbplot::

    >>> # I'm setting your_name to the string 'Alphonse' using single quotes
    >>> your_name = 'Alphonse'
    >>> your_name
    'Alphonse'

.. nbplot::

    >>> # But I could have used double quotes, it ends up the same to Python.
    >>> third_name = "Alphonse"
    >>> third_name
    'Alphonse'

************************
Functions process things
************************

Python also has *functions*. It is easiest to explain a function by example.
``len`` is a function, returning the length of something. Here we get the
length of the string:

.. nbplot::

    >>> len('Alphonse')
    8

The result that Python returned from ``len`` is the number of characters in
the string ``'Alphonse'``. The variable ``your_name`` also points to the
string ``'Alphonse'``, so we get the same result from calling ``len`` on the
variable ``your_name``:

.. nbplot::

    >>> len(your_name)
    8

The function has a name - ``len``. We call it, by using its name and then an
opening parenthesis, and then the *arguments* that we want to send to the
function, and then a closing parenthesis.

In this case the function ``len`` accepts only one argument, which is the
thing we want the length of.

Now try setting the variable ``my_name`` to a string containing your first
(given) name. Then get the Notebook to tell you how many characters there are
in your name. Here's how I would do that, in the cell below. You can edit the
cell to put your name in there instead.

.. nbplot::

    >>> my_name = 'Matthew'
    >>> len(my_name)
    7

There are functions which work on numbers as well. For example, the function
``max`` accepts two (or more) numbers, and returns the maximum:

.. nbplot::

    >>> max(10, 4)
    10

******************************
What type of thing have I got?
******************************

So far we have seen two different types of thing that a variable can refer to
- numbers and strings.

We often want to find out what type of thing a variable refers to.  We can use
the function ``type`` for this.  For example:

.. nbplot::

    >>> # Set name "a" to refer to the number 5
    >>> a = 5
    >>> # What type of thing does "a" refer to?
    >>> type(a)
    <class 'int'>

Here ``a`` refers to an integer (whole number).

.. nbplot::

    >>> # What type of thing does "my_name" refer to?
    >>> type(my_name)
    <class 'str'>

``my_name`` refers to a string.

******************************
Set equal to and test equal to
******************************

We have been setting the values of variables with the variable name (e.g.
`my_name`) followed by the equals character `=` and then the value. For
example:

.. nbplot::

    >>> # Setting variable my_name to have value "Matthew"
    >>> my_name = "Matthew"

This is the use of equal to mean "set the variable on the left equal to the
value on the right".

There is another use of "equal" which is to test whether something is equal to
something else.  This is called "test equals".  Python uses double equal signs
``==`` for that meaning of equals.  For example, here we test whether the
value of variable ``my_name`` is equal to the string `'John'`:

.. nbplot::

    >>> # Equal in the sense of test equal to
    >>> my_name == 'John'
    False

Notice that test-equal, with ``==``, is an expression, that returns the value
``True`` if the two sides are equal, and ``False`` if they are not:

.. nbplot::

    >>> # Equal in the sense of test equal to
    >>> my_name == 'Matthew'
    True

********
Packages
********

So far all the stuff we have seen uses functions that Python will always
give you. For example, ``len`` and ``max`` are always available to you,
whenever you start Python.

There are many other things that Python keeps in *modules*. Modules are
libraries of functions and other things, that you cannot use, until you
load them into Python. You load them into Python using the ``import``
command.

For example, we are soon going to be using the ``random`` module. This
is a module that gives us random numbers of various sorts. Before we can
use the ``random`` module, we have to ``import`` it - like this:

.. nbplot::

    >>> import random

What type of thing is this?

.. nbplot::

    >>> type(random)
    <class 'module'>

Now we have the random module loaded, we can access its functions, by
typing the module name ``random``, followed by a dot, followed by the
function we want to use. For example, ``random`` has a function
``randint``, that returns a number between the first argument (the low
bound) and the second argument (the high bound). We can get a random
number between 0 and 10 like this:

.. nbplot::
    :hide-from: all
    :show-to: doctest

    >>> random.seed(1939)

.. nbplot::

    >>> random.randint(0, 10)
    9

.. _getting-help:


************
Getting help
************

Often we want to know what a function does, or how many arguments it takes.
The Notebook has a useful feature to help us. Type the name of the function
you are interested in, followed by ``?`` and press Shift-Enter. The Notebook
will show you pane of help on that function.  Try it now, for ``len`` and
``max``.

.. nbplot::

    >>> # Type (e.g):
    >>> #
    >>> # len?
    >>> #
    >>> # in the cell below

It is also common that we want to know what functions or other goodies there
are in a module.  The Notebook can help with that too.  In the code cell
below, try typing `random.` (note the trailing dot) and then, without pressing
Return, press the Tab key.  The Notebook shows you a list of functions and
other things inside the ``random`` module.  This is called "Tab completion".

.. nbplot::

    >>> # Type:
    >>> #
    >>> # random.
    >>> #
    >>> # followed by Tab, in the cell below
