#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""the arbitary arguments paradigm"""

import pet


class Dog(pet.Pet):
    """a subclass constructure"""
    def __init__(self, has_shots=False, **kwargs):
        """Constructor for the subclass.
        Args:
            has_shots(bool, optional): Defaults to False
            kwargs: an arbitrary arg dictionary.
        Attributes:
            has_shots(bool): defaults to False.
        """
        self.has_shots = has_shots
        pet.Pet.__init__(self, **kwargs)
