from random import randint
with open('CBS_02PYE_L08_T01_FileReadWrite.txt', "w+", encoding="UTF-8") as file:
    for i in range(10000):
        file.write(str(randint(10000000, 99999999)) + '\n')
    file.seek(0)
    result = sum(map(float, file))

print(result)
