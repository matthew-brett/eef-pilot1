#######
My mean
#######

In case you get stuck, here's a version of ``my_mean`` that should work:

.. nbplot::

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
