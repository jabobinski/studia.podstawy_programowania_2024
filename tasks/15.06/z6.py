import unittest

def add_floats(a, b):
    """Add two floating-point numbers."""
    return a + b

class TestAddFloats(unittest.TestCase):

    def test_basic_addition(self):
        result = add_floats(0.1, 0.2)
        self.assertAlmostEqual(result, 0.3, places=7, msg=f"Error: {result} is not equal to 0.3")

    def test_negative_numbers(self):
        result = add_floats(-1.5, 2.5)
        self.assertAlmostEqual(result, 1.0, places=7, msg=f"Error: {result} is not equal to 1.0")

    def test_large_numbers(self):
        result = add_floats(1e12, 1e-12)
        self.assertAlmostEqual(result, 1e12, places=7, msg=f"Error: {result} is not equal to 1e12")

    # Additional test cases can be added as needed

if __name__ == '__main__':
    unittest.main()
