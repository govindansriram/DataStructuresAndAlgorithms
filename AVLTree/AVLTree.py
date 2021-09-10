from typing import Optional


class Node:

    def __init__(self, data):
        self.__data = data
        self.height = 1
        self.right = None
        self.left = None

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data


def insert_node(root: Node,
                data) -> Node:
    if root is None:
        return Node(data)

    elif data > root.get_data():
        root.right = insert_node(root.right, data)

    else:
        root.left = insert_node(root.left, data)

    root.height = (1 + max(get_height(root.right), get_height(root.left)))

    balance_level = get_balance_val(root)

    if balance_level < -1 and data > root.right.get_data():
        return rotate_left(root)

    if balance_level > 1 and data < root.left.get_data():
        return rotate_right(root)

    if balance_level > 1 and data > root.left.get_data():
        root.left = rotate_left(root.left)
        return rotate_right(root)

    if balance_level < -1 and data < root.right.get_data():
        root.right = rotate_right(root.right)
        return rotate_left(root)

    return root


def delete_node(root: Node,
                data) -> Optional[Node]:
    if root is None:
        return None
    elif data > root.get_data():
        root.right = delete_node(root.right, data)
    elif data < root.get_data():
        root.left = delete_node(root.left, data)
    else:
        if root.right is None:
            temp = root.left
            root = None
            return temp

        if root.left is None:
            temp = root.right
            root = None
            return temp

        new_node = get_max_left(root.left)
        root.set_data(new_node.get_data())
        root.left = delete_node(root.left, new_node.get_data())

    if root is None:
        return None

    root.height = 1 + max(get_height(root.right), get_height(root.left))

    balance_val = get_balance_val(root)

    if balance_val > 1:

        if get_balance_val(root.left) >= 0:
            root = rotate_right(root)
            return root

        root.left = rotate_left(root.left)
        return rotate_right(root)

    if balance_val < -1:

        if get_balance_val(root.right) <= 0:
            root = rotate_left(root)
            return root

        root.right = rotate_right(root.right)
        return rotate_left(root)

    return root


def get_balance_val(root: Node) -> int:
    if root is None:
        return 0

    return get_height(root.left) - get_height(root.right)


def get_max_left(root: Node) -> Optional[Node]:
    if root is None:
        return None
    elif root.right is None:
        return root
    else:
        return get_max_left(root.right)


def get_height(node: Node) -> int:
    return node.height if node is not None else 0


def rotate_left(root: Node):
    new_root = root.right
    new_right = root.right.left

    new_root.left = root
    root.right = new_right

    root.height = (1 + max(get_height(root.left), get_height(root.right)))
    new_root.height = (1 + max(get_height(new_root.left), get_height(new_root.right)))

    return new_root


def rotate_right(root: Node):
    new_root = root.left
    new_left = root.left.right

    new_root.right = root
    root.left = new_left

    root.height = (1 + max(get_height(root.left), get_height(root.right)))
    new_root.height = (1 + max(get_height(new_root.left), get_height(new_root.right)))

    return new_root


def print_level_order(root: Node):
    h = get_height(root)
    for i in range(1, h + 1):
        print_current_level(root, i)


def print_current_level(root: Node, level):
    if root is None:
        return
    if level == 1:
        print(root.get_data(), end=" ")
    elif level > 1:
        print_current_level(root.left, level - 1)
        print_current_level(root.right, level - 1)