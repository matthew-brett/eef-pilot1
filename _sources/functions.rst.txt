#########
Functions
#########

.. code-links:: clear

.. notes

    Need something on why functions are useful (moving common operations so
    they can be re-used without retyping) (testing).

    Standard deviation function is too long.  Needs to be simplified to

    mu = my_mean(some_values)
    sum_of_squares = 0
    for value in some_values:
        deviation = value - mu
        sq_deviation = deviation ** 2
        sum_of_squares = sum_of_squares + sq_deviation
    variance = sum_of_squares / len(some_values)
    return math.sqrt(variance)

Have already seen functions in action, such as ``len`` and ``print``.

Here's ``len`` in action:

.. nbplot::

    >>> my_name = "Matthew"
    >>> len(my_name)
    7

Remember, functions have a name - ``len``.  We call them by using the name,
followed by open parenthesis - ``(``, followed by zero or more arguments,
followed by close parenthesis - ``)``.

``len`` takes only one argument.  Try the code below - what happens?

.. nbplot::

    >>> your_name = "Yogi"
    >>> len(my_name, your_name)  # doctest: +SKIP

You can see that ``len`` returns a value.  The value is the length of the
argument.  For strings, that is the number of characters in the string.

Some functions take more than one argument.  ``print`` is an example.  We can
send ``print`` one argument, like this:

.. nbplot::

    >>> print(my_name)
    Matthew

We can send more than one argument to ``print`` by separating the arguments
with a comma - ``,``:

.. nbplot::

    >>> print(my_name, your_name)
    Matthew Yogi

These are functions that Python provides for us.

*******************
Write-your-own mean
*******************

Now we are going to write our own function.  This function will take one
argument - a list - and return the mean of the values in the list.

Remember the mean is the sum of all the values, divided by the number of
values.

To build our function, let's start with a small list, and work out what the
mean should be.  Copy this into a new cell in a Notebook.  Remember, lines
beginning with ``#`` ("hash") are comments - Python will ignore them, they are
for our benefit, to remind ourselves what we are trying to do.

.. nbplot::

    >>> # An example list
    >>> a_list = [2, -1, 6, 9, 5, 3]
    >>> # The sum of all the elements
    >>> summed = 2 + -1 + 6 + 9 + 5 + 3
    >> # The number of elements
    >>> n = len(a_list)
    >>> # Mean is the sum divided by the number of elements
    >>> a_list_mean = summed / n
    >>> a_list_mean
    4.0

Here our list is small, and it isn't too bad to type out all the elements with
plus signs between them, to get the sum.   We don't want to have to do that
all the time, especially with a long list.  Our first task is to work out how
to sum up all the elements of the list.  Time for a ``for`` loop.

Exercise
========

Write a ``for`` loop that sums up all the elements in ``a_list``.  Start like
this:

.. nbplot::

    >>> total = 0
    >>> # Use a for loop to go through each element ``a_list``
    >>> # Add each element to the total
    ...
    >>> print(total)

Now finish up your calculation of the mean by dividing ``total`` by the number
of elements in ``a_list``.  It should equal the answer above.  You've
calculated the mean!  Now it is time to put this into a function.

If you've done the exercise, make a new list, that is the elements of the old
list, with the mean subtracted from each element. Call this new list
``deviations``. Sum all the elements in the ``deviations`` list.  Can you see
why the sum must be the value you got, by doing a little algebra?

***************************
Back to write your-own-mean
***************************

Now we have the code to calculate the mean from a list of values, it's time to
make our own function.  The first job is to make a template, for our function,
that just prints out its arguments.  Try this in your Notebooks:

.. nbplot::

    >>> def my_mean(some_values):
    ...     # We plan to return the mean of the values in list "values"
    ...     print("Running inside my_mean function")
    ...     print(some_values)
    ...     # For now, just return 0
    ...     return 0

The function starts with the word ``def`` which tells Python we are defining a
function.  Next follows the name of the function -- ``my_mean``, followed by,
open parenthesis - ``(``.  You specify what arguments the function should
have, in the parentheses. In our case, our function as one argument, so there
is one value between the parentheses. Last we have close parenthesis - ``)``,
and our familiar colon at the end of the line, introducting an indented
*block*.

Next there follows a series of statements that are indented.  These statements
are the *body* of the function.  They are the code that gets run when the
function gets called.

We return the result with the ``return`` statement.  For the moment we return
a 0, but we hope to fix that soon.

Try calling the function, like this:

.. nbplot::

    >>> result = my_mean(a_list)
    Running inside my_mean function
    [2, -1, 6, 9, 5, 3]
    >>> result
    0

Try passing another list:

.. nbplot::

    >>> another_list = [3, 2, 1, 0]
    >>> result = my_mean(another_list)
    Running inside my_mean function
    [3, 2, 1, 0]

The output gives you an idea of what is happening.  When we run
``mean(a_list)``, Python gets the value from ``a_list``, and sets the name
``some_values`` to point to that value (the list).  Then it runs the indented
function block.  Finally, with the ``return`` statement, it returns the value
0.

Exercise
========

It is time to write our function calculating the mean.

Here's a template for you to copy into a Notebook.

.. nbplot::

    >>> def my_mean(some_values):
    ...     # We actually return the mean of the values in list "values"
    ...     # You may like to remove these prints later
    ...     print("Running inside my_mean function")
    ...     print(some_values)
    ...     total = 0
    ...     # Use a for loop to go through each element in ``some_values``
    ...     # Add each element to the total
    ...     # When that is done, then return total divided by number of
    ...     # elements
    ...     return total / len(some_values)

.. nbplot::
    :hide-from: all
    :show-to: doctest

    >>> def my_mean(some_values):
    ...     # We actually return the mean of the values in list "values"
    ...     # You may like to remove these prints later
    ...     total = 0
    ...     # Use a for loop to go through each element in ``some_values``
    ...     for value in some_values:
    ...         # Add each element to the total
    ...         total = total + value
    ...     # When that is done, then return total divided by number of
    ...     # elements
    ...     return total / len(some_values)

We will soon get used to testing everything we do.  Let's start by making a
test cell.  First run the ``my_mean`` cell above, to define the function.
Then run this test cell to test that it works for values we know.  As you fix
up ``my_mean``, run the ``my_mean`` cell, then run the test cell again, to check.

.. nbplot::

    >>> # Test cell for my_mean.
    >>> a_list = [2, -1, 6, 9, 5, 3]
    >>> result = my_mean(a_list)
    >>> if result == 4:
    ...     print("Yes! Nice job")
    ... else:
    ...     print("Oops, expected 4.0 but got", result)
    Yes! Nice job

If you've finished that, look around to see if you can find a library that has
a function to calculates the mean (Google for "Python mean"). Make a new test
function with several lists, testing that each of the lists gets the same mean
from ``my_mean`` as the other mean function you found. Think of a way of
generating a large number of different lists to test.

******************
Standard deviation
******************

Do you remember how to calculate standard deviation?

Just to confuse you, there are slightly different standard deviation
calculations, sometimes called the population standard deviation and the
sample standard deviation. Here we are calculating the population standard
deviation.

To keep ourselves honest, let's get someone else's standard deviation
calculation.  Here I am importing a library called ``numpy``.

.. nbplot::

    >>> import numpy
    >>> type(numpy)
    <class 'module'>

.. nplot::

    >>> # This is numpy's calculation of standard deviation
    >>> np.std(a_list)
    3.162277660168379...

Next we do the calculation ourselves.

Make sure you have defined a working version of ``my_mean``.  If you got
stuck, try the version in :doc:`my_mean`.

First we calculate the *deviation* of each value from the mean:

.. nbplot::

    >>> # First calculate the mean
    >>> # Make sure you've got my_mean fixed up
    >>> mu = my_mean(a_list)
    >>> mu
    4.0

Subtract the mean from each value, to get the deviations.

.. nbplot::

    >>> deviations = []
    >>> for element in a_list:
    ...     deviation = element - mu
    ...     deviations.append(deviation)
    ...
    >>> deviations
    [-2.0, -5.0, 2.0, 5.0, 1.0, -1.0]

Next we calculate the squared deviations:

.. nbplot::

    >>> sq_deviations = []
    >>> for element in deviations:
    ...     sq_deviation = element ** 2
    ...     sq_deviations.append(sq_deviation)
    ...
    >>> sq_deviations
    [4.0, 25.0, 4.0, 25.0, 1.0, 1.0]

The average of these squared deviations, is called the *variance*.  More
specifically, it is called the *population variance*.

.. nbplot::

    >>> variance = my_mean(sq_deviations)
    >>> variance
    10.0

Let's check that we get the same answer as ``numpy`` for that:

.. nbplot::

    >>> numpy.var(a_list)
    10.0

Finally, the standard deviation is the square root of the variance.  We need a
square root function, which we will get from the ``math`` module:

.. nbplot::

    >>> import math
    >>> type(math)
    <class 'module'>

.. nbplot::

    >>> math.sqrt(variance)
    3.162277660168379...

This is the same as:

.. nbplot::

    >>> numpy.std(a_list)
    3.162277660168379...

Putting that all together:

.. nbplot::

    >>> # First calculate the mean
    >>> mu = my_mean(a_list)
    >>> # Subtract mean from each value, to get the deviations.
    >>> deviations = []
    >>> for value in a_list:
    ...     deviation = value - mu
    ...     deviations.append(deviation)
    >>> # Calculate the squared deviations:
    >>> sq_deviations = []
    >>> for value in deviations:
    ...     sq_deviation = value ** 2
    ...     sq_deviations.append(sq_deviation)
    >>> # Population variance is mean of square deviations
    >>> variance = my_mean(sq_deviations)
    >>> # Standard deviation is square root of variance
    >>> sd = math.sqrt(variance)
    >>> sd
    3.162277660168379...

********
Exercise
********

Here is a template function to return the standard deviation.

Take the contents of the cell above, and put it into the function, renaming
``a_list`` to ``some_values``, where you need to, and fixing the indentation.

I've started that off for you with ``mu = my_mean(some_values)``.

.. nbplot::

    >>> # You need the math library for sqrt
    >>> import math
    >>>
    >>> def my_std(some_values):
    ...     # We plan to return standard deviation of values in list "values"
    ...     print("Running inside my_std function")
    ...     print(some_values)
    ...     # First calculate the mean
    ...     mu = my_mean(some_values)
    ...     # Put the rest of the standard deviation cell here.
    ...     # Return 0 - but you should return the standard deviation
    ...     return 0

.. nbplot::
    :hide-from: all
    :show-to: doctest

    >>> def my_std(some_values):
    ...     # Standard deviation of values in list "values"
    ...     sum_sq_dev = 0
    ...     # First calculate the mean
    ...     mu = my_mean(some_values)
    ...     for value in some_values:
    ...         sq_dev = value - mu) ** 2
    ...         sum_sq_dev = sum_sq_dev + sq_dev
    ...     variance = sum_sq_dev / len(some_values)
    ...     return math.sqrt(variance)

Here is a test cell. Keep running your ``my_std`` cell and the test cell until
you see ``Crushed it``.

.. nbplot::

    >>> import numpy
    >>> result = my_std(a_list)
    >>> if result == numpy.std(a_list):
    ...     print("Crushed it")
    ... else:
    ...     print("Expected", numpy.std(a_list), "got", result)
    Crushed it

For extra points, see if you can reduce the two ``for`` loops to one ``for``
loop in the ``my_std`` function.  Hint: add up the total of the squared
deviations in the loop.

Next try creating a function for the *sample* standard deviation.  Copy your
``my_std`` function above, and rename it as ``my_sample_std``.

Thus far, we have calculated the *population* standard deviation, where the
*population* variance is the sum of the squared deviations, divided by $N$.
$N$ is the number of elements. Therefore, the population variance is the
mean of the squared deviations.

The *sample* variance is the sum of the squared deviations, divided by $N−1$.
The sample standard deviation is the square root of the sample variance.

The function ``stdev`` from the ``statistics`` module calculates the sample
standard deviation. Test against that.
