
"""
Test harness for the SentinelOps CO2 assessment.
Run using: python test_module.py
"""

import math
import unittest

from sentinelops_module import (
    optimized_sort_alerts,
    optimized_is_blocked,
    optimized_find_signature,
    optimized_closest_logins,
)


class TestSentinelOps(unittest.TestCase):

    def test_sort_alerts(self):
        alerts = [
            ("A1", 3), ("A2", 9), ("A3", 5),
            ("A4", 9), ("A5", 1)
        ]
        result = optimized_sort_alerts(alerts)
        self.assertEqual(
            result,
            [("A2", 9), ("A4", 9), ("A3", 5),
             ("A1", 3), ("A5", 1)]
        )

    def test_equal_severities_preserve_order(self):
        alerts = [("A1", 5), ("A2", 5), ("A3", 5)]
        self.assertEqual(
            optimized_sort_alerts(alerts), alerts
        )

    def test_empty_alerts(self):
        self.assertEqual(optimized_sort_alerts([]), [])

    def test_blocked_ip(self):
        blocklist = ["10.0.0.5", "10.0.0.9"]
        self.assertTrue(
            optimized_is_blocked(blocklist, "10.0.0.9")
        )
        self.assertFalse(
            optimized_is_blocked(blocklist, "8.8.8.8")
        )

    def test_empty_blocklist(self):
        self.assertFalse(optimized_is_blocked([], "10.0.0.9"))

    def test_signature_search(self):
        self.assertEqual(
            optimized_find_signature("FAILFAIXFAIL", "FAIL"),
            [0, 8]
        )

    def test_signature_at_end(self):
        self.assertEqual(
            optimized_find_signature("ABCXYZ", "XYZ"), [3]
        )

    def test_pattern_longer_than_log(self):
        self.assertEqual(
            optimized_find_signature("ABC", "ABCDE"), []
        )

    def test_overlapping_signatures(self):
        self.assertEqual(
            optimized_find_signature("AAAA", "AA"), [0, 1, 2]
        )

    def test_empty_pattern(self):
        self.assertEqual(
            optimized_find_signature("ABC", ""), [0, 1, 2, 3]
        )

    def test_closest_pair(self):
        events = [
            (2, 3), (12, 30), (40, 50),
            (5, 1), (12, 10), (3, 4)
        ]
        pair, distance = optimized_closest_logins(events)

        self.assertIsNotNone(pair)
        self.assertAlmostEqual(distance, 1.0)

    def test_fewer_than_two_events(self):
        self.assertEqual(
            optimized_closest_logins([]), (None, math.inf)
        )
        self.assertEqual(
            optimized_closest_logins([(1, 2)]),
            (None, math.inf)
        )

    def test_duplicate_locations(self):
        events = [(1, 1), (1, 1), (5, 5)]
        pair, distance = optimized_closest_logins(events)

        self.assertEqual(distance, 0.0)
        self.assertEqual(len(pair), 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
