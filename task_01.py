#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 14 Warmup Task 1"""

import pet


class Dog(pet.Pet):
    """A class representing a dog."""

    def __init__(self, has_shots=False, **kwargs):
        """A constructor for the Dog class.
        Args:
            has_shots(bool, optional): A boolean value stating whether or not
            the dog has its shots.
            **kwargs: Arbitrary keyword arguments to be passed to the Pet class
            constructor.
        """
        self.has_shots = has_shots
        pet.Pet.__init__(self, **kwargs)
