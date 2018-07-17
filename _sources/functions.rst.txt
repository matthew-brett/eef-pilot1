#########
Functions
#########

.. code-links:: clear

Have already seen functions in action, such as ``len`` and ``max``.

These are functions that Python provides for us.

We can use functions in modules. One is example is the ``random`` function
from the ``random`` module.  This returns random number between 0 and 1.

.. nbplot::

    >>> import random

.. nbplot::
    :hide-from: all
    :show-to: doctest

    >>> random.seed(1966)

.. nbplot::

    >>> random.random()
    0.88990060071...

.. nbplot::

    >>> random.random()
    0.96023181107...

We can also write our own functions.

We will use a function to contain the logic for deciding whether the next
chlild is a boy or a girl.  Call our new function ``girl_or_boy1``.  Like
``random.random`` our function ``girl_or_boy`` will accept no arguments.  It
will return a ``G`` 50% of the time and a ``B`` 50% of the time.

Remember, we have already imported ``random``.

We make a function like this:

.. nbplot::

    >>> def girl_or_boy1():
    ...     # Return 'G' or 'B' with 50% chance
    ...     return random.choice('GB')

The function starts with the word ``def`` which tells Python we are defining a
function.  Next follows the name of the function, followed by, in our case,
parentheses.  You specify what arguments the function should have, in the
parentheses. In our case, our function as no arguments, so there is nothing
between the parentheses.

Next there follows one or more indented statements.  These statements are the
*body* of the function.  They are the code that gets run when the function
gets called.

We return the result with the ``return`` statement.  Here we are returning
``"G"`` or ``"B"``, each with a 0.5 probability.

Test it:

.. nbplot::

    >>> # Notice, we pass no arguments
    >>> girl_or_boy1()
    'B'
    >>> girl_or_boy1()
    'G'

So far all we have done is moved a single line of code into a function, but
functions allow us to put more logic into the function, without making the
call any more complicated.  For example, let's imagine we wanted to write our
function to allow for the possibility that the probability of a girl was not
exactly 0.5:

.. nbplot::

    >>> def girl_or_boy2():
    ...     # Return 'G' or 'B' with (for now) 50% chance.
    ...     # Make a random number between 0 and 1
    ...     random_no = random.random()
    ...     # Calculate the return value
    ...     if random_no < 0.5:  # We might want to change this later
    ...         our_result = 'G'
    ...     else:
    ...         our_result = 'B'
    ...     # Send back the result
    ...     return our_result

Let's call the function a few times to see if the results are plausible:

.. nbplot::

    >>> girl_or_boy2()
    'G'

.. nbplot::

    >>> girl_or_boy2()
    'B'

.. nbplot::

    >>> girl_or_boy2()
    'G'

********
Exercise
********

Up until now, we've assumed that the chance that a child is a boy is 0.5.  Now
assume the proportion of boys born in the UK is 0.513 [#male-births]_.

Here's a copy of the ``girl_or_boy2`` function above, renamed as
``girl_or_boy3``.  Modify the function to return ``"B"`` (for a boy) 51.3% of
the time, and ``"G"`` (for a girl) 48.7% of the time.

.. nbplot::

    >>> def girl_or_boy3():
    ...     # Return 'G' with probability 0.487, 'B' with p=0.513.
    ...     # Make a random number between 0 and 1
    ...     random_no = random.random()
    ...     # Calculate the return value
    ...     if random_no < 0.5:  # We might want to change this later
    ...         our_result = 'G'
    ...     else:
    ...         our_result = 'B'
    ...     # Send back the result
    ...     return our_result

You can try your function out a few times with the cell below:

.. nbplot::

    >>> girl_or_boy3()
    'G'

If you've got that done, use a ``for`` loop to run this function 10000 times,
and record what proportion of times it returns ``"G"``.  Is the answer close
to 0.487?  It should be ...

.. [#male-births] `Official UK government statistics
   <https://www.gov.uk/government/statistics/gender-ratios-at-birth-in-great-britain-2010-to-2014>`_
   give the birth ratio as 105.3. This the number of boys born for every 100
   girls.
