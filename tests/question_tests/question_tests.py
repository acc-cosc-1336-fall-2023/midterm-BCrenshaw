#write function tests here, don't add input('') statements here!

# pylint: disable=C0103
# pylint: disable=C0111
# pylint: disable=C0114
# pylint: disable=C0115
# pylint: disable=C0116
# pylint: disable=C0303
# pylint: disable=C0304
# pylint: disable=E0401

import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import test_config, is_prime
from src.question_b.question_b import get_miles_per_hour
from src.question_c.question_c import use_global, create_global
from src.question_d.question_d import get_random_number, use_global_variables

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())

    def test_is_prime(self):
        self.assertEqual('False', is_prime(4))
        self.assertEqual('True', is_prime(5))
        self.assertEqual('True', is_prime(11))

    def test_get_miles_per_hour(self):
        self.assertEqual(19.883872, get_miles_per_hour(32, 60))

    def test_use_global(self):
        create_global(2)
        self.assertEqual(4, use_global(0)*2)
        self.assertEqual(6, use_global(1)*2)
        self.assertEqual(6, use_global(0)*2)

    def test_get_random_number(self):
        min_random = 1
        max_random = 5
        use_global_variables(min_random, max_random)
        self.assertEqual(True, min_random <= get_random_number() <= max_random)