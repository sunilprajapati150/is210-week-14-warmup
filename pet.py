#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Provides the Pet class."""

import datetime


class Pet(object):
    """A class that represents a generic Pet."""

    def __init__(self, birthyear, weight, length, color, owner=None):
        """Constructor for the Pet class.

        Args:
            birthyear (int): Year the pet was born.
            weight (int): Weight of the pet in kg.
            length (int): Length of the pet in cm.
            color (str): Color of the pet.
            owner (str, optional): Name of the pet's owner, defaults to None.

        Attributes:
            age: (int): Age of the pet in years.
            birthyear (int): Year the pet was born.
            weight (int): Weight of the pet in kg.
            length (int): Length of the pet in cm.
            color (str): Color of the pet.
            owner (str, optional): Name of the pet's owner, defaults to None.
        """
        self.age = datetime.datetime.now().year - birthyear
        self.birthyear = birthyear
        self.weight = weight
        self.length = length
        self.color = color
        self.owner = owner
