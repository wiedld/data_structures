# PROBLEM

# Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column is set to 0

#######################################

# e.g. input: [[1,1,1,1],[1,0,1,1],[[1,1,1,1]]
#  indexes: [[00,01,02,03],[10,11,12,13],[20,21,22,23]]

# e.g. output:  [[1,0,1,1],[0,0,0,0],[[1,0,1,1]]
#   indexes:  anything with the same x of y of the original

# steps:
    # 1 - get list of x coordinate, and y coordinates.
    #     - use sets, to save on lookup time.  unique items ok.
    #     - look at each (x,y) only once --> O(n * m)
    # 2 - build a list of coordinates to change.
    #      - worst case, --> O(n * m). if all x and y are there.
    #      - but avg case is likely less
    # 3 - change the coordinates of those that have an x in x_set, and y in y_set
    #   use indexing to directly change value
    #      - worst case, --> O(n * m)
    #      - but avg case is likely less
    # worst case is 3(n * m).  avg can be alot less.

# alternative method for steps 2 and 3 (in combo), is to run through everything again and see if the x,y coord has an x in set_x or a y in set_y
    # lookup time is O(1) for each set. --> O(m * n) * 0(2) = m * n
    # so the total time of all steps = 2(n * m)

# used alternative method


def change_to_zeros(matrix):
    set_x_coord, set_y_coord = find_coord_w_zero(matrix)
    result = change_matrix(matrix, set_x_coord, set_y_coord)

    return result



def find_coord_w_zero(matrix):
    set_x, set_y = set(), set()

    N = len(matrix)
    M = len(matrix[0])

    for x in range(N):
        for y in range(M):
            if matrix[x][y] == 0:
                set_x.add(x)
                set_y.add(y)

    return set_x, set_y



def change_matrix(matrix, x_coord, y_coord):
    N = len(matrix)
    M = len(matrix[0])

    for x in range(N):
        for y in range(M):
            if (x in x_coord) or (y in y_coord):
                matrix[x][y] = 0

    return matrix



test = [[1,1,1,1],[1,0,1,1],[1,1,1,1]]
print change_to_zeros(test)

