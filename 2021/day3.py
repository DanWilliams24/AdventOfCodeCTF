
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

def compare_bit_counts(zeros, ones, is_oxygen):
    if(is_oxygen):
        return (zeros > ones)


def search_bits_fast(arr, is_oxygen=True):
    
    candidates = arr.copy()
    digits = ""
    #every bitstring is the same length
    str_len = len(arr[0])
    for col in range(str_len):
        #print(candidates)
        new_arr = []
        zeros = 0
        ones = 0
        for row in range(len(candidates)):
            if(candidates[row][col] == "0"):
                zeros += 1
            elif(candidates[row][col] == "1"):
                ones += 1


        sig_bit = ""
        #print(f"for column {col}: {zeros},{ones}")
        if(zeros == ones):
            #print("zeros are equal to ones")
            if(is_oxygen):
                sig_bit = "1"
            else:
                sig_bit = "0"
        else:
            if(is_oxygen):
                sig_bit = "0" if max(zeros, ones) == zeros else "1"
            else:
                sig_bit = "0" if min(zeros, ones) == zeros else "1"
                
        digits += sig_bit

        #print(f"Significant bit for column {col} is {sig_bit}")
        for i in range(len(candidates)):
            

            if(candidates[i][col] == sig_bit):
                if(digits != candidates[i][0:len(digits)]):
                    print(f"Problem here: {candidates[i]}")
                new_arr.append(candidates[i])
        candidates = new_arr.copy()
        
        if(len(candidates) == 1):
            break
    

    if(len(candidates) == 1):
        if(is_oxygen):
            print(f"Oxygen Rating Bitstring: {candidates[0]}")
        else:
            print(f"CO2 Rating Bitstring: {candidates[0]}")
    else:
        print(f"failed; Elements remaining {candidates}")
    print(f"Bits: {digits}")
    




def read_input(inputfile):
    input_arr = []
    with open(inputfile, "r") as file:
        for line in file:
            input_arr.append(line.rstrip())
    return input_arr


def main():
    input_arr = read_input("input_day3.txt")
    #print("H")
    #print(input_arr)
    search_bits_fast(input_arr, is_oxygen=True)
    search_bits_fast(input_arr, is_oxygen=False)
    #search_bits_radix(input_arr)




if __name__ == "__main__":
    main()