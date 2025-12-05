import re

def funct():
    print("hello")

def main():
    input_file = "../input.txt"
    count = 0
    ranges = []

    with open(input_file, "r") as file:
        reading_input_data = True
        for line in file:
            if line == "\n":
                reading_input_data = False
                continue

            line = line.strip()

            if reading_input_data:
                curr_range = line.split("-")
                ranges.append(range(int(curr_range[0]), int(curr_range[1])))
            else:
                for i in ranges:
                    if (int(line) in i):
                        count += 1
                        break
    
    print(count)        


if __name__ == "__main__":
    main()