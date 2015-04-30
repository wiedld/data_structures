# PROBLEM

# Given a directed graph, design an algorithm to find out whether there is a route between two nodes

###########################################################

# graph as a dictionrary.
# keys = nodes
# values = tails of arcs, directional, and the end node it heads to

graph = {'A': ['B', 'C'],
        'B': ['C', 'D'],
        'C': ['D', 'F'],
        'D': ['C'],
        'E': ['F'],
        'F': ['E']}



def find_path(graph, curr_pos, end, path=[]):

    # base cases
    if curr_pos==end:
        path.append(curr_pos)
        return path

    if end not in graph:
        return None

    # continue along all possible paths
    for node in graph[curr_pos]:

        # prevent from going in circles
        if node not in path:

            # in for loop, prevent curr pos from being added twice
            if curr_pos not in path:
                path.append(curr_pos)

            new_path = find_path(graph, node, end, path)

            if new_path:
                return new_path




# print find_path(graph, 'A', 'F')  # A->B->C->F  or A->C->F
# print find_path(graph, 'E', 'A')    # return None
print find_path(graph, 'D', 'E')    # D->C->F->E

