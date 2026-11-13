import unittest

def calculate_grade(quiz, project, final_exam, practical):
    return round(
        (quiz * 0.10) +
        (project * 0.20) +
        (final_exam * 0.50) +
        (practical * 0.20),
        2
    )

class TestGrades(unittest.TestCase):

    def test_normal_marks(self):
        self.assertEqual(
            calculate_grade(80, 70, 90, 85),
            84.0
        )

    def test_zero_marks(self):
        self.assertEqual(
            calculate_grade(0, 0, 0, 0),
            0
        )

    def test_full_marks(self):
        self.assertEqual(
            calculate_grade(100, 100, 100, 100),
            100
        )

if __name__ == "__main__":
    unittest.main()