#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests Task 02."""


# Import Python libs
import unittest


# Import user libs
import task_02


class Task02TestCase(unittest.TestCase):
    """Task 02 tests"""


    def setUp(self):
        self.fruit = {
            'Rutabaga': 14,
            'Forelle Pear': 34,
            'Raspberries': 2,
            'Red Plum': 37
        }


    def get_testval(self):
        """Returns testvalues."""
        outval = {}
        for k, v in self.fruit.iteritems():
            if k in task_02.FRUIT:
                outval[k] = task_02.FRUIT[k] * v

        return outval


    def test_get_cost_per_item(self):
        """Tests that get_cost_per_item returns the correct values."""
        retval = task_02.get_cost_per_item(self.fruit)
        self.assertEqual(retval, self.get_testval())


    def test_get_total_cost(self):
        """Tests that get_cost_per_item returns the correct values."""
        tc = sum(self.get_testval().values())
        self.assertEqual(task_02.get_total_cost(self.fruit), tc)


if __name__ == '__main__':
    unittest.main()
