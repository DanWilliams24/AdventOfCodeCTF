# This is for part A
# runs in O(n)
def find_depth_inc(arr):
    prev_depth = None
    increasing_count = 0
    for depth in arr:
        if(prev_depth != None and depth > prev_depth):
            increasing_count += 1
            prev_depth = depth
        else:
            prev_depth = depth
    print(f"Measurements larger than the previous: {increasing_count}")


# This is for part B
# Naive Approach: O(n^2) (read data into a list)
def find_depth_inc_sliding(arr):
    prev_depth_window = None
    increasing_count = 0
    for i in range(len(arr)):
        #print(i, end=" ")
        if(i+2 < len(arr)):
            depth_window_sum = arr[i] + arr[i+1] + arr[i+2]
            if(prev_depth_window != None and depth_window_sum > prev_depth_window):
                increasing_count += 1
                prev_depth_window = depth_window_sum
            else:
                prev_depth_window = depth_window_sum
    print(f"Measurements larger than the previous window: {increasing_count}")




# Given that this is a CTF, lets exclude reading in input from file from asymptotic complexity analyses
def read_input(inputfile):
    input_arr = []
    with open(inputfile, "r") as file:
        for line in file:
            input_arr.append(int(line))
    return input_arr


def main():
    input_arr = read_input("input_day1.txt")
    find_depth_inc(input_arr)
    find_depth_inc_sliding(input_arr)





if __name__ == "__main__":
    main()