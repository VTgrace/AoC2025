def calc_num(dir, curr, num):
    if (dir == "L"):
        if (((num - curr) % 100) == 0):
            return 0

        return(100 - ((num - curr) % 100))
    elif (dir == "R"):
        return (((curr + num)) % 100)


def will_overflow(dir, curr, num):
    if dir == "L":
        return (curr - num < 0)
    elif dir == "R":
        return (curr + num > 99)
    
def main():
    input_file = "input.txt"
    start = 50
    count = 0

    out = open("out.txt", "w")

    with open(input_file, "r") as file:
        curr = start
        out.write(f'Current: {curr}\n')

        for line in file:
            line.strip()

            dir = line[0].upper()
            num = int(line[1:])

            if (will_overflow(dir, curr, num)):
                curr = calc_num(dir, curr, num)
            else:
                if (dir == "L"):
                    curr -= num
                if (dir == "R"):
                    curr += num

            out.write(f'Dial is rotated {dir}{num} to point at {curr}\n')

            if curr == 0:
                count += 1
            
    print(count)
    out.close()

if __name__ == "__main__":
    main()