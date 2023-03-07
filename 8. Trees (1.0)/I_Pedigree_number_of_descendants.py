import sys


def find_progenitor(tree):
    candidates = list(tree.keys())

    for descendants in tree.values():
        for descendant in descendants:
            if descendant in candidates:
                candidates.remove(descendant)

    return candidates[0]


def count_descendants(tree, progenitor, descendants_count):
    descendants_count[progenitor] = 0

    if progenitor not in tree:
        return 0

    current_progenitor_count = 0

    for descendant in tree[progenitor]:
        current_progenitor_count += (
            count_descendants(tree, descendant, descendants_count) + 1
        )

    descendants_count[progenitor] += current_progenitor_count

    return current_progenitor_count


if __name__ == "__main__":
    sys.setrecursionlimit(100000)

    n = int(input())
    tree = {}
    for i in range(n - 1):
        descendant, ancestor = input().split()
        if ancestor not in tree:
            tree[ancestor] = []
        tree[ancestor].append(descendant)

    # Alexander_I 0
    # Alexei 1
    # Anna 4
    # Elizabeth 0
    # Nicholaus_I 0
    # Paul_I 2
    # Peter_I 8
    # Peter_II 0
    # Peter_III 3
    # n = 9
    # tree = {
    #     "Peter_I": ["Alexei", "Anna", "Elizabeth"],
    #     "Alexei": ["Peter_II"],
    #     "Anna": ["Peter_III"],
    #     "Peter_III": ["Paul_I"],
    #     "Paul_I": ["Alexander_I", "Nicholaus_I"],
    # }

    if n != 0:
        progenitor = find_progenitor(tree)

        descendants_count = {}
        count_descendants(tree, progenitor, descendants_count)

        for ancestor, count in sorted(descendants_count.items()):
            print(f"{ancestor} {count}")
