###########
While loops
###########

The ``while`` loop is rather like the ``for`` loop (see: :doc:`print_if_for`).

Here is a simple ``while`` loop where I add up all the numbers between 1 and
21 inclusive:

.. nbplot::

    >>> # We use a variable to keep track of the total
    >>> total = 0
    >>> # We use a variable to keep track of what number we're on
    >>> current_number = 0
    >>> while current_number < 22:
    ...     total = total + current_number
    ...     current_number = current_number + 1
    ...
    >>> print(total)
    231

The ``while`` loop, like the ``if`` statement, tests a condition, here
``current_number < 22``.  Like the ``if`` statement, there are indented
statements after the condition test, that only run if the condition test is
True.  The difference is that a while loop keeps running the indented
statements until the condition is True.  So, the first time through, when
``current_number`` is set to 0, the condition will be True (0 is less than
22), and the body of the while loop executes.  But, when the while loop
finishes running ``current_number = current_number + 1`` at the end of the
block, it goes back and checks the conditional again.  Now ``current_number``
is 1, but this is still less than 22, and so we proceed to run ``total =
total + current_number`` and the rest of the statements in the body.  We do
this until the condition is False, and then the while loop stops and the
program continues after the end of the while loop.

Exercises:

* Use a version of the while loop above to add up all the numbers between 10
  and 21, inclusive.
* Use a version of the while loop above to add up all the even numbers between
  0 and 20, inclusive.
* Make an empty list, and use a while loop to go through all the numbers
  between 5 and 30, inclusive, appending them to the list.
