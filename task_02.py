#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""use of comprehensions"""

from data import FRUIT


def get_cost_per_item(shoplist):
    """Function iterates the argumentusing key from FRUIT.
    Args:
        shoplist(dict): key is the item name found in FRUIT and its
                        value is an integer indicating the number of units to
                        purchase.
    Returns:
        a dictionary keyed by the name of fruits with total cost per_item.
    Examples:
        >>> shoplist = {'Lime': 12, 'Red Pear': 4, 'Peach': 24, 'Beet': 1}        >>> get_cost_per_item(shoplist)
        {'Lime': 7.08, 'Peach': 95.76, 'Red Pear': 9.96}
    """
    return {key: FRUIT[key] * shoplist[key] for key in shoplist.iterkeys()
            if key in FRUIT}


def get_total_cost(shoplist):
    """A function to get the total cost.
    Args:
        shoplist(dict): key is the item name found in FRUIT and
                        value is an integer indicating the number of units to
                        purchase.
    Returns:
        a number indicating the total cost.
    Examples:
        >>> shoplist = {'Lime': 12, 'Red Pear': 4, 'Peach': 24, 'Beet': 1}
        >>> get_total_cost(shoplist)
        112.80000000000001
    """
    new_list = get_cost_per_item(shoplist)
    return sum([val for val in new_list.itervalues()])
