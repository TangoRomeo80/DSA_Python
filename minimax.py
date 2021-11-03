import math


def minimax(node_index, depth, is_max, values, target_depth):
    if depth == target_depth:
        return values[node_index]
    elif is_max:
        return max(minimax(node_index * 2, depth + 1, False, values, target_depth),
                   minimax((node_index * 2) + 1, depth + 1, False, values, target_depth))
    else:
        return min(minimax(node_index * 2, depth + 1, True, values, target_depth),
                   minimax((node_index * 2) + 1, depth + 1, True, values, target_depth),)


values_list = [3, 5, 6, 9, 1, 2, 0, -1]
tree_target_depth = math.log2(len(values_list))

print(f'Optimal value is: {minimax(0, 0, True, values_list, tree_target_depth)}')
