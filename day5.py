

def read_input(inputfile):
    input_arr = []
    with open(inputfile, "r") as file:
        for line in file:
            parts = line.split(" -> ")
            
            input_arr.append(line.rstrip())
    return input_arr


def main():
    input_arr = read_input("input_day3.txt")
    #print("H")
    #print(input_arr)
    #search_bits_radix(input_arr)




if __name__ == "__main__":
    main()