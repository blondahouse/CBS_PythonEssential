iterable = range(10)

iter_obj = iter(iterable)

while True:
    try:
        print(next(iter_obj))
    except StopIteration:
        break