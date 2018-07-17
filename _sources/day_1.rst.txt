#####
Day 1
#####

*********************************
Morning - thinking about sampling
*********************************

* 10.00 - 10.15 - Are there too few Brexiteers in the survey?  How would we
  decide?
* 10.15 - 10.45 - another problem of proportions.  If a family has 4 children,
  what is the probability that the family has 3 girls?  A simulation.
* 10 minute break
* 10.55 - 11.15 - what is the algorithm?
* 11.15 - 12.00 - the machinery we will need: :doc:`print_if_for`.

**************************************
Afternoon - probability and simulation
**************************************

* back for ``for`` loops in :doc:`print_if_for`.
* lists in :doc:`lists`.
* solving with simulation; :doc:`three_girls`;

Notebooks from the afternoon:

* :download:`riffing_on_if_for_and.ipynb`;
* :download:`riffing_on_lists.ipynb`.

An explanation of ``and`` and ``or``: :doc:`and_or`.

********
Homework
********

* Download the notebook from the link at top of :doc:`three_girls` - it's a
  slightly modified solution to the three girls problem we were working on
  today.   Make a copy, that you are going to modify.
* Modify the notebook to give the probability of 2 girls, instead of 3 girls.
  What is that?
* Make another copy of the original Notebook for the next problem.  The actual
  probability of having a male child is not 0.5 but 0.513. [#male-births]_.
  To do a better simulation, we need to modify the Notebook to give a 0.513
  probability of ``"B"`` and a 0.487 probability of ``"G"``. You can't easily
  use ``random.choice`` for this, but you could an expression like this to
  decide if it is a *girl*::

    random.uniform(0, 1) <= 0.487

  ``random.uniform(0, 1)`` returns a random number between 0 and 1 - so the
  number it returns will be ``<= 0.487`` about 48.7% of the time.

  Modify your new copy of the Notebook to use something like this to give the
  probability of a girl.  You should find that your estimate of the proportion
  of 3-girl families drops slightly, because girls are slightly less common
  than boys.

.. [#male-births] `Official UK government statistics
   <https://www.gov.uk/government/statistics/gender-ratios-at-birth-in-great-britain-2010-to-2014>`_
   give the birth ratio as 105.3. This the number of boys born for every 100
   girls.

.. include:: links_names.inc
