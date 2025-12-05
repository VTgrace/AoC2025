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

            if reading_input_data:
                ranges.append(line.strip())
            else:
                for i in ranges:
                    range = i.split("-")

                    diff = int(range[1]) - int(range[0])

                    if ((int(line)) <= int(range[1]) and (int(line)) >= int(range[0])):
                        count += 1
                        break
    
    print(count)        


if __name__ == "__main__":
    main()