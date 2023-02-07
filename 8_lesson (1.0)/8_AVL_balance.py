class BinarySearchTree:
    def __init__(self):
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

    def is_avl_balanced(self, tree):
        if tree == None or tree[0] == None:
            return True

        left_height = self.count_tree_height(tree[1])
        right_height = self.count_tree_height(tree[2])

        return (
            abs(left_height - right_height) <= 1
            and self.is_avl_balanced(tree[1])
            and self.is_avl_balanced(tree[2])
        )


# numbers = list(map(int, input().split()))

# YES
numbers = [7, 3, 2, 1, 9, 5, 4, 6, 8, 0]

# YES
# numbers = [0]

# YES
# numbers = [7, 3, 9, 0]

# YES
# numbers = [7, 3, 9, 8, 0]

# YES
# numbers = [7, 9, 0]

# YES
# numbers = [7, 3, 0]

# NO
# numbers = [7, 3, 5, 4, 6, 0]

# NO
# numbers = [7, 10, 8, 9, 0]

tree = BinarySearchTree()
tree.create_tree(numbers)

if tree.is_avl_balanced(tree.tree):
    print("YES")
else:
    print("NO")
