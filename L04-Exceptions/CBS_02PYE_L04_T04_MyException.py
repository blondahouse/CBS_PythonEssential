class InvalidAgeException(Exception):
    pass


number = 18

while True:
    try:
        input_num = int(input("Enter a number: "))
        if input_num < number:
            raise InvalidAgeException
        else:
            print("Eligible to Vote")

    except InvalidAgeException:
        print("Exception occurred: Invalid Age")