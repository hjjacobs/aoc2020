#
# AoC 2020 ; Day 3 Part 1
# Starting at the top-left corner of your map and following a slope of right 3 and down 1, 
# how many trees would you encounter?
#
#   return [char for char in word]
# 

def split(word): 
    res = [] 
    res[:] = word.rstrip()

    return res


def read_file():

    geology = []

    with open('day3/input.txt') as f:
        for line in f:
           geology.append(split(line.rstrip()))

    return geology

def count_trees(geology):
    num_trees = 0
    max_rows = len(geology)
    max_columns = len(geology[0])
    RIGHT=3
    DOWN=1
    current_column = 0
    current_row = 1 # skip first row

    while current_row < max_rows:
        current_column += RIGHT

        if (current_column >= max_columns):
            current_column = current_column - max_columns

        if (geology[current_row][current_column]) == '#':
            num_trees += 1

        current_row += DOWN

    return num_trees
 
def main():
    print(count_trees(read_file()))

if __name__ == '__main__':
    main()
