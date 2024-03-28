# This script uses python 3.12 to solve the 4 gallon bucket problem
# The parameters of the problem is that you have to fetch exactly 4 gallons of water from a stream using only an unmarked 5 gallon bucket, and an unmarked 3 gallon bucket in less than 15 steps.

def measure_water():
    three_gallon_bucket = 0 # Each bucket begins with no water
    five_gallon_bucket = 0
    steps = 0

    while five_gallon_bucket != 4 and three_gallon_bucket != 4:
        # Fill the 5-gallon bucket
        if five_gallon_bucket == 0:
            five_gallon_bucket = 5 # Max amount of water for the five_gallon_bucket
            steps += 1 # Every step will be counted to measure if its staying within the problems parameters of less than 15 steps
            print(f"Step {steps}: Filled 5-gallon bucket. (5 gallons in 5-gallon bucket, {three_gallon_bucket} gallons in 3-gallon bucket)")
        # Pour the 5-gallon bucket into the 3-gallon bucket
        elif three_gallon_bucket < 3: #If three_three_gallon bucket is less that 3, five gallon bucket will pour into it
            transfer = min(five_gallon_bucket, 3 - three_gallon_bucket)
            three_gallon_bucket += transfer
            five_gallon_bucket -= transfer
            steps += 1 # Every step will be counted to measure if its staying within the problems parameters of less than 15 steps
            print(f"Step {steps}: Poured {transfer} gallons from 5-gallon bucket to 3-gallon bucket. ({five_gallon_bucket} gallons in 5-gallon bucket, {three_gallon_bucket} gallons in 3-gallon bucket)")
        # Empty the 3-gallon bucket
        else:
            three_gallon_bucket = 0
            steps += 1
            print(f"Step {steps}: Emptied 3-gallon bucket. ({five_gallon_bucket} gallons in 5-gallon bucket, 0 gallons in 3-gallon bucket)")

    if five_gallon_bucket == 4:
        return f"Desired result achieved in {steps} steps: 5-gallon bucket has 4 gallons of water"
    elif three_gallon_bucket == 4:
        return f"Desired result achieved in {steps} steps: 3-gallon bucket has 4 gallons of water"
    else:
        return "Desired result not achieved"

result = measure_water()
print(result)