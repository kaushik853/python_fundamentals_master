'''
Demonstrate your knowledge of unittest by first creating a function with input parameters and a return value.

Once you have a function, write at least two tests for the function that use various assertions. The
test should pass.

Also include a test that does not pass.

'''
import unittest

def sum_two(a, b):
    """ sum of two numbers """
    return a + b

def is_prime(number):
    """Return True if *number* is prime."""
    if number <= 1:
        return False
    for element in range(2, number):
        if number % element == 0:
            return False
    return True

class Mytest_case(unittest.TestCase):

    def test_sum_two(self):
        self.assertEqual(sum_two(3, 5), 8)
    def test_fail_sum_two(self):
        self.assertEqual(sum_two(4, z), 9)
    def test_is_prime(self):
        self.assertTrue(is_prime(5))
    def test_no_is_prime(self):
        self.assertTrue(is_prime(36))

if __name__ == "__main__":
    unittest.main()
