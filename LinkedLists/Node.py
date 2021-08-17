class Node:

    def __init__(self,
                 data):
        self.__data = data
        self.__left_node = None
        self.__right_node = None

    def get_data(self):
        return self.__data

    def set_left_node(self, left_node):
        self.__left_node = left_node

    def set_right_node(self, right_node):
        self.__right_node = right_node

    def get_left_node(self):
        return self.__left_node

    def get_right_node(self):
        return self.__right_node
