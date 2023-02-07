class BinarySearchTree:
    def __init__(self):
        self.tree = [None, None, None]

    def add_node(self, num, tree, level):
        level += 1

        if tree[0] == None:
            tree[0] = num

        elif tree[0] == num:
            return None

        else:
            key = tree[0]

            if num < key:
                left = tree[1]
                if left == None:
                    tree[1] = [num, None, None]
                    return level + 1
                else:
                    level = self.add_node(num, left, level)

            elif num > key:
                right = tree[2]
                if right == None:
                    tree[2] = [num, None, None]
                    return level + 1
                else:
                    level = self.add_node(num, right, level)

        return level

    def create_tree(self, numbers):
        levels = []

        for num in numbers[:-1]:
            level = 0
            res_level = self.add_node(num, self.tree, level)
            if res_level:
                levels.append(res_level)

        return levels

    def count_tree_height(self, tree):
        if tree == None or tree[0] == None:
            return 0
        else:
            return 1 + max(
                self.count_tree_height(tree[1]), self.count_tree_height(tree[2])
            )


# numbers = list(map(int, input().split()))

# 1 2 3 4 2 3 4 4 3
numbers = [7, 3, 2, 1, 9, 5, 4, 6, 8, 0]

#
# numbers = [0]

# 1 2 3 4
# numbers = [6, 5, 4, 3, 0]

# 1 2
# numbers = [6, 5, 6, 6, 6, 0]

tree = BinarySearchTree()
levels = tree.create_tree(numbers)
print(*levels)
