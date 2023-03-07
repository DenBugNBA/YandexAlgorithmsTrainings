set_size = 10
myset = [[] for _ in range(set_size)]


def add(x):
    if not find(x):
        myset[x % set_size].append(x)


def find(x):
    for now in myset[x % set_size]:
        if now == x:
            return True
    return False


def delete(x):
    x_list = myset[x % set_size]
    for i in range(len(x_list)):
        if x_list[i] == x:
            x_list[i] = x_list[len(x_list) - 1]
            x_list.pop()
            return
