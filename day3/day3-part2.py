#
# AoC 2020 ; Day 3 Part 2
# What do you get if you multiply together the number of trees encountered on each of the listed slopes?
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

def count_trees(geology, right, down):
    num_trees = 0
    max_rows = len(geology)
    max_columns = len(geology[0])
    current_column = 0
    current_row = down # skip first row(s)

    while current_row < max_rows:
        current_column += right

        if (current_column >= max_columns):
            current_column = current_column - max_columns

        if (geology[current_row][current_column]) == '#':
            num_trees += 1

        current_row += down

    print(num_trees)

    return num_trees
 
def determine_alternates(geology):
    all_trees = 1
    alternatives = [(1,1), (3,1), (5,1), (7,1), (1,2)] # (RIGHT, DOWN)

    for alternative in alternatives:
        all_trees *= count_trees(geology, right=alternative[0], down=alternative[1])

    return all_trees

def main():
    print(f"All trees: {determine_alternates(read_file())}")

if __name__ == '__main__':
    main()
