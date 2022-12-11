import json

while True:
    library_length = input('Enter library length (non negative integer): ')
    try:
        range(1, 10).index(int(library_length))
    except ValueError:
        print('Error message: Wrong input, try again')
    else:
        library_length = int(library_length)
        break

links_library = dict()

while library_length:
    library_length -= 1
    key_input = input('Enter short link: ')
    value_input = input('Enter full link: ')
    links_library[key_input] = value_input

# json_data = json.dumps(links_library)

with open('CBS_02PYE_L08_T02_URLShortening.json', 'a') as file:
    json.dump(links_library, file)
