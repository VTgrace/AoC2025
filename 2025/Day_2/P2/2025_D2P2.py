import re

def find_factors(num):
    factors = []
    for i in range(1, num + 1):
        if (not (num % i)):
            factors.append(i)

    return factors


def main():
    input_file = "../input.txt"
    sum = 0

    with open(input_file, "r") as file:
        data = file.read().split(',')
        
        for i in data:
            # Separate ranges
            nums = re.split("-", i)

            # Loop through every number in range
            for j in range(int(nums[0]), int(nums[1]) + 1):                
                currNum = str(j)
                length = len(currNum)

                factors = (find_factors(length))

                # Check for invalid ID in every factor
                for k in factors:
                    pattern = currNum[:k]
                    matches = re.findall(pattern, currNum)

                    # Check for invalid ID
                    # If found, stop checking other factors
                    if (len(matches) == (length / k) and len(matches) > 1):
                        sum += j
                        break
    print(sum)

if __name__ == "__main__":
    main()