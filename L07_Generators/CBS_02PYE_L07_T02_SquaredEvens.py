my_list = [1, 2, 4, 5, 6, 7, 12, 25, 374, 542, 1213, 6423, 45678]
even_list = [num for num in my_list if num % 2 == 0]

a = [i ** 2 for i in even_list]
b = (i ** 2 for i in even_list)
print(a)
while True:
    try:
        print(next(b))
    except StopIteration:
        break
