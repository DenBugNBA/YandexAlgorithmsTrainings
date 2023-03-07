import sys


def find_progenitor(tree):
    candidates = list(tree.keys())

    for descendants in tree.values():
        for descendant in descendants:
            if descendant in candidates:
                candidates.remove(descendant)

    return candidates[0]


def count_levels(tree, progenitor, descendants_count, levels_count, current_level):
    levels_count[progenitor] = current_level

    if progenitor not in tree:
        return

    for descendant in tree[progenitor]:
        count_levels(
            tree, descendant, descendants_count, levels_count, current_level + 1
        )


if __name__ == "__main__":
    sys.setrecursionlimit(100000)

    n = int(input())
    tree = {}
    for i in range(n - 1):
        descendant, ancestor = input().split()
        if ancestor not in tree:
            tree[ancestor] = []
        tree[ancestor].append(descendant)

    # Alexander_I 4
    # Alexei 1
    # Anna 1
    # Elizabeth 1
    # Nicholaus_I 4
    # Paul_I 3
    # Peter_I 0
    # Peter_II 2
    # Peter_III 2
    # n = 9
    # tree = {
    #     "Peter_I": ["Alexei", "Anna", "Elizabeth"],
    #     "Alexei": ["Peter_II"],
    #     "Anna": ["Peter_III"],
    #     "Peter_III": ["Paul_I"],
    #     "Paul_I": ["Alexander_I", "Nicholaus_I"],
    # }

    # AQHFYP 3
    # AYKOTYQ 2
    # IWCGKHMFM 1
    # MJVAURUDN 2
    # MKFXCLZBT 2
    # PUTRIPYHNQ 2
    # QIUKGHWCDC 1
    # UQNGAXNP 1
    # WPLHJL 0
    # YURTPJNR 2
    # n = 10
    # tree = {
    #     "MKFXCLZBT": ["AQHFYP"],
    #     "QIUKGHWCDC": ["AYKOTYQ", "MJVAURUDN", "YURTPJNR"],
    #     "WPLHJL": ["IWCGKHMFM", "QIUKGHWCDC", "UQNGAXNP"],
    #     "IWCGKHMFM": ["MKFXCLZBT"],
    #     "UQNGAXNP": ["PUTRIPYHNQ"],
    # }

    # BFNRMLH 3
    # CSZMPFXBZ 2
    # FMVQTU 9
    # FUXATQUGIG 8
    # GNVIZ 6
    # IHWBQDJ 1
    # IQGIGUJZ 5
    # IRVAVMQKN 7
    # JMUPNYRQD 4
    # LACXYFQHSQ 0
    # n = 10
    # tree = {
    #     "CSZMPFXBZ": ["BFNRMLH"],
    #     "IHWBQDJ": ["CSZMPFXBZ"],
    #     "FUXATQUGIG": ["FMVQTU"],
    #     "IRVAVMQKN": ["FUXATQUGIG"],
    #     "IQGIGUJZ": ["GNVIZ"],
    #     "LACXYFQHSQ": ["IHWBQDJ"],
    #     "JMUPNYRQD": ["IQGIGUJZ"],
    #     "GNVIZ": ["IRVAVMQKN"],
    #     "BFNRMLH": ["JMUPNYRQD"],
    # }

    if n != 0:
        progenitor = find_progenitor(tree)

        levels_count = {}
        count_levels(tree, progenitor, levels_count, levels_count, 0)

        for name, level in sorted(levels_count.items()):
            print(f"{name} {level}")
