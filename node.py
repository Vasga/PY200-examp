from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """
        self.value = value
        self.next = next_

    def __repr__(self) -> str:
        """ Метод __repr__"""
        return f"Node({self.value}, {None})" if self.next is None else f"Node({self.value}, Node({self.next}))"

    def __str__(self) -> str:
        """ Метод __str__"""
        return str(self.value)

    def is_valid(self, node: Any) -> None:
        """ Метод проверки корректности связываемого узла """
        if not isinstance(node, (type(None), Node)):
            raise TypeError

    def set_next(self, next_: Optional["Node"] = None) -> None:
        """ Метод должен проверять корректность узла и устанавливать значение атрибуту next"""
        self.is_valid(next_)
        self.next = next_

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_node):
        self.is_valid(next_node)
        self._next = next_node


class DoubleLinkedNode(Node):
    """ Класс, который описывает узел двусвязного списка."""

    def __init__(self, value: Any, next_: Optional["Node"] = None, prev: Optional["Node"] = None):
        """
        Создаем новый узел двуcвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        :param prev : предыдущий узел если он есть
        """
        super().__init__(value, next_)
        self._prev = prev

    def __repr__(self) -> str:
        """  Перегружаем метод __repr__"""
        next_prev = None if self.prev is None else f"DoubleLinkedNode({self.prev})"
        next_repr = None if self.next is None else f"DoubleLinkedNode({self.next})"

        return f"DoubleLinkedNode({self.value}, {next_prev}, {next_repr})"

    def __str__(self) -> str:
        """ Метод __str__"""
        return str(self.value)

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, prev: Optional["Node"] = None):
        self._prev = prev
        self.is_valid(prev)


if __name__ == "__main__":

    first_node = DoubleLinkedNode(1)
    second_node = DoubleLinkedNode(2)
    third_node = DoubleLinkedNode(3)
    fourth_node = DoubleLinkedNode(4)

    first_node.next = second_node
    second_node.next = third_node
    second_node.prev = first_node
    third_node.prev = second_node
    third_node.next = fourth_node
    fourth_node.prev = third_node

    print(repr(first_node))
    print(repr(second_node))
    print(repr(third_node))
    print(repr(fourth_node))

