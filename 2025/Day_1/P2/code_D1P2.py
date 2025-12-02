def calc_num(dir, curr, num):
    count = 0
    if (dir == "L"):
        o = num - curr

        # account for the fact that we know it will pass 0 once
        if (curr):
            count += 1

        # add additional rotations
        count += int((o / 100))

        # account for curr landing on 0 at end
        if (not ((o) % 100)):
            count -= 1
            return 0, count

        return (100 - ((o) % 100)), count
    
    elif (dir == "R"):
        o = num + curr
        count += int(o / 100)

        # account for curr landing on 0 at end
        if (not (o % 100)):
            count -= 1

        return (((o)) % 100), count


def will_overflow(dir, curr, num):
    if dir == "L":
        return (curr < num)
    elif dir == "R":
        return (curr + num > 99)
    
def main():
    input_file = "input.txt"
    start = 50
    full_rotation_count = 0
    total_mid_rotation_count = 0

    out = open("out.txt", "w")

    with open(input_file, "r") as file:
        curr = start
        out.write(f'Current: {curr}\n')

        for line in file:
            mid_rotation_count = 0

            line.strip()

            dir = line[0].upper()
            num = int(line[1:])

            if (will_overflow(dir, curr, num)):
                result = calc_num(dir, curr, num)
                curr = result[0]
                mid_rotation_count += result[1]

            else:
                if (dir == "L"):
                    curr -= num
                if (dir == "R"):
                    curr += num

            out.write(f'Dial is rotated {dir}{num} to point at {curr}')
            if mid_rotation_count:
                out.write(f'; during this rotation, it points at 0 {mid_rotation_count} time(s).')

            if curr == 0:
                full_rotation_count += 1

            total_mid_rotation_count += mid_rotation_count
            mid_rotation_count = 0

            out.write(f'\n')
            
    print(f'Full rotation counts: {full_rotation_count}')
    print(f'Mid rotation counts: {total_mid_rotation_count}')
    print(f'Total counts: {full_rotation_count + total_mid_rotation_count}')

    out.close()

if __name__ == "__main__":
    main()