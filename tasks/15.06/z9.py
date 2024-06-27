import unittest
import sqlite3

def query_students_by_age(min_age):
    """Query students from database by minimum age."""
    try:
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        cursor.execute(f"SELECT name FROM students WHERE age >= ?", (min_age,))
        results = cursor.fetchall()
        conn.close()
        return [row[0] for row in results]  # Extracting names from results
    except Exception as e:
        print(f"Failed to query database: {e}")
        return []

class TestDatabaseQuery(unittest.TestCase):

    def setUp(self):
        # Set up any necessary resources before each test
        self.create_test_data()

    def tearDown(self):
        # Clean up any resources after each test
        self.delete_test_data()

    def create_test_data(self):
        # Create test data in the database
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
        cursor.execute("INSERT INTO students (name, age) VALUES ('Alice', 20)")
        cursor.execute("INSERT INTO students (name, age) VALUES ('Bob', 22)")
        cursor.execute("INSERT INTO students (name, age) VALUES ('Charlie', 25)")
        conn.commit()
        conn.close()

    def delete_test_data(self):
        # Delete test data from the database
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS students")
        conn.commit()
        conn.close()

    def test_query_students_by_age(self):
        # Test case 1: Query students with age >= 22
        expected_result = ['Bob', 'Charlie']
        result = query_students_by_age(22)
        self.assertEqual(result, expected_result, f"Error: Query result {result} does not match expected {expected_result}")

        # Test case 2: Query students with age >= 18 (including all)
        expected_result_all = ['Alice', 'Bob', 'Charlie']
        result_all = query_students_by_age(18)
        self.assertEqual(result_all, expected_result_all, f"Error: Query result {result_all} does not match expected {expected_result_all}")

if __name__ == '__main__':
    unittest.main()
