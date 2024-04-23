import unittest
import os


class Autograde(unittest.TestCase):
    def test_mini_report(self):  # pytest-style test case for auto-grading
        self.assertTrue(os.path.exists("week9-mini-report.pdf"), 'Cannot fine week9-mini-report.pdf')
        self.assertTrue(os.path.getsize("week9-mini-report.pdf") > 13000, 'Your mini report is too short.')