while True:
    do = input('Enter the operation -->')
    if do == 'quit':
        break
    else:
        try:
            result = eval(do)
        except SyntaxError:  # 2 +*? 4
            print('SyntaxError occurred')
        except TypeError:  # 2 / '2'
            print('TypeError occurred')
        except ValueError:  # int('f')
            print('ValueError occurred')
        except ZeroDivisionError:  # 2 / 0
            print('ZeroDivisionError occurred')
        except NameError:  # wp + 1
            print('NameError occurred')
        else:
            print('Result: ', result)
