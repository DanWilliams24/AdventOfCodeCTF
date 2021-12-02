# This is part one
def find_position(arr):
    horizontal = 0
    depth = 0
    for cmd in arr:
        parts = cmd.split(" ")
        cmd_name = parts[0]
        value = int(parts[1])

        if(cmd_name == "forward"):
            horizontal += value
        elif(cmd_name == "down"):
            depth += value
        elif(cmd_name == "up"):
            depth -= value
    print(f"Final position of Sub: Horizontal - {horizontal}, Depth - {depth}")    
    print(f"Product of Horizontal and depth: {horizontal*depth}")


# This is part two
def find_angled_position(arr):
    horizontal = 0
    depth = 0
    aim = 0
    for cmd in arr:
        parts = cmd.split(" ")
        cmd_name = parts[0]
        value = int(parts[1])

        if(cmd_name == "forward"):
            horizontal += value
            depth += aim*value
        elif(cmd_name == "down"):
            aim += value
        elif(cmd_name == "up"):
            aim -= value
    print(f"Final Aimed position of Sub: Horizontal - {horizontal}, Depth - {depth}")    
    print(f"Product of Horizontal and depth: {horizontal*depth}")



def read_input(inputfile):
    input_arr = []
    with open(inputfile, "r") as file:
        for line in file:
            input_arr.append(line)
    return input_arr


def main():
    input_arr = read_input("input_day2.txt")
    find_position(input_arr)
    find_angled_position(input_arr)




if __name__ == "__main__":
    main()