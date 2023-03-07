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


# освободить память
def del_node(memory_struct, index):
    memory, first_free = memory_struct

    # заменяем в удаляемом элементе следующий на первый свободный
    memory[index][1] = first_free

    # первый свободный - тот, что освободился
    memory_struct[1] = index
