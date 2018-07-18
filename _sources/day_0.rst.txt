#####
Day 0
#####

To start:

* Get a study number from me;
* Fill out `this form <https://goo.gl/forms/jDwL5DFZEJAmim8D2>`_;
* Get a consent form from me, ask any questions, sign it.
* Check your setup, by making a new Notebook:

    * Windows, with Anaconda - open Anaconda Prompt.  Type ``jupyter
      notebook``.
    * Mac, with Anaconda - open Terminal.app (maybe from Spotlight).  Type
      ``jupyter notebook``.

  Any problems, ask for help.

********************************
What is data science.  Why? How?
********************************

The problem

* introduction to the course - :download:`talk slides
  <intro_talk_slides.pdf>` [#get-source]_.
* :doc:`the Brexit problem <brexit_problem>`.
* Three girls.  A simulation.
* The algorithm.
* On debugging.
* :doc:`assignment`.
* :doc:`strings`.

.. curriculum

    assignment is giving a name to a value
    variable names
    values and expressions "n gets the value 7"
    assignment exercises
    reassigning a variable
    updating a variable
    strings
    lists

.. quotes

    A statement is an instruction that the Python interpreter can execute. We
    have only seen the assignment statement so far. Some other kinds of
    statements that we’ll see shortly are while statements, for statements, if
    statements, and import statements. (There are other kinds too!)

    An expression is a combination of values, variables, operators, and calls to
    functions. Expressions need to be evaluated. If you ask Python to print an
    expression, the interpreter evaluates the expression and displays the result.

    The evaluation of an expression produces a value.

.. steps

    family = []
    family.append(random.choice(['G', 'B']))
    family.append(random.choice(['G', 'B']))
    family.append(random.choice(['G', 'B']))
    family.append(random.choice(['G', 'B']))
    family

.. [#get-source] Source files for building the slides, and source for all the
   pages in this website are always available in the `course Github
   repository`_.

.. include:: links_names.inc
