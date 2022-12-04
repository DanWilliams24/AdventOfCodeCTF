class Pixel:
    def __init__(self, x, y, z) -> None:
        self.pos = (x,y,z)
        self.x = 0
        self.y = 0
        self.z = 0
        self.status = False
    

    def inbounds(self):
        return (self.inbound(self.pos[0]) and self.inbound(self.pos[1]) and self.inbound(self.pos[2]))


    def inbound(x):
        return x < 50 and x > -50
    
class Board:
    def __init__(self) -> None:
        self.matrix = {}
    
    #do a cool dictionary trick
    def insert_coord(self, point, status):
        self.matrix[point] = status
        
        
    def get_all_on(self):
        on = 0
        #print(list(self.matrix.keys()))
        for key in self.matrix.keys():
            if(self.matrix[key] == True):
                on += 1

        return on
    

def generate_dim_coord(intervals, count):
    coords = []
    #print(intervals)
    for i in range(*intervals[0]):
        for j in range(*intervals[1]):
            for k in range(*intervals[2]):
                coords.append((i, j, k))
        
    #print(len(coords))
    return coords

def read_input(inputfile):
    print("Preprocessing:")
    coord_list = []
    with open(inputfile, "r") as file:
        
        lines = file.readlines()
        for i in range(len(lines)):
            print(f"Line #{i+1}")
            parts = lines[i].split(" ")
            status = (parts[0] == "on")
            dims = parts[1].split(",")
            unzipped_dimension_coords = []
            intervals = []
            for dim in dims:
                parts = dim[2:].split("..")
                start = int(parts[0])
                stop = int(parts[1]) + 1
                intervals.append((start, stop))
            
            unzipped_dimension_coords.append(generate_dim_coord(intervals, abs(stop-start)))
            
            coords = list(zip(*unzipped_dimension_coords))
            #print(list(coords))
            #print(dims)
            coord_list.append((coords, status))
            #print(status)
            
    return coord_list
    


def main():
    instructions = read_input("input_day22.txt")

    board = Board()
    count = 1
    for coord_value_pair in instructions:
        print(f"On line number {count}/{len(instructions)}")
        #print(coord_value_pair)
        status = coord_value_pair[1]
        for tupl in coord_value_pair[0]:
            #print(tupl)
            board.insert_coord(tupl, status)
        count += 1
    
    print(f"Answer: {board.get_all_on()}")



if __name__ == "__main__":
    main()
