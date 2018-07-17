#############
Slicing lists
#############

.. code-links:: clear

Sometimes, we want to split up lists, or get elements from lists.

We can do this with list slicing.

.. nbplot::

    >>> my_list = [5, 1, 3, 2, 7, 10]
    >>> my_list
    [5, 1, 3, 2, 7, 10]

How do I get the first element in the list?

.. nbplot::

    >>> # The first element of the list
    >>> my_list[0]
    5

The number 0 in ``my_list[0]``, is the list *index*.  The *index* give the
position of the element we want.  The *index* of the first element is 0, the
index of the second element is 1, and so on.

Get the third element.

Get the last element.

Let's say I only want the first 3 numbers from this list.  I can do this with
list slicing:

.. nbplot::

    >>> # Get the first 3 elements
    >>> first_3 = my_list[:3]
    >>> first_3
    [5, 1, 3]

Read the colon ``:`` as "everything up to (but not including)". So, you can
read the slice expression ``my_list[:3]`` as "get all the elements from
``my_list`` up to, but not including, the element at position 3".  You can
also read this as "get the first 3 elements.

Let's say I did not want to start at the first element.  I can do this by
putting the position that I want to start at, before the colon.  For example,
here I get the elements at indices 2 and 3 (the third and fourth elements):

.. nbplot::

    >>> # Get the third and fourth elements
    >>> third_fourth = my_list[2:4]
    >>> third_fourth
    [3, 2]

Get the second, third and fourth elements.

If we don't specify the index after the colon, it means "all the way to the
end".  So, say I wanted all the elements from position 3 (fourth element), I
could do this:

.. nbplot::

    >>> # Get all the elements from position 3 (fourth element)
    >>> my_list[3:]
    [2, 7, 10]

If you find the indices confusing (0 is first, 1 is second), you're not alone.
It takes time to get used to that.  Although it can be confusing, I think
you'll find, over time, it starts to make sense.

But - for now - if you only remember one thing about this, here is the way to
split the list into the first 3 elements, and everything after:

.. nbplot::

    >>> # First 3 - colon followed by 3
    >>> first_3 = my_list[:3]
    >>> # Everything after - 3 followed by colon
    >>> everything_after = my_list[3:]
    >>> first_3
    [5, 1, 3]
    >>> everything_after
    [2, 7, 10]
