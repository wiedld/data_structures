# PROBLEM
# Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees Can you do this in place?

###################################

# e.g. input: [[A,B,C,D],[E,F,G,H],[I,J,K,L],[M,N,O,P]]
#  indexes: [[00,01,02,03],[10,11,12,13],[20,21,22,23],[30,31,32,33]]

# e.g. output:  [[M,I,E,A],[N,J,F,B],[O,K,G,C],[P,L,H,D]]
#   indexes:  [[30,20,10,00],[31,21,11,01],[32,22,12,02],[33,32,13,03]]

# steps:
    # - take last nested list (index -1) e.g. [30,31,32,33]
    # - add to new nested list, with index and append one to each sublist
    # - pop last nested list from original
    # - repeated until entire original list is empty
    # - recursion.  base case = empty

# bigO. time. O(n), because indexing to each value directly, and only once.
# bigO. space. 1 extra list. constant


def rotate_matrix_90(matrix):
    output = make_output(matrix)

    return rotate_matrix(matrix,output)



def rotate_matrix(matrix,output):

    # base case
    if len(matrix) == 0:
        return output

    sublist = matrix.pop(-1)
    # extend list with values from sublist
    for idx in range(len(sublist)):
        output[idx].extend( [sublist[idx]] )

    return rotate_matrix(matrix, output)



def make_output(matrix):
    # is an NxN matrix.  just need length.
    N = len(matrix)
    output = []
    for idx in range(N):
        output.append([])
    return output


# TEST
test = [["A","B","C","D"],["E","F","G","H"],["I","J","K","L"],["M","N","O","P"]]
print rotate_matrix_90(test)

