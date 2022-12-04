
def part1():
    pass


def main():
    print("a")
    with open('input1.txt') as f:
        lines = [line.rstrip() for line in f]
    print(lines)
    data = [0]
    counter = 0
    for entry in lines:
        if '' == entry:
            counter += 1
            data.append(0)
            continue
        else:
            data[counter] += int(entry)
    calories = sorted(data)
    print(calories[-1]+ calories[-2] + calories[-3])

if __name__ == "__main__":
    main()