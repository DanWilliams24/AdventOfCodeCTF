#12.05.2022

#why spend the extra time parsing, if the initial order stays constant throughout
data = {
    1:["F", "T", "C", "L", "R", "P", "G", "Q"],
    2: ["N", "Q", "H", "W", "R", "F", "S", "J"],
    3: ["F", "B", "H", "W", "P", "M", "Q"],
    4: ["V", "S", "T", "D", "F"],
    5: ["Q", "L", "D", "W", "V", "F", "Z"],
    6: ["Z", "C", "L", "S"],
    7: ["Z", "B", "M", "V", "D", "F"],
    8: ["T", "J", "B"],
    9: ["Q", "N", "B" , "G" , "L", "S", "P" , "H"]
}

def do_instruction(quant, from_loc, to_loc):
    for i in range(quant):
        data[to_loc].append(data[from_loc].pop())

def do_instruction2(quant, from_loc, to_loc):
    if(quant > 1):
        for i in range(quant):
            data[to_loc].append(data[from_loc][(len(data[from_loc])-quant)+i])
            del data[from_loc][(len(data[from_loc])-quant)+i]
    else:
        do_instruction(quant, from_loc, to_loc)


def part1():
    with open('input5.txt') as f:
        lines = [line.rstrip() for line in f]
    for line in lines:
        do_instruction(int(line.split(" ")[1]), int(line.split(" ")[3]), int(line.split(" ")[5]))
    print(data)

def part2():
    with open('input5.txt') as f:
        lines = [line.rstrip() for line in f]
    for line in lines:
        do_instruction2(int(line.split(" ")[1]), int(line.split(" ")[3]), int(line.split(" ")[5]))
    print(data)
    ans = ""
    for key in data.keys():
        ans += data[key][-1]
    print(ans)

def main():
    part2()

if __name__ == "__main__":
    main()