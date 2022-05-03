

def build_polymer(template, rules):
    res_template = ""
    #print(res_template)
    for i in range(1,len(template)):
        rule = template[i-1:i+1]
        insertion = rules[rule]
        created = template[i-1] + insertion
        res_template += created
    res_template += template[-1]

    #print(res_template)
    return res_template


def iterate_polymers(template, rules, iterations):
    new_template = template
    for i in range(iterations):
        print(f"Current Iteration: {i+1}, size = {len(new_template)}")
        new_template = build_polymer(new_template, rules)
    
    counts = {}
    max_letter = new_template[0]
    min_letter = new_template[0]
    for letter in new_template:
        
        if(letter not in counts):
            the_count = new_template.count(letter)
            counts[letter] = the_count
            if(the_count > counts[max_letter]):
                max_letter = letter
            
            if(the_count < counts[min_letter]):
                min_letter = letter
        
            print(counts[max_letter])
            print(counts[min_letter])
    print(max_letter)
    print(min_letter)
    print(counts)
    return counts[max_letter] - counts[min_letter]

    



def read_input(inputfile):
    dictionary = {}
    template = ""
    with open(inputfile, "r") as file:
        lines = file.readlines()
        template = lines[0].rstrip()
        for i in range(2,len(lines)):
            parts = lines[i].split(" -> ")
            dictionary[parts[0].rstrip()] = parts[1].rstrip()
    return template, dictionary


def main():
    template, dictionary = read_input("input_day14.txt")
    the_sum = iterate_polymers(template, dictionary, 40)
    print(the_sum)



if __name__ == "__main__":
    main()
