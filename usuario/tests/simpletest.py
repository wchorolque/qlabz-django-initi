# -*- coding: utf-8 -*-

"""
This file demostrates writing test using the unittest model.
These will pass when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase

class SimpleTest(TestCase):

    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEquals(1 + 1, 2)

    def test_basic_addition(self):
        """
        Tests that 1 - 1 always equals 0.
        """
        self.assertEquals(1 - 1, 1)

