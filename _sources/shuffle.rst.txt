#######
Shuffle
#######

.. requires
    slice-list

.. code-links:: clear

Sometimes we want to take the elements in a list, and put them into a random
order.

Luckily, Python thought of that for us.

.. nbplot::

    >>> import random

.. nbplot::
    :hide-from: all
    :show-to: doctest

    >>> random.seed(1966)

.. nbplot::

    >>> my_list = [5, 1, 3, 2, 7]
    >>> my_list
    [5, 1, 3, 2, 7]

Now we shuffle the elements to a random order:

.. nbplot::

    >>> random.shuffle(my_list)
    >>> my_list
    [1, 7, 3, 2, 5]
    >>> random.shuffle(my_list)
    >>> my_list
    [2, 5, 3, 1, 7]
    >>> random.shuffle(my_list)
    >>> my_list
    [7, 3, 2, 5, 1]

********
Exercise
********

Here's a cell that makes a list with the names of all the cards in a standard
52 card pack.  Run it to get a not-shuffled pack of cards.

.. nbplot::

    >>> suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    >>> values = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
    ...           'Jack', 'Queen', 'King', 'Ace']
    >>> deck = []
    >>> for suit in suits:
    ...     for value in values:
    ...         card = value + ' of ' + suit
    ...         deck.append(card)
    ...
    >>> # Show the first 15 cards in the deck
    >>> deck[:15]
    ['2 of Hearts',
     '3 of Hearts',
     '4 of Hearts',
     '5 of Hearts',
     '6 of Hearts',
     '7 of Hearts',
     '8 of Hearts',
     '9 of Hearts',
     '10 of Hearts',
     'Jack of Hearts',
     'Queen of Hearts',
     'King of Hearts',
     'Ace of Hearts',
     '2 of Diamonds',
     '3 of Diamonds']

Shuffle the deck with ``random.shuffle``.

Use a ``for`` loop to shuffle the cards 10000 times.   Your loop might start
like this:

.. nbplot::
    :hide-from: doctest

    >>> count = 0
    >>> for i in range(10000):
    ...     # do something

Count how many times the ``"Ace of Spades"`` is the first card, after
shuffling.   What proportion is that?  Is that what you were expecting?  What
is the exact answer, using probability?

Again use a ``for`` loop again to shuffle the cards 10000 times.  Count how
many times the ``"Ace of Spades"`` is either the first card or the second
card.   What proportion is that?  Can you calculate what the exact answer is,
using probability?
