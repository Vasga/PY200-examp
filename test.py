import unittest

from node import DoubleLinkedNode, Node
from main import DoubleLinkedList


class TestCaseDoubleNode(unittest.TestCase):
    """

    """

    def test_init_dnode_without_next(self):
        """Проверить следующий узел после инициализации с аргументом next_ по умолчанию"""

        db_node = DoubleLinkedNode("node_without_next")
        msg = "Значение следующего узла по умолчанию должно быть None"
        self.assertIsNone(db_node.next, msg)

    def test_init_dnode_without_prev(self):
        """Проверить следующий узел после инициализации с аргументом prev по умолчанию"""

        db_node = DoubleLinkedNode("node_without_prev")
        msg = "Значение предыдущего узла по умолчанию должно быть None"
        self.assertIsNone(db_node.prev, msg)

    def test_init_node_with_next(self):
        """Проверить следующий узел после инициализации с переданным аргументом next_"""
        first_node = DoubleLinkedNode("right")
        second_node = DoubleLinkedNode("left", first_node)

        msg = "Значение следующего при инициализации некорректно"
        self.assertEqual(repr(second_node.next), repr(first_node), msg)

    def test_init_node_with_prev(self):
        """Проверить следующий узел после инициализации с переданным аргументом prev"""

        first_node = DoubleLinkedNode(1)
        second_node = DoubleLinkedNode(2)
        third_node = DoubleLinkedNode(3)

        first_node.next = second_node
        second_node.next = third_node
        second_node.prev = first_node
        third_node.prev = second_node
        msg = "Значение предыдущего узла при инициализации некорректно"
        self.assertEqual(repr(third_node.prev), repr(DoubleLinkedNode(2, third_node, first_node)), msg)

    def test_repr_node_without_next(self):
        """Проверить метод __repr__, для случая когда нет следующего  и предыдущего узла"""
        db_node = DoubleLinkedNode("node_without_next_prev")

        msg = "Значение представления __repr__ некорректно для узла без следующего и предыдущего узла. "
        self.assertEqual(repr(db_node), "DoubleLinkedNode(node_without_next_prev, None, None)", msg)

    def test_str(self):
        some_value = 5
        db_node = DoubleLinkedNode(some_value)

        self.assertEqual(str(db_node), str(some_value))


class TestCaseDoubleLinkedList(unittest.TestCase):
    """

    """
