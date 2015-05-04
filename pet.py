#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Provides the Pet class."""

import datetime


class Pet(object):
    """A class that represents a generic Pet."""

    def __init__(self, birthyear, weight, length, color, owner=None):
        """Constructor for the Pet class."""

        self.age = datetime.datetime.now().year - birthyear
        self.birthyear = birthyear
        self.weight = weight
        self.length = length
        self.color = color
        self.owner = owner
