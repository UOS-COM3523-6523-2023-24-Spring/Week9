import os


def test_mini_report():  # pytest-style test case for auto-grading
    assert os.path.exists("week9-mini-report.pdf"), 'Cannot fine week9-mini-report.pdf'
    assert os.path.getsize("week9-mini-report.pdf") > 13000, 'Your mini report is too short.'