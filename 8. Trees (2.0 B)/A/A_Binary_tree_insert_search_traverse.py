class BinarySearchTree:
    def __init__(self):
        # 0: val, 1: left, 2: right
        self.tree = [None, None, None]

    def add_node(self, num, tree):
        if tree[0] == None:
            tree[0] = num
        else:
            key = tree[0]

            if num < key:
                left = tree[1]
                if left == None:
                    tree[1] = [num, None, None]
                else:
                    self.add_node(num, left)

            elif num > key:
                right = tree[2]
                if right == None:
                    tree[2] = [num, None, None]
                else:
                    self.add_node(num, right)

    def search_node(self, num, tree):
        if tree == None or tree[0] == None:
            return False
        else:
            key = tree[0]

            if key == num:
                return True

            return self.search_node(num, tree[1]) or self.search_node(num, tree[2])

    def print_tree(self, tree, level):
        if tree[1] != None:
            self.print_tree(tree[1], level + 1)

        print(f"{level * '.'}{tree[0]}")

        if tree[2] != None:
            self.print_tree(tree[2], level + 1)


def handle_request(request, tree):
    params = request.split()

    if len(params) == 2:
        num = int(params[1])

        if params[0] == "ADD":
            if tree.search_node(num, tree.tree):
                print("ALREADY")
            else:
                tree.add_node(num, tree.tree)
                print("DONE")

        elif params[0] == "SEARCH":
            if tree.search_node(num, tree.tree):
                print("YES")
            else:
                print("NO")

    elif len(params) == 1:
        if params[0] == "PRINTTREE":
            tree.print_tree(tree.tree, 0)


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()

    tree = BinarySearchTree()

    for request in lines:
        handle_request(request, tree)
