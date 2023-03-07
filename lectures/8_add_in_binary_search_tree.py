def init_memory(max_n):
    memory = []

    for i in range(max_n):
        # ключ, левый сын, правый сын
        memory.append([0, i + 1, 0])
        # менеджер памяти использует поле "левый сын"
        # для указания на следующий элемент списка.
        # правый сын не используется.

    # массив, указатель на первый свободный элемент
    return [memory, 0]


# выделить память
def new_node(memory_struct):
    memory, first_free = memory_struct

    # первый свободный элемент заменяется на следующий элемент
    memory_struct[1] = memory[first_free][1]

    # возвращаем старый первый свободный элемент, который до этого запомнили
    return first_free


def create_and_fill_node(memory_struct, key):
    index = new_node(memory_struct)

    memory_struct[0][index][0] = key
    memory_struct[0][index][1] = -1
    memory_struct[0][index][2] = -1

    return index


def add(memory_struct, root, x):
    key = memory_struct[0][root][0]

    if x < key:
        left = memory_struct[0][root][1]
        if left == -1:
            memory_struct[0][root][1] = create_and_fill_node(memory_struct, x)
        else:
            add(memory_struct, left, x)

    elif x > key:
        right = memory_struct[0][root][2]
        if right == -1:
            memory_struct[0][root][2] = create_and_fill_node(memory_struct, x)
        else:
            add(memory_struct, right, x)


memory_struct = init_memory(20)
print(memory_struct, end="\n\n")
root = create_and_fill_node(memory_struct, 8)

add(memory_struct, root, 10)
add(memory_struct, root, 9)
add(memory_struct, root, 14)
add(memory_struct, root, 13)
add(memory_struct, root, 3)
add(memory_struct, root, 1)
add(memory_struct, root, 6)
add(memory_struct, root, 4)
add(memory_struct, root, 7)

print(memory_struct)

#  8
#  /\
# _  10
#    /\
#   9  14
