#####
Lists
#####

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

Exercises:

Use a ``for`` loop to make a list of all the numbers between 0 and 10.

Use a ``for`` loop to make a list of all the numbers from 0 through 99 that
are divisible by 3 and by 4.

Use a ``for`` loop and the `randint` function from the ``random`` module to
make 100 random integers in the range 0 through 10.  Count how many zeros you
got.
