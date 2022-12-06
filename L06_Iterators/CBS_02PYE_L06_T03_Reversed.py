class ReversedList:

    def __init__(self, list_to_reverse):
        self.list_to_reverse = list_to_reverse
        self.last_element = len(list_to_reverse)

    def __next__(self):
        if not self.last_element:
            raise StopIteration
        element = self.list_to_reverse[self.last_element - 1]
        # element = self.list_to_reverse.pop()
        self.last_element -= 1
        return element


if __name__ == '__main__':
    # some_iterable_object = range(10, 100, 2)
    # some_iterable_object = []
    some_iterable_object = ['a', 'b']
    my_generator_instance = ReversedList(some_iterable_object)
    while True:
        try:
            print(my_generator_instance.__next__())
        except StopIteration:
            break
