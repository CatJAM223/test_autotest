from unittest import TestCase
from src.logic import solve


class TestSolve(TestCase):

    def test_r4(self):
        n, m, c, edges = 0, 0, [1], []
        expected_result = 0
        actual_result = solve(n, m, c, edges)
        self.assertEqual(expected_result, actual_result, "aa")

    def test_r5(self):
        n, m, c, edges = 4, 4, [2], []
        expected_result = 0
        actual_result = solve(n, m, c, edges)
        self.assertEqual(expected_result, actual_result, "бб")

