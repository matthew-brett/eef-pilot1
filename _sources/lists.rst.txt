#####
Lists
#####

..  The datacamp tutorial assumes you know list indexing. Also covers
    adding lists, and multiplying them by a scalar.  Also list slicing.

.. code-links:: clear

We have seen numbers and strings as types.

.. nbplot::

    >>> a = 10
    >>> type(a)
    <class 'int'>

.. nbplot::

    >>> b = 1.0
    >>> type(b)
    <class 'float'>

.. nbplot::

    >>> my_name = "Matthew"
    >>> type(my_name)
    <class 'str'>

Another useful type, is the ``list``.  Here we make an empty list:

.. nbplot::

    >>> my_list = []
    >>> type(my_list)
    <class 'list'>

We can also put elements into the list:

.. nbplot::

    >>> my_list = [2, 4, 6]
    >>> my_list
    [2, 4, 6]

What do you think you will get from ``len(my_list)``?

Like other Python object, lists have *methods*.  Methods are functions,
attached to the object, that operate on the object.  You can get to the
methods with the variable name (e.g. ``my_list``) followed by a dot ``.``,
followed by the method name.  One useful method for a list is ``append``.  It
works like this:

.. nbplot::

    >>> another_list = []
    >>> another_list
    []
    >>> another_list.append(3)
    >>> another_list
    [3]
    >>> another_list.append(5)
    >>> another_list
    [3, 5]

Another useful method is ``count``.  It counts the number of times a
particular element occurs in the list.

.. nbplot::

    >>> another_list.count(3)
    1
    >>> another_list.append(3)
    >>> another_list.count(3)
    2
    >>> another_list.count(99)
    0

#########
Exercises
#########

Make a list with all the odd numbers from 1 through 9 (just type it in for
now).  It should look this this when you print it::

    [1, 3, 5, 7, 9]

Print out the number of elements there are in this list.

Print out the number of 7s in the list.

Append the value 7 to this list.  It should print out as::

    [1, 3, 5, 7, 9, 7]

Print out the number of 7s again.

Append another 7.  Print out the number of 7s.
