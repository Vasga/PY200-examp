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
        self.next = next_  # вызовется setter

    def __repr__(self) -> str:
        return f"Node({self.value}, {None})" if self.next is None else f"Node({self.value}, Node({self.next}))"

    def __str__(self) -> str:
        return str(self.value)

    def is_valid(self, node: Any) -> None:
        if not isinstance(node, (type(None), Node)):
            raise TypeError

    def set_next(self, next_: Optional["Node"] = None) -> None:
        self.is_valid(next_)
        self.next = next_


class DoubleLinkedNode(Node):
    """ Класс, который описывает узел двусвязного списка."""

    def __init__(self, value: Any, next_: Optional["Node"] = None, prev: Optional["Node"] = None):
        """
        Создаем новый узел двуcвязного списка
        :param prev : предыдущий узел если он есть
        """
        super().__init__(value, next_)
        self.prev = prev

    def __repr__(self) -> str:
        next_prev = None if self.prev is None else f"DoubleLinkedNode({self.prev})"
        next_repr = None if self.next is None else f"DoubleLinkedNode({self.next})"

        return f"DoubleLinkedNode({self.value}, {next_prev}, {next_repr})"

    def __str__(self) -> str:
        super().__str__()
        return str(self.value)

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, prev: Optional["Node"] = None):
        self._prev = prev


# if __name__ == "__main__":
#     f = DoubleLinkedNode(1)
#     s = DoubleLinkedNode(2)
#     t = DoubleLinkedNode(3)
#     fo = DoubleLinkedNode(4)
#
#     f.next = s
#     s.next = t
#     s.prev = f
#     t.prev = s
#     t.next = fo
#
#     print(repr(f))
#     print(repr(s))
#     print(repr(t))
