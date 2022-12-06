def reverse_list(list_to_reverse):
    last_element = len(list_to_reverse) - 1
    while last_element >= 0:
        element = list_to_reverse[last_element]
        last_element -= 1
        yield element


if __name__ == '__main__':
    l = range(3, 10)
    a = reverse_list(l)
    for n in a:
        print(n)
