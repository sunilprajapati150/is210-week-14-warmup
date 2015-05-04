#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests Task 01."""


# Import Python libs
import unittest


# Import user libs
import task_01


class Task01TestCase(unittest.TestCase):
    """Task 01 tests"""

    def test_dog_properties(self):
        """Tests that the Dog class has all appropriate attributes."""
        attrs = {'birthyear': 2014,
                 'weight': 18,
                 'length': 17,
                 'color': 'brindle',
                 'has_shots': True}

        my_dog = task_01.Dog(**attrs)
        for attr_name, attr_val in attrs.iteritems():
            self.assertEqual(getattr(my_dog, attr_name), attr_val)


if __name__ == '__main__':
    unittest.main()
