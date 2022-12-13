class Employee:

    def __init__(self, first_name, second_name, department, year):
        if type(first_name) == str:
            if str(first_name)[0].isupper():
                self.first_name = first_name
            else:
                raise ValueError('Name should start from upper letter')
        else:
            raise ValueError('First name cannot contain any digits')

        if type(second_name) == str:
            if str(second_name)[0].isupper():
                self.second_name = second_name
            else:
                raise ValueError('Name should start from upper letter')
        else:
            raise ValueError('Second name cannot contain any digits')
        self.department = department
        if type(int(year)) == int:
            if int(year) > 2000:
                self.year = int(year)
            else:
                raise ValueError('Company establishing date is 2001')
        else:
            raise ValueError('Year should be type of int')

    def __str__(self):
        return '%s %s from %s department. Employed at %s' % (self.first_name,
                                                             self.second_name,
                                                             self.department,
                                                             self.year)


if __name__ == '__main__':
    e_list = []
    while True:
        print('Enter new employee')
        f_name = input('First name (exit to stop): ')
        if f_name == 'exit':
            break
        s_name = input('Second name (exit to stop): ')
        if s_name == 'exit':
            break
        dept = input('Department (exit to stop): ')
        if dept == 'exit':
            break
        year = input('Year of employment (exit to stop): ')
        if year == 'exit':
            break
        try:
            emp = Employee(f_name, s_name, dept, year)
        except ValueError as e:
            print(e)
        else:
            e_list.append(emp)

    jl = Employee('John', 'Lippman', 'Technical', 2004)
    e_list.append(jl)
    js = Employee('John', 'Steward', 'Technical', 2003)
    e_list.append(js)
    ls = Employee('Larry', 'Steward', 'Management', 2001)
    e_list.append(ls)
    for e in e_list:
        try:
            if e.year > 2002:
                print(e)
        except AttributeError:
            print('AttributeError occurred')
