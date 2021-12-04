

def get_bingo_winner(boards, queue):
    #create a  winners array for all horizontals and diagonals
    best = []
    winners = []
    for i in range(len(boards)):
        board = boards[i]
        winners = [0 for k in range(len(board)*2)]
        res = False
        for j in range(len(queue)):
            item = queue[j]
            pos = find_pos(board, item)
            if(pos == -1):
                continue
            x, y = pos
            winners[x] += 1
            winners[5+y] += 1
            res = check_winners(winners)
            if(res):
                #append the last item read before winning to our best list
                best.append(j)
                break

    maxi = 0
    for i in range(len(best)):
        if(best[i] > best[maxi]):
            maxi = i
    
    print(f"Best Bingo player is number: {maxi}")
    print(winners)
    print(boards[maxi])
    return boards[maxi]

def board_check(board, queue):
    winners = [0 for k in range(len(board)*2)]
    res = False
    for j in range(len(queue)):
        item = queue[j]
        pos = find_pos(board, item)
        if(pos == -1):
            continue
        x, y = pos
        board[x][y] = 'X'
        winners[x] += 1
        winners[5+y] += 1
        res = check_winners(winners)
        if(res):
            print(f"Last digit called {item}")
            
            break
        
    
    


def check_winners(winners):
    if(int(len(winners)/2) in winners):
        return True

def find_pos(board, elem):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if(board[i][j] == elem):
                return (i, j)
    return -1


def read_input(inputfile):
    input_arr = []
    with open(inputfile, "r") as file:
        lines = file.readlines()
        queue = [int(i) for i in lines[0].split(",")]
        arr = []
        for line in lines[2:]:
            
            if(line == "\n"):
                
                input_arr.append(arr)
                #print(f"input arr: ")
                #print_2d_arr(input_arr)
                arr = []
                continue
            numbers = []
            for number in line.split(" "):
                if(number.rstrip().isnumeric()):
                    numbers.append(int(number))
            #print(numbers)
            arr.append(numbers)
        #print(arr)

    return input_arr, queue

def print_2d_arr(arr):
    for items in arr:
        for item in items:
            for it in item:
                print(f"{it}", end=" ")
            print(" ")
        print("")

def main():
    input_arr, queue = read_input("input_day4.txt")
    print("FINAL")
    print_2d_arr(input_arr)
    print(queue)

    
    minimum_board = get_bingo_winner(input_arr, queue)
    print("what i need")
    board_check(minimum_board, queue)
    print(minimum_board)
    

if __name__ == "__main__":
    main()