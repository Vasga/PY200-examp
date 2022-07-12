from typing import Iterable, Optional, Any
from collections.abc import MutableSequence

from node import Node, DoubleLinkedNode


class LinkedList(MutableSequence):
    """ Класс, который описывает узел связного списка. """

    def __init__(self, data: Iterable = None):
        """Конструктор связного списка"""
        self._len = 0
        self._head: Optional[Node] = None
        self._tail = self._head
        super().__init__()

        if data is not None:
            for value in data:
                self.append(value)

    def append(self, value: Any):
        """ Добавление элемента в конец связного списка. """
        append_node = Node(value)

        if self._head is None:
            self._head = append_node
        else:
            last_index = self._len - 1
            last_node = self.step_by_step_on_nodes(last_index)

            self.linked_nodes(last_node, append_node)

        self._len += 1

    def __len__(self):
        return self._len

    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        """
        Функция, которая связывает между собой два узла.

        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел
        """
        left_node.set_next(right_node)

    def step_by_step_on_nodes(self, index: int) -> Node:
        """ Функция выполняет перемещение по узлам до указанного индекса. И возвращает узел. """

        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self._len:  # для for
            raise IndexError()

        current_node = self._head
        for _ in range(index):
            current_node = current_node.next

        return current_node

    def __getitem__(self, index: int) -> Any:
        """ Метод возвращает значение узла по указанному индексу. """
        if not isinstance(index, int):
            raise TypeError()
        node = self.step_by_step_on_nodes(index)
        return node.value

    def __setitem__(self, index: int, value: Any) -> None:
        """ Метод устанавливает значение узла по указанному индексу. """
        if not isinstance(index, int):
            raise TypeError()
        node = self.step_by_step_on_nodes(index)
        node.value = value

    def __delitem__(self, index: int):
        """ Метод удаляет значение узла по указанному индексу. """
        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self._len:  # для for
            raise IndexError()

        if index == 0:
            self._head = self._head.next
        elif index == self._len - 1:
            tail = self.step_by_step_on_nodes(index - 1)
            tail.next = None
        else:
            prev_node = self.step_by_step_on_nodes(index - 1)
            del_node = prev_node.next
            next_node = del_node.next

            self.linked_nodes(prev_node, next_node)

        self._len -= 1

    def to_list(self) -> list:
        """ Метод который формирует  из LinkedList встроенный list"""
        return [linked_list_value for linked_list_value in self]

    def __repr__(self) -> str:
        """  Метод __repr__ который будет выводить представление LinkedList """
        return f"{self.__class__.__name__}({self.to_list()})"

    def __str__(self) -> str:
        """ Метод __str__ который будет выводить представление LinkedList"""
        return f"{self.to_list()}"

    def insert(self, index: int, value: Any) -> None:
        """ Метод вставки узла по индексу"""
        if not isinstance(index, int):
            raise TypeError()

        insert_node = Node(value)

        if index == 0:
            insert_node.next = self._head
            self._head = insert_node
            self._len += 1
        elif index >= self._len - 1:
            self.append(value)
        else:
            prev_node = self.step_by_step_on_nodes(index - 1)
            next_node = prev_node.next

            self.linked_nodes(prev_node, insert_node)
            self.linked_nodes(insert_node, next_node)

            self._len += 1


class DoubleLinkedList(LinkedList):

    @staticmethod
    def linked_nodes(left_node: DoubleLinkedNode, right_node: Optional[DoubleLinkedNode] = None) -> None:
        left_node.next = right_node
        right_node.prev = left_node

    def append(self, value: Any):
        """ Перегружаем метод добавления элемента в конец связного списка. """
        append_node = DoubleLinkedNode(value)

        if self._head is None:
            self._head = self._tail = append_node
        else:
            self.linked_nodes(self._tail, append_node)
            self._tail = append_node

        self._len += 1


if __name__ == '__main__':
    list_ = (1, 2, 3, 7, 9, 10)
    linked_list = DoubleLinkedList(list_)
    print(repr(linked_list))

    linked_list.insert(0, 0)
    print(repr(linked_list))

    linked_list.append(88)
    print(repr(linked_list))

    linked_list.__setitem__(0, 22)
    print(repr(linked_list))

    linked_list.__delitem__(0)
    print(repr(linked_list))

