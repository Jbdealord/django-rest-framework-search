# coding=utf-8
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import unittest
from drf_search import validators


class ValidateNumericalTests(unittest.TestCase):
    def test_validate(self):
        self.assertTrue(validators.validate_numerical(123))
        self.assertTrue(validators.validate_numerical("123"))
        self.assertFalse(validators.validate_numerical("Jazz"))

        self.assertFalse(validators.validate_numerical([123]))
        self.assertFalse(validators.validate_numerical({123}))
        self.assertFalse(validators.validate_numerical((123,)))


class ValidateBooleanTests(unittest.TestCase):
    def test_validate(self):
        # with boolean True
        self.assertTrue(validators.validate_boolean(True))
        self.assertTrue(validators.validate_boolean("True"))
        self.assertTrue(validators.validate_boolean("tRuE"))
        self.assertTrue(validators.validate_boolean(1))

        # with boolean False
        self.assertTrue(validators.validate_boolean(False))
        self.assertTrue(validators.validate_boolean("False"))
        self.assertTrue(validators.validate_boolean("fAlSe"))
        self.assertTrue(validators.validate_boolean(0))

        # things that won't work
        self.assertFalse(validators.validate_boolean(2))
        self.assertFalse(validators.validate_boolean([]))
        self.assertFalse(validators.validate_boolean("Jazz"))



class ValidateListTests(unittest.TestCase):
    def test_validate(self):
        self.assertTrue(validators.validate_list([1, 2, 3]))
        self.assertTrue(validators.validate_list("[1, 2, 3]"))

        self.assertFalse(validators.validate_list(123))
        self.assertFalse(validators.validate_list("jazz"))
        self.assertFalse(validators.validate_list({'a': 1, 'b': 2, 'c': 3}))
        self.assertFalse(validators.validate_list("{'a': 1, 'b': 2, 'c': 3}"))
