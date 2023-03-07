def create_ancestors_set(name, tree):
    ancestors_set = set()

    while name in tree:
        ancestors_set.add(name)
        name = tree[name]

    ancestors_set.add(name)

    return ancestors_set


def find_lowest_common_ancestor(first_name, second_name, tree):
    first_ancestors = create_ancestors_set(first_name, tree)

    current_search_name = second_name

    while current_search_name not in first_ancestors:
        current_search_name = tree[current_search_name]

    return current_search_name


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()

    n = int(lines[0])

    tree = {}

    for i in range(1, n):
        descendant, ancestor = lines[i].split()

        tree[descendant] = ancestor

    for i in range(n, len(lines)):
        first_name, second_name = lines[i].split()

        print(find_lowest_common_ancestor(first_name, second_name, tree))
