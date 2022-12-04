
def part1():
    strat = {'X': 1, #rock
            'Y': 2, #paper
            "Z": 3} #scissors

    player = {
        'A': 1, #rock
        'B': 2, #paper
        'C': 3 #scissors
    }

    print("a")
    with open('input2.txt') as f:
        lines = [line.rstrip() for line in f]
    print(lines)
    score = 0
    for game in lines:
        op, you = game.split(" ")
        if(strat[you] == player[op] ):
            print("LAST CASE")
            print("here", score,strat[you] + 3)
            score += strat[you] + 3
        elif((op == "B" and you == "X") or (op == "A" and you == "Z") or (op == "C" and you == "Y")):
            score += strat[you] + 0
        else:
            score += strat[you] + 6
        print(score)
    print(score)


def part2():
    strat = {'X': 0, #lose
            'Y': 3, #draw
            "Z": 6} #win

    player = {
        'A': 1, #rock
        'B': 2, #paper
        'C': 3 #scissors
    }

    print("a")
    with open('input2.txt') as f:
        lines = [line.rstrip() for line in f]
    print(lines)
    score = 0
    for game in lines:
        op, you = game.split(" ")
        if strat[you] == 3:
            # need draw 
            score += strat[you] + player[op]
        elif strat[you] == 0:
            if op == "B":
                score += strat[you] + player["A"]
            elif op == "A":
                score += strat[you] + player["C"]
            elif op == "C":
                score += strat[you] + player["B"]
        elif strat[you] == 6:
            if op == "B":
                score += strat[you] + player["C"]
            elif op == "A":
                score += strat[you] + player["B"]
            elif op == "C":
                score += strat[you] + player["A"]

    print(score)

    '''
    if rock and paper # paper

    else if rock and scissors # rock

    else if scissors and paper # scissors
    '''
def main():
    part2()

if __name__ == "__main__":
    main()