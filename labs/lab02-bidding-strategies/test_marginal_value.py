import unittest
from marginal_value import calculate_marginal_value

class TestMarginalValue(unittest.TestCase):

    def test_example_case(self):
        goods = {"A", "B"}
        bids = {"A": 95, "B": 90}
        prices = {"A": 80, "B": 80}

        def valuation(bundle):
            if "A" in bundle and "B" in bundle:
                return 100
            elif "A" in bundle:
                return 90
            elif "B" in bundle:
                return 70
            return 0

        mv_a = calculate_marginal_value(goods, "A", valuation, bids, prices)
        expected_mv_a = 30
        self.assertAlmostEqual(mv_a, expected_mv_a, places=3, msg=f"Incorrect marginal value for A: expected {expected_mv_a}, got {mv_a}")

    def test_no_goods_won(self):
        goods = {"A", "B"}
        bids = {"A": 50, "B": 50}
        prices = {"A": 100, "B": 100}

        def valuation(bundle): 
            return len(bundle) * 10 

        mv_a = calculate_marginal_value(goods, "A", valuation, bids, prices)
        mv_b = calculate_marginal_value(goods, "B", valuation, bids, prices)
        self.assertEqual(mv_a, 10, "Incorrect marginal value for A")
        self.assertEqual(mv_b, 10, "Incorrect marginal value for B")

    def test_student_case_1(self):

        goods = {"A", "B", "C"}
        bids = {"A": 100, "B": 80, "C": 100}
        prices = {"A": 50, "B": 70, "C": 50}

        def student_valuation(bundle):
            values = {"A": 40, "B": 60, "C": 50}
            return sum(values[g] for g in bundle)

        mv_b = calculate_marginal_value(goods, "B", student_valuation, bids, prices)
        self.assertEqual(mv_b, 60, "Incorrect marginal value for B in student test case 1")

    def test_student_case_2(self):

        goods = {"X", "Y", "Z"}
        bids = {"X": 30, "Y": 20, "Z": 20}
        prices = {"X": 25, "Y": 50, "Z": 50}

        def student_valuation(bundle):
            return 5 * len(bundle)

        mv_x = calculate_marginal_value(goods, "X", student_valuation, bids, prices)
        self.assertEqual(mv_x, 5, "Incorrect marginal value for X in student test case 2")

    def test_student_case_3(self):

        goods = {"P", "Q", "R"}
        bids = {"P": 80, "Q": 40, "R": 70}
        prices = {"P": 60, "Q": 30, "R": 65}

        def student_valuation(bundle):
            base_values = {"P": 50, "Q": 30, "R": 40}
            bonus = 20 if "P" in bundle and "Q" in bundle else 0
            return sum(base_values[g] for g in bundle) + bonus

        mv_r = calculate_marginal_value(goods, "R", student_valuation, bids, prices)
        self.assertEqual(mv_r, 40, "Incorrect marginal value for R in student test case 3")

if __name__ == "__main__":
    unittest.main()
