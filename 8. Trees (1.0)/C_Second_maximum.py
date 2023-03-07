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

    def create_tree(self, numbers):
        for num in numbers[:-1]:
            self.add_node(num, self.tree)

    def count_tree_height(self, tree):
        if tree == None or tree[0] == None:
            return 0
        else:
            return 1 + max(
                self.count_tree_height(tree[1]), self.count_tree_height(tree[2])
            )

    def count_second_maximum(self, tree):
        prev_root = None
        while tree[2] != None:
            prev_root = tree[0]
            tree = tree[2]

        if tree[1] != None:
            tree = tree[1]
            while tree[2] != None:
                tree = tree[2]
            return tree[0]
        else:
            return prev_root


if __name__ == "__main__":
    numbers = list(map(int, input().split()))

    # 8
    # numbers = [7, 3, 2, 1, 9, 5, 4, 6, 8, 0]

    # 5
    # numbers = [6, 5, 0]

    # 5
    # numbers = [5, 6, 0]

    # 7
    # numbers = [7, 3, 9, 0]

    # 8
    # numbers = [7, 3, 9, 8, 0]

    # 7
    # numbers = [7, 9, 0]

    # 3
    # numbers = [7, 3, 0]

    # 6
    # numbers = [7, 3, 5, 4, 6, 0]

    # 9
    # numbers = [7, 10, 8, 9, 0]

    tree = BinarySearchTree()
    tree.create_tree(numbers)

    print(tree.count_second_maximum(tree.tree))
