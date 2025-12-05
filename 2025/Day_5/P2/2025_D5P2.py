import re

def funct():
    print("hello")

def main():
    input_file = "../input2.txt"
    count = 0
    mySet = set()

    with open(input_file, "r") as file:
        reading_input_data = True
        for line in file:
            line = line.strip()
            the_range = line.split("-")
            print(the_range)

            start = int(the_range[0])
            end = int(the_range[1])

            for i in range(start, end + 1):
                mySet.add(i)

    
    print(len(mySet))  


if __name__ == "__main__":
    main()