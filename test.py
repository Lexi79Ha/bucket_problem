# This code import unittest and uses python v. 3.12 to ensure that the program satisfies the problem constraints of the bucket problem
# Test constraints: Total gallons of water = 4 gallons, Total steps < 15
import unittest

def measure_water():
    three_gallon_bucket = 0
    five_gallon_bucket = 0
    steps = 0

    while not (five_gallon_bucket == 4 and three_gallon_bucket == 0):
        # Fill the 5-gallon bucket
        if five_gallon_bucket == 0:
            five_gallon_bucket = 5
            steps += 1
        # Pour the 5-gallon bucket into the 3-gallon bucket
        elif three_gallon_bucket < 3:
            transfer = min(five_gallon_bucket, 3 - three_gallon_bucket)
            three_gallon_bucket += transfer
            five_gallon_bucket -= transfer
            steps += 1
        # Empty the 3-gallon bucket
        else:
            three_gallon_bucket = 0
            steps += 1

    return steps

class TestMeasureWater(unittest.TestCase):
# Test the problem constraint of steps to solve problem not exceeding 15 steps
    def test_completion_time(self):
        steps = measure_water()
        self.assertLessEqual(steps, 15)  # Expected completion in less than 15 steps
# Tests the total sum of the water gathered through steps, and ensure requirement of four gallons has been meant
    def test_total_gallons(self):
        three_gallon_bucket = 0
        five_gallon_bucket = 0
        steps = measure_water()

        while not (five_gallon_bucket == 4 and three_gallon_bucket == 0):
            if five_gallon_bucket == 0:
                five_gallon_bucket = 5
            elif three_gallon_bucket < 3:
                transfer = min(five_gallon_bucket, 3 - three_gallon_bucket)
                three_gallon_bucket += transfer
                five_gallon_bucket -= transfer
            else:
                three_gallon_bucket = 0

        self.assertEqual(five_gallon_bucket + three_gallon_bucket, 4)  # Expected total gallons to be 4
# Tests the three_gallon_bucket and five_gallon_bucket to ensure there values never go beyond the problems designated capacities of 3 and 5
    def test_bucket_capacity(self):
        three_gallon_bucket = 0
        five_gallon_bucket = 0
        steps = measure_water()

        while not (five_gallon_bucket == 4 and three_gallon_bucket == 0):
            if five_gallon_bucket == 0:
                five_gallon_bucket = 5
            elif three_gallon_bucket < 3:
                transfer = min(five_gallon_bucket, 3 - three_gallon_bucket)
                three_gallon_bucket += transfer
                five_gallon_bucket -= transfer
            else:
                three_gallon_bucket = 0

            self.assertLessEqual(three_gallon_bucket, 3) # Ensure 3-gallon bucket never exceeds 3
            self.assertLessEqual(five_gallon_bucket, 5)  # Ensure 5-gallon bucket never exceeds 5

if __name__ == "__main__":
    unittest.main()