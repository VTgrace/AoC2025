import re

def funct():
    print("hello")

def main():
    input_file = "../input.txt"
    sum = 0

    with open(input_file, "r") as file:
        data = file.read().split(',')
        
        for i in data:
            nums = re.split("-", i)

            for j in range(int(nums[0]), int(nums[1]) + 1):                
                currNum = str(j)
                length = len(currNum)

                # Ignore numbers that have an odd amount of characters
                if (length % 2):
                    continue

                length = length // 2

                # Check that first half equals second half
                if (currNum[length:] == currNum[:length]):
                    sum += j

    print(sum)


if __name__ == "__main__":
    main()