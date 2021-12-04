
#this is part 1, this is part 2
def get_bits(arr):
    #create a bit count arr, with indexes for each column 
    bit_counts = [0 for i in range(len(arr[0]))]
    

    # we iterate through the entire list once, so O(n) since the digits are of fixed size
    for digits in arr:
        for i in range(len(digits)):
            # if 0, minus 1, if 1 add 1
            # whether its greater or less than 0 dictates whether its 0 or 1
            if(digits[i] == "0"):
                bit_counts[i] -= 1
            elif(digits[i] == "1"):
                bit_counts[i] += 1
    print(bit_counts)
    final_binary_ep = ""
    final_binary_gam = ""
    for num in bit_counts:
        if(num > 0):
            final_binary_ep += "1"
            final_binary_gam += "0"
        elif(num < 0):
            final_binary_ep += "0"
            final_binary_gam += "1"
    print(f"Final Binary ESP: {final_binary_ep}")
    print(f"Final Binary GAM: {final_binary_gam}")
    return final_binary_ep
    

# this is part 2
def search_bits(arr):
    bit_counts = get_bits(arr)
    best_ones = []
    for binary in arr:
        matches = 0
        for i in range(len(bit_counts)):
            if(bit_counts[i] == binary[i]):
                matches += 1
            else:
                break

        if(not best_ones):
            best_ones.insert(0, (binary, matches))
        elif(matches >= best_ones[0][1]):
            best_ones.insert(0, (binary, matches))
    print(best_ones)


def search_bits_radix(arr):
    bitstrings = [bits for bits in arr]
    bad_indexes = []
    #for each column
    for i in range(len(arr[0])):
        if(len(bitstrings) == 1):
            break

        balance = 0
        # for each row
        for j in range(len(arr)):
            if j in bad_indexes:
                continue
            
            # if 0, minus 1, if 1 add 1
            # whether its greater or less than 0 dictates whether its 0 or 1
            if(arr[j][i] == "0"):
                balance -= 1
            elif(arr[j][i] == "1"):
                balance += 1

        
        to_delete = []
        print(f"Balance: {balance}")
        if(balance > 0):
            print(f"1 is most significant")
            # 1 is the most significant

            # delete all bitstrings with 0 at this column
            
            for row in range(len(bitstrings)):
                bitstring = bitstrings[row]
                print(f"Looking at {bitstring}")
                print(f"(col {i}) {bitstring[i]} == 0 {bitstring[i] == '0'}")
                if(bitstring[i] == "0"):
                    to_delete.append(bitstring)
                    bad_indexes.append(row)
            
        elif(balance < 0):
            print(f"0 is most significant")
            # 0 is the most significant

            # delete all bitstrings with 1 at this column 
            for row in range(len(bitstrings)):
                bitstring = bitstrings[row]
                print(f"Looking at {bitstring}")
                print(f"(col {i}) {bitstring[i]} == 1 {bitstring[i] == '1'}")
                if(bitstring[i] == "1"):
                    to_delete.append(bitstring)
                    bad_indexes.append(row)
        else:
            print("UHHHHHHH")

        print(bitstrings)
        for item in to_delete:
            
            bitstrings.remove(item)
        print(bitstrings)
        
        print(f"Current List of bitstrings: {bitstrings}")

    print(f"Final String from Search: {bitstrings}")





def read_input(inputfile):
    input_arr = []
    with open(inputfile, "r") as file:
        for line in file:
            input_arr.append(line.rstrip())
    return input_arr


def main():
    input_arr = read_input("input_day3.txt")
    search_bits_radix(input_arr)




if __name__ == "__main__":
    main()