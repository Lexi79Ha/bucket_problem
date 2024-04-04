# This script uses python 3.12 to solve the 4 gallon bucket problem
# The parameters of the problem is that you have to fetch exactly 4 gallons of water from a stream using only an unmarked 5 gallon bucket, and an unmarked 3 gallon bucket in less than 15 steps.
# This program uses a while not loop under the conditions that "Five_gallon_bucket = 4 and the three_gallon_bucket = 3"
# The steps of the loop are as followed: Fill five_gallon_bucket, Pour five_gallon_bucket into the three gallon bucket, then empty three gallon bucket once it reached max capacity, this continues until all conditions are meant
def measure_water():
    three_gallon_bucket = 0 # Buckets start out empty
    five_gallon_bucket = 0 # Buckets start out empty
    steps = 0

    while not (five_gallon_bucket == 4 and three_gallon_bucket == 0):
        # Fill the 5-gallon bucket
        if five_gallon_bucket == 0:
            five_gallon_bucket = 5
            steps += 1 # Amount of steps will increase through every action
            print(f"Step {steps}: Filled 5-gallon bucket. (5 gallons in 5-gallon bucket, {three_gallon_bucket} gallons in 3-gallon bucket)")
        # Pour the 5-gallon bucket into the 3-gallon bucket
        elif three_gallon_bucket < 3:
            transfer = min(five_gallon_bucket, 3 - three_gallon_bucket)
            three_gallon_bucket += transfer
            five_gallon_bucket -= transfer
            steps += 1 # Amount of steps will increase through every action
            print(f"Step {steps}: Poured {transfer} gallons from 5-gallon bucket to 3-gallon bucket. ({five_gallon_bucket} gallons in 5-gallon bucket, {three_gallon_bucket} gallons in 3-gallon bucket)")
        # Empty the 3-gallon bucket
        else:
            three_gallon_bucket = 0
            steps += 1 # Amount of steps will increase through every action
            print(f"Step {steps}: Emptied 3-gallon bucket. ({five_gallon_bucket} gallons in 5-gallon bucket, 0 gallons in 3-gallon bucket)")

    return f"Desired result achieved in {steps} steps: 5-gallon bucket has 4 gallons of water and 3-gallon bucket is empty"

result = measure_water()
print(result)