
def brute_force(arr):
    sums = [0 for i in range(min(arr), max(arr))]
    for i in range(min(arr), max(arr)):
        for j in range(len(arr)):
            sums[i] += cost_func(abs(i-arr[j]))
    
    return min(sums)
    # 16,1,2,0,4,2,7,1,2,14


def cost_func(cost):
    return sum(range(1,cost+1))



def read_input(inputfile):
    input_arr = []
    with open(inputfile, "r") as file:
        data  = file.readlines()
        numbers = data[0].split(",")
        #print(numbers)
        input_arr = [int(n.rstrip()) for n in numbers]
        #print(numbers)
    return input_arr


def main():
    input_arr = read_input("input_day7.txt")
    print(brute_force(input_arr))

    #print("H")
    #print(input_arr)
    #search_bits_radix(input_arr)




if __name__ == "__main__":
    main()