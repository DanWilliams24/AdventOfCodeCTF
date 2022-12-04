
def contains(start, end, start1, end1):
    return True if int(start1) <= int(start) and int(end1) >= int(end) else False


def contains1(start, end, start1, end1):
    return any([i in range(int(start1), int(end1)+1) for i in range(int(start),int(end)+1)])
 

def part1():
    lines = []
    with open('input4.txt') as f:
        lines = [line.rstrip() for line in f]
    count = 0
    for line in lines:
        range1, range2 = line.split(",")
        range1 = range1.split("-")
        range2 = range2.split("-")
        if(contains(range1[0], range1[1],range2[0], range2[1] ) ):
            print(range1)
            count += 1
        elif (contains(range2[0], range2[1],range1[0], range1[1] )):
            print(range2)
            count += 1
        elif(contains1(range1[0], range1[1],range2[0], range2[1] ) ):
            print(range1)
            count += 1
        elif (contains1(range2[0], range2[1],range1[0], range1[1] )):
            print(range2)
            count += 1


    print(count)

def part2():
    pass

def main():
    part1()

if __name__ == "__main__":
    main()