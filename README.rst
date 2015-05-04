####################
IS 210 Assignment 14
####################
************
Warmup Tasks
************

:College: CUNY School of Professional Studies
:Course-Name: Software Application Programming I
:Course-Code: IS 210
:Points: 12
:Due-Date: YYYY-MM-DDTHH:mm:ss

Overview
========

In this assignment, you'll be introduced to a variety of advanced patterns
with functions and iterables. These tools are often encountered in a number
of advanced contexts and most have notable performance benefits, however,
for the purpose of these assignments, these tools will be introduced outside
of their more common contexts.

Instructions
============

The following tasks will either have you interacting with existing files in
the assignment repository or creating new ones on the fly. Don't forget to add
your interpreter directive, utf-8 encoding, and a short docstring with any new
files that you create!

.. important::

    In these exercises, you may, on occasion, come across a task that requres
    you to research or use a function or method not directly covered by the
    course text. Since Python is such a large language it would be impossible
    for the author to have included descriptions of each and every available
    function which would largely duplicate the offical Python documentation.

    A *vital* skill to successful programming is being comfortable searching
    for and using official language documentation sources like the
    `Python String Documentation`_ page. Throughout our coursework we will be
    practicing both the use of the language in practice and the search skills
    necessary to become functional programmers.

Warmup Tasks
============

Task 01
-------

The arbitrary arguments paradigms (eg, ``*args`` and ``**kwargs``) have many
uses but none so-common as when interfacing parent classes or component parts.
The is-a/has-a paradigm can prove problematic in that it expects both the
parent class and the child class to be continually updated each time new values
are added.

Consider the following:

.. code:: python

    class Parent(object):

        def bigSum(self, val1, val2, val3, val4):
            return val1 + val2 + val3 + val4

        
    class Child(Parent):

        constant = 50

        def bigSum(self, val1, val2, val3, val4):
            return self.constant + Parent.bigSum(val1, val2, val3, val4)

Now, think about what would have to change if ``Parent.bigSum()`` added a fifth
argument named ``val5``.

With arbitrary arguments, solving this problem becomes much simpler. Instead,
of changing all of the code, we could implement something like:

.. code:: python

    class Parent(object):

        def bigSum(self, val1, val2, val3, val4):
            return val1 + val2 + val3 + val4

        
    class Child(Parent):

        constant = 50

        def bigSum(self, *args):
            return self.constant + Parent.bigSum(self, *args)

Now, as changes are made to ``Parent.bigSum()``, they can be transparently
passed in from ``Child.bigSum()`` without the latter needing to know about the
former's direct signature.

Now, the above example is an oversimplification which does have some downsides
the most notable among them being that someone reading ``Child.bigSum()`` can
no longer tell exactly what arguments are *allowed* in the function. This is
a fairly big issue and would be considered by many to be an anti-pattern or
bad-practice. As a result, such patterns should only be considered when you
have no other choice. For example, if ``Parent()`` was an unknown class
created via some form of user input or other condition, you might not be able
to correctly state all of its arguments. In this case, it would be appropriate.

While it's not wholly uncommon to see such patterns, construction of one would
be far beyond the normal reach of this assignment. As such, you'll get a little
hands-on experience with arbitrary arguments although the pattern itself is an
unideal one.

Specifications
^^^^^^^^^^^^^^

#.  Create a module named ``task_01.py``

#.  Import the ``pet`` module which has a ``Pet`` class

#.  Create a ``Dog`` class which is subclassed from ``Pet``

#.  Create a constructor for the ``Dog`` class that has two major parameters:

    #.  ``has_shots``, (boolean, optional), Defaults to ``False``

    #.  an arbitrary arguments dictionary

#.  In the constructor, assign the ``has_shots`` parameter to an attribute,
    ``self.has_shots``.

#.  Assign the other arguments in the arbitrary arguments dictionary to the
    parent class (``Pet``) constructor via the arbitrary arguments call, eg:

    .. code:: python

        myfunc(**someargs)

.. warning::

    Tests will only be of mild use in this task since they can only detect
    whether or not the resultant class implements all of the expected
    attributes. Grading, however, will be dependent upon proper implmentation
    of arbitrary arguments.

Task 02
-------

Comprehensions are powerful tools for processing data quickly, efficiently,
and with a minimum of developer effort. Here we'll use one to go shopping!

Specifications
^^^^^^^^^^^^^^

#.  Create a file named ``task_02.py``.

#.  Copy ``data.FRUIT`` into the global namespace via
    ``from data import FRUIT``.

#.  Create a function named ``get_cost_per_item()``.
    
    #.  Takes exactly one argument: a dictionary called ``shoplist``.

        #.  The key of ``shoplist``  should be the item name as found in
            ``FRUIT``

        #.  The value of ``shoplist`` should be an integer indicating the
            number of units to purchase.

    #.  In one line, use a *dictionary comprehension* to:

        #.  Iterate over the ``shoplist``

        #.  Filter results for ``shoplist`` to only return keys found in
            ``FRUIT``

        #.  Multiply the number of units from ``shoplist`` by the price of
            the units found in ``FRUIT``. (These are the respective
            values of each dictionary).

        #.  Return a new dictionary keyed by the name of the fruit with the
            total cost per-item reflected.

#.  Create a function named ``get_total_cost()``.

    #.  Takes exactly one argument: a dictionary called ``shoplist``.

        #.  The key of ``shoplist``  should be the item name as found in
            ``FRUIT``

        #.  The value of ``shoplist`` should be an integer indicating the
            number of units to purchase.

    #.  In a single-line:

        #.  Uses ``get_cost_per_item()`` to retrieve the per-item costs.

        #.  Sums the values of the resultant dictionary together.

            .. tip::

                Check out the ``sum()`` function to help with this. There's
                also a helpful dictionary built-in function you might want to
                use.

        #.  Returns the total cost.

Examples
^^^^^^^^

.. code:: pycon

    >>> print shoplist
    {'Lime': 12, 'Red Pear': 4, 'Peach': 24, 'Beet': 1}
    >>> get_cost_per_item({'Lime': 12, 'Red Pear': 4, 'Peach': 24, 'Beet': 1})
    {'Lime': 7.08, 'Peach': 95.76, 'Red Pear': 9.96}
    >>> get_total_cost({'Lime': 12, 'Red Pear': 4, 'Peach': 24, 'Beet': 1})
    112.80000000000001

Executing Tests
===============

Code must be functional and pass tests before it will be eligible for credit.

Linting
-------

Lint tests check your code for syntactic or stylistic errors To execute lint
tests against a specific file, simply open a terminal in the same directory as
your code repository and type:

.. code:: console

    $ pylint filename.py

Where ``filename.py`` is the name of the file you wish to lint test.

Unit Tests
----------

Unit tests check that your code performs the tested objectives. Unit tests
may be executed individually by opening a terminal in the same directory as
your code repository and typing:

.. code:: console

    $ nosetests tests/name_of_test.py

Where ``name_of_test.py`` is the name of the testfile found in the ``tests``
directory of your source code.

Running All Tests
-----------------

All tests may be run simultaneously by executing the ``runtests.sh`` script
from the root of your assignment repository. To execute all tests, open a
terminal in the same directory as your code repository and type:

.. code:: console

    $ bash runtests.sh

Submission
==========

Code should be submitted to `GitHub`_ by means of opening a pull request.

As-of Lesson 02, each student will have a branch named after his or her
`GitHub`_ username. Pull requests should be made against the branch that
matches your `GitHub`_ username. Pull requests made against other branches will
be closed.  This work flow mimics the steps you took to open a pull request
against the ``pull`` branch in Week Two.

For a refresher on how to open a pull request, please see homework instructions
in Lesson 01. It is recommended that you run PyLint locally after each file
is edited in order to reduce the number of errors found in testing.

In order to receive full credit you must complete the assignment as-instructed
and without any violations (reported in the build status). There will be
automated tests for this assignment to provide early feedback on program code.

When you have completed this assignment, please post the link to your
pull request in the body of the assignment on Blackboard in order to receive
credit.

.. _GitHub: https://github.com/
.. _Python String Documentation: https://docs.python.org/2/library/stdtypes.html
