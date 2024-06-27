import unittest
import threading
import time

class Counter:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()

    def increment(self):
        for _ in range(1000):
            with self.lock:
                self.value += 1
            # Simulate some work
            time.sleep(0.001)

class TestMultiThreading(unittest.TestCase):

    def test_increment_counter(self):
        counter = Counter()
        threads = []

        # Create multiple threads to increment the counter concurrently
        for _ in range(10):
            thread = threading.Thread(target=counter.increment)
            threads.append(thread)
            thread.start()

        # Wait for all threads to complete
        for thread in threads:
            thread.join()

        # Check if the counter was incremented correctly
        expected_counter = 10000  # 1000 increments per thread, 10 threads
        self.assertEqual(counter.value, expected_counter, f"Error: Counter value is {counter.value}, expected {expected_counter}")

if __name__ == '__main__':
    unittest.main()
