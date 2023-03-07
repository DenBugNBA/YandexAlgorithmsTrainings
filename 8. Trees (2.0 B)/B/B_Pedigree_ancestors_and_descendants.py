from collections import deque


def find_progenitor(tree):
    candidates = list(tree.keys())

    for descendants in tree.values():
        for descendant in descendants:
            if descendant in candidates:
                candidates.remove(descendant)

    return candidates[0]


def find_descendant(ancestor_name, target_descendant, tree):
    candidates = deque([ancestor_name])

    while candidates:
        current_ancestor = candidates.popleft()

        if current_ancestor in tree:
            for descendant in tree[current_ancestor]:
                if descendant == target_descendant:
                    return True

                candidates.append(descendant)

    return False


def is_descendant_or_ancestor(first_name, second_name, tree):
    if find_descendant(first_name, second_name, tree):
        return 1

    if find_descendant(second_name, first_name, tree):
        return 2

    return 0


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()

    n = int(lines[0])

    tree = {}

    for i in range(1, n):
        descendant, ancestor = lines[i].split()

        if ancestor not in tree:
            tree[ancestor] = []
        tree[ancestor].append(descendant)

    for i in range(n, len(lines)):
        first_name, second_name = lines[i].split()
        print(is_descendant_or_ancestor(first_name, second_name, tree))
