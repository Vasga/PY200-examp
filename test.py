import unittest

from node import DoubleLinkedNode
from main import DoubleLinkedList


class TestCaseDoubleNode(unittest.TestCase):
    """
    Проверка методов класса DoubleLinkedNode
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
    """ Проверка методов класса DoubleLinkedList """

    def test_repr_db_list(self):
        """ Проверка метода __repr__ DoubleLinkedList """
        list_ = (1, 2, 3)
        db_list = DoubleLinkedList(list_)
        msg = "Значение представления  __repr__ для двусвязного списка не соответствует"
        self.assertEqual(repr(db_list), "DoubleLinkedList([1, 2, 3])", msg)

    def test_str_db_list(self):
        """ Проверка метода __str__ DoubleLinkedList """
        list_ = (1, 2, 3)
        db_list = DoubleLinkedList(list_)
        msg = "Значение представления  __str__ для двусвязного списка не соответствует"
        self.assertEqual(str(db_list), "[1, 2, 3]", msg)

    def test_getitem_db_list(self):
        """   """
        list_ = (1, 2, 3)
        db_list = DoubleLinkedList(list_)
        index = 2
        msg = "Значение представления  __getitem__ для двусвязного списка не соответствует"
        self.assertEqual(db_list.__getitem__(index), db_list[index], msg)

    def test_delitem_db_list(self):
        """ Проверка метода __delitem__ DoubleLinkedList"""
        list_ = (1, 2, 3)
        db_list = DoubleLinkedList(list_)
        db_list.__delitem__(2)
        msg = "Удаление элемента  не произошло"
        self.assertNotEqual(len(db_list), len(list_), msg)

    def test_setitem_db_list(self):
        """ Проверка метода __setitem__ DoubleLinkedList"""
        val = "wow"
        ind = 0
        list_ = (1, 2, 3)
        db_list = DoubleLinkedList(list_)
        db_list.__setitem__(ind, val)
        self.assertEqual(db_list[ind], val, msg="Изменения элемента не соответствует заданному значению")


if __name__ == '__main__':
    unittest.main()
