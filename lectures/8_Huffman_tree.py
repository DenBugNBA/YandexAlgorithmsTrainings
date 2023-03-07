def make_tree(description):
    tree = {"left": None, "right": None, "up": None, "type": "root"}

    current_node = tree

    for char in description:
        if char == "D":
            new_node = {"left": None, "right": None, "up": current_node, "type": "left"}

            current_node["left"] = new_node

            current_node = new_node

        elif char == "U":
            while current_node["type"] == "right":
                current_node = current_node["up"]

            current_node = current_node["up"]

            new_node = {
                "left": None,
                "right": None,
                "up": current_node,
                "type": "right",
            }

            current_node["right"] = new_node

            current_node = new_node

    return tree


def traverse_tree(root, prefix):
    # достаточно проверить одного потомка
    if root["left"] is None and root["right"] is None:
        return ["".join(prefix)]

    prefix.append("0")
    ans = traverse_tree(root["left"], prefix)
    prefix.pop()

    prefix.append("1")
    ans.extend(traverse_tree(root["right"], prefix))
    prefix.pop()

    return ans


description = "DUDDUU"

tree = make_tree(description)
print(tree, "\n")

print(traverse_tree(tree, []))
