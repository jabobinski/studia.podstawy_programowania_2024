import unittest

def parse_and_validate_input(input_string):
    """Parse and validate input string."""
    try:
        # Assume input format: "name,age,email"
        name, age_str, email = input_string.split(',')
        age = int(age_str.strip())

        # Validate age range (example: age should be between 18 and 100)
        if age < 18 or age > 100:
            return False, "Age must be between 18 and 100"

        # Validate email format (basic check for simplicity)
        if '@' not in email or '.' not in email:
            return False, "Invalid email format"

        # If all checks pass, return True (valid input)
        return True, "Input data is valid"

    except ValueError:
        return False, "Invalid input format"

class TestParseAndValidateInput(unittest.TestCase):

    def test_valid_input(self):
        input_string = "John Doe,25,john.doe@example.com"
        valid, message = parse_and_validate_input(input_string)
        self.assertTrue(valid, f"Expected valid input, got: {message}")

    def test_invalid_age(self):
        input_string = "Jane Smith,17,jane.smith@example.com"
        valid, message = parse_and_validate_input(input_string)
        self.assertFalse(valid, f"Expected invalid age, got: {message}")

    def test_invalid_email(self):
        input_string = "Bob Johnson,30,bob.johnson.example.com"
        valid, message = parse_and_validate_input(input_string)
        self.assertFalse(valid, f"Expected invalid email format, got: {message}")

    def test_invalid_format(self):
        input_string = "Alice Brown,28"
        valid, message = parse_and_validate_input(input_string)
        self.assertFalse(valid, f"Expected invalid input format, got: {message}")

if __name__ == '__main__':
    unittest.main()
