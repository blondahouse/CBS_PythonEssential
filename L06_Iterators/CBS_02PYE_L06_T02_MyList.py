"""
Пример реализации списка с итератором
"""


class MyList:
    """Класс списка"""

    class _ListNode:
        """Внутренний класс элемента списка"""

        # По умолчанию атрибуты-данные хранятся в словаре __dict__.
        # Если возможность динамически добавлять новые атрибуты
        # не требуется, можно заранее их описать, что более
        # эффективно с точки зрения памяти и быстродействия, что
        # особенно важно, когда создаётся множество экземляров
        # данного класса.
        __slots__ = ('value', 'prev', 'next')

        def __init__(self, value, prev=None, next=None):
            self.value = value
            self.prev = prev
            self.next = next

        def __repr__(self):
            return 'MyList._ListNode({}, {}, {})'.format(self.value, id(self.prev), id(self.next))

    class _Iterator:
        """Внутренний класс итератора"""

        def __init__(self, list_instance):
            self._list_instance = list_instance
            self._next_node = list_instance._head

        def __iter__(self):
            return self

        def __next__(self):
            if self._next_node is None:
                raise StopIteration

            value = self._next_node.value
            self._next_node = self._next_node.next

            return value

    def __init__(self, iterable=None):
        # Длина списка
        self._length = 0
        # Первый элемент списка
        self._head = None
        # Последний элемент списка
        self._tail = None

        # Добавление всех переданных элементов
        if iterable is not None:
            for element in iterable:
                self.append(element)

    def append(self, element):
        """Добавление элемента в конец списка"""

        # Создание элемента списка
        node = MyList._ListNode(element)

        if self._tail is None:
            # Список пока пустой
            self._head = self._tail = node
        else:
            # Добавление элемента
            self._tail.next = node
            node.prev = self._tail
            self._tail = node

        self._length += 1

    def clean(self):
        self._head = self._tail = None

    def insert(self, index, element):

        node = MyList._ListNode(element)

        if self._tail is None:
            self._head = self._tail = node
        else:
            if index >= self._length:
                self.append(element)
            else:
                if index == 0:
                    self._head.prev = node
                    node.next = self._head
                    self._head = node
                else:
                    index = index if index > 0 else self._length - (-index) % self._length
                    el = self._head
                    for _ in range(index - 1):
                        el = el.next

                    node.prev = el
                    node.next = el.next
                    node.next.prev = node
                    el.next = node
                self._length += 1

    def pop(self):
        """Удаление элемента в конце списка"""

        value_to_return = None
        if self._tail is None:
            self._head = self._tail = None
        else:
            value_to_return = self._tail.value
            self._tail = self._tail.prev
            self._tail.next = None
            self._length -= 1
        return value_to_return

    def remove(self, index):

        if self._tail is None:
            self._head = self._tail = None
        else:
            if index >= self._length - 1:
                self.pop()
            else:
                if index == 0:
                    self._head = self._head.next
                    self._head.prev = None
                else:
                    index = index if index > 0 else self._length - (-index) % self._length
                    el = self._head
                    for _ in range(index):
                        el = el.next

                    el.prev.next = el.next
                    el.next.prev = el.prev
                self._length -= 1

    def __len__(self):
        return self._length

    def __repr__(self):
        # Метод join класса str принимает последовательность строк
        # и возвращает строку, в которой все элементы этой
        # последовательности соединены изначальной строкой.
        # Функция map применяет заданную функцию ко всем элементам последовательности.
        return 'MyList([{}])'.format(', '.join(map(repr, self)))

    def __str__(self):
        return '[{}]'.format(', '.join(map(str, self)))

    def __getitem__(self, index):
        if not 0 <= index < len(self):
            raise IndexError('list index out of range')

        node = self._head
        for _ in range(index):
            node = node.next

        return node.value

    def __iter__(self):
        return MyList._Iterator(self)


def main():
    # Создание списка
    my_list = MyList([1, 2, 5])

    # Вывод длины списка
    print(len(my_list))

    # Вывод самого списка
    print(my_list, len(my_list))

    print()

    my_list.append(7)
    print(my_list, len(my_list))

    print()

    my_list.insert(150, 8)  # out of indexes [1, 2, 5, 7, 8]
    print([1, 2, 5, 7, 8], ' expected insert(150, 8)\n', my_list, ' len: ', len(my_list), sep='')
    my_list.insert(0, 0)  # first [0, 1, 2, 5, 7, 8]
    print([0, 1, 2, 5, 7, 8], ' expected insert(0, 0)\n', my_list, ' len: ', len(my_list), sep='')
    my_list.insert(6, 9)  # last [0, 1, 2, 5, 7, 8, 9]
    print([0, 1, 2, 5, 7, 8, 9], ' expected insert(6, 9)\n', my_list, ' len: ', len(my_list), sep='')
    my_list.insert(3, 4)  # positive in the middle [0, 1, 2, 4, 5, 7, 8, 9]
    print([0, 1, 2, 4, 5, 7, 8, 9], ' expected insert(3, 4)\n', my_list, ' len: ', len(my_list), sep='')
    my_list.insert(-3, 6)  # negative in the middle [0, 1, 2, 4, 5, 6, 7, 8, 9]
    print([0, 1, 2, 4, 5, 6, 7, 8, 9], ' expected insert(-3, 6)\n', my_list, ' len: ', len(my_list), sep='')
    my_list.insert(-24, 3)  # negative in the middle [0, 1, 2, 4, 5, 6, 7, 8, 9]
    print([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], ' expected insert(-24, 3)\n', my_list, ' len: ', len(my_list), sep='')

    print()

    pop_value = my_list.pop()
    print([0, 1, 2, 3, 4, 5, 6, 7, 8], ' expected pop()\n', my_list, ' pop value: ', pop_value, sep='')

    print()

    my_list.remove(150)  # out of indexes [1, 2, 5, 7, 8]
    print([0, 1, 2, 3, 4, 5, 6, 7], ' expected remove(150)\n', my_list, ' len: ', len(my_list), sep='')
    my_list.remove(0)  # first [0, 1, 2, 5, 7, 8]
    print([1, 2, 3, 4, 5, 6, 7], ' expected remove(0)\n', my_list, ' len: ', len(my_list), sep='')
    my_list.remove(3)  # last [0, 1, 2, 5, 7, 8, 9]
    print([1, 2, 3, 4, 6, 7], ' expected remove(3)\n', my_list, ' len: ', len(my_list), sep='')
    my_list.remove(-3)  # negative in the middle [0, 1, 2, 4, 5, 6, 7, 8, 9]
    print([1, 2, 3, 6, 7], ' expected remove(-3)\n', my_list, ' len: ', len(my_list), sep='')
    my_list.remove(-13)  # negative in the middle [0, 1, 2, 4, 5, 6, 7, 8, 9]
    print([1, 2, 6, 7], ' expected remove(-13)\n', my_list, ' len: ', len(my_list), sep='')

    print()

    my_list.clean()
    print('clean list ', my_list)


if __name__ == '__main__':
    main()
