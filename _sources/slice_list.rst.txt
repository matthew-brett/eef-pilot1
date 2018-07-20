##################
Working with lists
##################

.. code-links:: clear

##############
Indexing lists
##############

Sometimes, we want to split up lists, or get elements from lists.

We can do this with list slicing.

.. nbplot::

    >>> my_list = [5, 1, 3, 2, 7, 10]
    >>> my_list
    [5, 1, 3, 2, 7, 10]

The elements have *positions* in the list.  These positions are also called
*indices*?

In Python, as for many other languages, the first *position* or *index*, is 0.

How do I get the first element in the list?

.. nbplot::

    >>> # The first element of the list
    >>> my_list[0]
    5

The number 0 in ``my_list[0]``, is the list *position* or *index*.
The index of the first element is 0, the index of the second element is 1, and
so on:

.. nbplot::

    >>> my_list = [5, 1, 3, 2, 7, 10]
    >>> print("The list is", my_list)
    >>> list_length = len(my_list)
    >>> print("The length of the list is", list_length)
    >>> for i in range(list_length):
    ...     print("The value at index", i, "is", my_list[i])
    ...
    The list is [5, 1, 3, 2, 7, 10]
    The length of the list is 6
    The value at index 0 is 5
    The value at index 1 is 1
    The value at index 2 is 3
    The value at index 3 is 2
    The value at index 4 is 7
    The value at index 5 is 10

Exercise
========

Get the third element (element at position 2).

Get the last element.

Add the first element to the last element.

************************
Taking slices from lists
************************

Let's say I only want the first 3 numbers from this list.  I can do this with
list slicing:

.. nbplot::

    >>> # Get the elements at positions up to, but not including 3
    >>> first_3 = my_list[:3]
    >>> first_3
    [5, 1, 3]

Read the colon ``:`` as "everything up to (but not including)". So, you can
read the slice expression ``my_list[:3]`` as "get all the elements from
``my_list`` up to, but not including, the element at position 3".  You can
also read this as "get the first 3 elements".

Let's say I did not want to start at the first element.  I can do this by
putting the position that I want to start at, before the colon.  For example,
here I get the elements at indices 2 and 3 (the third and fourth elements):

.. nbplot::

    >>> # Get the third and fourth elements
    >>> third_fourth = my_list[2:4]
    >>> third_fourth
    [3, 2]

Read as "all the elements starting at position 2, up to, but not including,
the element at position 4".

I can also miss off the value after the colon.  In that case, Python concludes
you want all the elements, up to the end.

.. nbplot::

    >>> # Get all the elements from the third, to the end.
    >>> third_to_end = my_list[2:]
    >>> third_to_end
    [3, 2, 7, 10]


If you find the indices confusing (0 is first, 1 is second), you're not alone.
It takes time to get used to that.  Although it can be confusing, I think
you'll find, over time, it starts to make sense.

****************
Splitting a list
****************

We often want to split a list into a two parts.  List slicing does that
nicely.  Here we split a list into the two.  The first list contains the first
3 elements, and second contains everything after that.

.. nbplot::

    >>> # First 3 - colon followed by 3
    >>> first_3 = my_list[:3]
    >>> # Everything after - 3 followed by colon
    >>> everything_after = my_list[3:]
    >>> first_3
    [5, 1, 3]
    >>> everything_after
    [2, 7, 10]

********
Exercise
********

Here's a list of all the numbers from 100 to 120, inclusive:

.. nbplot::

    >>> hundred_plus = list(range(100, 121))

Split this list into two, the first containing the first 5 elements, and the
second containing elements from position 5 to the end.

Use ``sum`` (:doc:`sum`) or a ``for`` loop to calculate the sum of these two
lists.

Show that the sum of these two sums is equal to the sum of the whole
``hundred_plus`` list.

Split the list into three lists, each of 10 elements:

* the first 10 elements;
* elements from position 10 up to, but not including position 20;
* the remainder.

Show the sums of each of these three lists.

List slicing can also use step sizes, as in ``my_list[2:10:3]`` (where ``3``
is the step size).  Try using step sizes to take the sum of every second
element, starting at the element at position 5, up to, but not including, the
element at position 15.  I think that should be 545.  You can also omit the
second (end position) number.  Do that to calculate the sum of every fourth
element starting at position 3, to the end.   I think that's 555.
