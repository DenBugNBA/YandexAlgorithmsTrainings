def find_element(memory_struct, root, x):
    key = memory_struct[root][0]

    if key == x:
        return root

    elif x < key:
        left = memory_struct[root][1]
        if left == -1:
            return -1
        else:
            return find_element(memory_struct, left, x)

    elif x > key:
        right = memory_struct[root][2]
        if right == -1:
            return -1
        else:
            return find_element(memory_struct, right, x)
