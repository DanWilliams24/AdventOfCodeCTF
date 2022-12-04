
def part1():
    print("a")
    with open('input3.txt') as f:
        lines = [line.rstrip() for line in f]

    score = 0
    for line in lines:
        cmpt1 = line[:int(len(line)/2)]
        cmpt2 = line[int(len(line)/2):]
        shared_chars = []
        print(cmpt1, cmpt2)
        cmpt1 = list(cmpt1)
        cmpt2 = list(cmpt2)

        for i in range(len(cmpt1)):
            if cmpt1[i] in cmpt2:
                shared_chars.append(cmpt1[i])

        #print(shared_chars)
        
        print(list(set(shared_chars)))
        
        for item in set(shared_chars):
            if (item != item.lower()):
                #uppercase
                print("is upper")
                print(item, ord(item)-64+26)
                score += (ord(item)-64)+26
            else:
                #lower
                print("is lower")
                print(item, ord(item)-96)
                score += (ord(item)-96)
            
            #print(item, ord(item)-97)
            print(score)
    print(score)


def determine_sets(list1, list2, list3):
    return list(set(list1) & set(list2) & set(list3))


def part2():
    print("a")
    with open('input3.txt') as f:
        lines = [line.rstrip() for line in f]

    score = 0
    for i in range(0, len(lines), 3):
        sack1 = list(lines[i])
        sack2 = list(lines[i+1])
        sack3 = list(lines[i+2])

        shared_chars = []
        #print(sack1, sack2,sack3)

        shared_chars = determine_sets(sack1, sack2, sack3)
        
        print(list(set(shared_chars)))
        
        for item in set(shared_chars):
            if (item != item.lower()):
                #uppercase
                #print("is upper")
                #print(item, ord(item)-64+26)
                score += (ord(item)-64)+26
            else:
                #lower
                #print("is lower")
                #print(item, ord(item)-96)
                score += (ord(item)-96)
            
            #print(item, ord(item)-97)
            print(score)
    print(score)


def main():
    part2()

if __name__ == "__main__":
    print(ord("A")-64)
    main()