from LinkedLists.Node import Node


class DoublyLinkedList:

    def __init__(self):
        self.__length = 0

        self.__ghost_head = Node(None)
        self.__ghost_tail = Node(None)

        self.__ghost_head.set_right_node(self.__ghost_tail)
        self.__ghost_tail.set_left_node(self.__ghost_head)

    def get_head(self) -> Node:
        return self.__ghost_head.get_right_node()

    def get_tail(self) -> Node:
        return self.__ghost_tail.get_left_node()

    def get_length(self) -> int:
        return self.__length

    def insert_at_head(self,
                       data):

        head_node = self.__ghost_head.get_right_node()
        new_node = Node(data)
        new_node.set_right_node(head_node)
        head_node.set_left_node(new_node)
        self.__ghost_head.set_right_node(new_node)
        new_node.set_left_node(self.__ghost_head)
        self.__length += 1

    def cut_tail(self):
        if self.get_length() > 0:
            tail_node = self.__ghost_tail.get_left_node()
            new_tail = tail_node.get_left_node()
            new_tail.set_right_node(self.__ghost_tail)
            self.__ghost_tail.set_left_node(new_tail)

            del tail_node
            self.__length -= 1
        else:
            raise Exception("LinkedList is empty, unable to delete tail")

    def decapitate(self):
        if self.get_length() > 0:
            head_node = self.__ghost_head.get_right_node()
            new_head = head_node.get_right_node()
            new_head.set_left_node(self.__ghost_head)
            self.__ghost_head.set_right_node(new_head)

            del head_node
            self.__length -= 1
        else:
            raise Exception("LinkedList is empty, unable to delete head")

    def cut_at_index(self,
                     index):

        if index == 0:
            self.decapitate()

        elif index >= self.__length - 1:
            self.cut_tail()

        else:
            middle = self.__length // 2
            curr_node = None

            if index <= middle:
                idx = 0
                curr_node = self.get_head()
                for curr_idx, curr_node in enumerate(self.iterate_forward(self.__length)):
                    if idx + curr_idx >= index:
                        break

            if index > middle:
                idx = self.__length - 1
                for curr_idx, curr_node in enumerate(self.iterate_backward(self.__length)):
                    if idx - curr_idx <= index:
                        break

            left_curr = curr_node.get_left_node()
            right_curr = curr_node.get_right_node()
            left_curr.set_right_node(right_curr)
            right_curr.set_left_node(left_curr)
            del curr_node
            self.__length -= 1

    def insert_at_tail(self,
                       data):

        tail_node = self.__ghost_tail.get_left_node()
        new_node = Node(data)
        new_node.set_left_node(tail_node)
        tail_node.set_right_node(new_node)
        self.__ghost_tail.set_left_node(new_node)
        new_node.set_right_node(self.__ghost_tail)
        self.__length += 1

    def insert_at_index(self,
                        index,
                        data):

        if index == 0:
            self.insert_at_head(data)

        elif index > self.__length - 1:
            self.insert_at_tail(data)

        else:
            middle = self.__length // 2
            new_node = Node(data)
            curr_node = None

            if index <= middle:
                idx = 0
                for curr_idx, curr_node in enumerate(self.iterate_forward(self.__length)):
                    if idx + curr_idx >= index:
                        break

            else:
                idx = self.__length - 1
                for curr_idx, curr_node in enumerate(self.iterate_backward(self.__length)):
                    if idx - curr_idx <= index:
                        break

            left_curr = curr_node.get_left_node()
            left_curr.set_right_node(new_node)
            new_node.set_right_node(curr_node)
            new_node.set_left_node(left_curr)
            curr_node.set_left_node(new_node)

            self.__length += 1

    def chain_list_at_head(self,
                           new_list):

        self.__length += new_list.get_length()

        new_head = new_list.get_head()
        new_tail = new_list.get_tail()

        new_tail.set_right_node(self.get_head())
        self.get_head().set_left_node(new_tail)

        self.__ghost_head.set_right_node(new_head)
        new_head.set_left_node(self.__ghost_head)

    def chain_list_at_tail(self, new_list):

        self.__length += new_list.get_length()

        new_head = new_list.get_head()
        new_tail = new_list.get_tail()

        new_head.set_left_node(self.get_tail())
        self.get_tail().set_right_node(new_head)

        self.__ghost_tail.set_left_node(new_tail)
        new_tail.set_right_node(self.__ghost_tail)

    def chain_list_at_index(self,
                            new_list,
                            index):

        if index == 0:
            self.chain_list_at_head(new_list)
        elif index > self.__length - 1:
            self.chain_list_at_tail(new_list)
        else:
            middle = self.__length // 2
            curr_node = None

            if index <= middle:
                idx = 0
                for curr_idx, curr_node in enumerate(self.iterate_forward(self.__length)):
                    if idx + curr_idx >= index:
                        break

            else:
                idx = self.__length - 1
                for curr_idx, curr_node in enumerate(self.iterate_backward(self.__length)):
                    if idx - curr_idx <= index:
                        break

            left_curr = curr_node.get_left_node()
            new_head = new_list.get_head()
            new_tail = new_list.get_tail()

            left_curr.set_right_node(new_head)
            new_head.set_left_node(left_curr)
            new_tail.set_right_node(curr_node)
            curr_node.set_left_node(new_tail)

    def iterate_forward(self,
                        link_count,
                        start_node=None):

        curr_node = start_node if start_node is not None else self.get_head()

        link_step = 0

        while link_step < link_count:
            yield curr_node
            if curr_node.get_right_node() == self.__ghost_tail:
                break

            curr_node = curr_node.get_right_node()
            link_step += 1

    def iterate_backward(self,
                         link_count,
                         start_node=None):

        curr_node = start_node if start_node is not None else self.get_tail()

        link_step = 0

        while link_step < link_count:
            yield curr_node
            if curr_node.get_left_node() == self.__ghost_head:
                break

            curr_node = curr_node.get_left_node()
            link_step += 1
