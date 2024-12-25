import unittest
from logger.logger_impl import Logger

class TestLogger(unittest.TestCase):
    def setUp(self):
        self.logger = Logger()

    def test_log_info(self):
        self.logger.log_info("This is an info message")
        self.assertIn("INFO: This is an info message", self.logger.get_logs())

    def test_log_warning(self):
        self.logger.log_warning("This is a warning message")
        self.assertIn("WARNING: This is a warning message", self.logger.get_logs())

    def test_log_error(self):
        self.logger.log_error("This is an error message")
        self.assertIn("ERROR: This is an error message", self.logger.get_logs())

    def test_clear_logs(self):
        self.logger.log_info("This is an info message")
        self.logger.clear_logs()
        self.assertEqual(self.logger.get_logs(), [])

if __name__ == '__main__':
    unittest.main()