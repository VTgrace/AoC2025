def main():
    input_file = "../input.txt"
    problems = []
    total = 0

    with open(input_file, "r") as file:
        for line in file:
            stripped = line.strip()

            currLine = stripped.split()
            problems.append(currLine)

    print(f'rows: {len(problems)} cols: {len(problems[0])}')

    for c in range(len(problems[0]) - 1, -1, -1):
        currTotal = 0
        addNumbers = False

        if (problems[len(problems) - 1][c] == "+"):
            addNumbers = True
        elif (problems[len(problems) - 1][c] == "*"):
            currTotal = 1
            addNumbers = False
        
        for r in range(len(problems) - 2, -1, -1):
            currNum = int(problems[r][c])

            if (addNumbers):
                currTotal += currNum
            else:
                currTotal *= currNum

        total += int(currTotal)

    print(total)

if __name__ == "__main__":
    main()