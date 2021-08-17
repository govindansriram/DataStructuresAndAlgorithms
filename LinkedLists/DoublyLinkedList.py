from LinkedLists.Node import Node


class DoublyLinkedList:

    def __init__(self, data):
        self.__length = 1
        self.__head = Node(data)
        self.__tail = self.__head

    def get_head(self) -> Node:
        return self.__head

    def get_tail(self) -> Node:
        return self.__tail

    def get_length(self) -> int:
        return self.__length

    def insert_at_head(self,
                       data):

        new_node = Node(data)
        new_node.set_right_node(self.__head)
        self.__head.set_left_node(new_node)
        self.__head = new_node

        self.__length += 1

    def insert_at_tail(self,
                       data):

        new_node = Node(data)
        new_node.set_left_node(self.__tail)
        self.__tail.set_right_node(new_node)
        self.__tail = new_node

        self.__length += 1

    def insert_at_index(self,
                        index,
                        data):

        if index == 0:
            self.insert_at_head(data)

        if index > self.__length - 1:
            self.insert_at_tail(data)

        else:
            new_node = Node(data)
            idx = 0
            curr_node = self.__head

            while idx < index:
                if curr_node.get_right_node() is None:
                    break
                curr_node = curr_node.get_right_node()

                idx += 1

            left_curr = curr_node.get_left_node()
            left_curr.set_right_node(new_node)
            new_node.set_right_node(curr_node)
            new_node.set_left_node(left_curr)
            curr_node.set_left_node(new_node)

            self.__length += 1

    def iterate_forward(self):
        curr_node = self.__head

        while True:
            yield curr_node.get_data()
            if curr_node.get_right_node() is None:
                break

            curr_node = curr_node.get_right_node()

    def iterate_backward(self):
        curr_node = self.__tail

        while True:
            yield curr_node.get_data()
            if curr_node.get_left_node() is None:
                break

            curr_node = curr_node.get_left_node()
