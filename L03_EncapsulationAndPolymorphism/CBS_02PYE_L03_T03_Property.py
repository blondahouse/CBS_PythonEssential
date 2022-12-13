class Temperature:

    def __init__(self):
        self.__celsius_temp = None
        self.__fahrenheit_temp = None

    @property
    def celsius_temp(self):
        return self.__celsius_temp

    @celsius_temp.setter
    def celsius_temp(self, value):
        self.__celsius_temp = value
        self.__fahrenheit_temp = (value * 9 / 5) + 32

    @property
    def fahrenheit_temp(self):
        return self.__fahrenheit_temp

    @fahrenheit_temp.setter
    def fahrenheit_temp(self, value):
        self.__fahrenheit_temp = value
        self.__celsius_temp = (value - 32) * 5 / 9


temp = Temperature()
temp.celsius_temp = 36.6

print(f'Celsius temperature is: {temp.celsius_temp}')
print(f'Fahrenheit temperature is: {temp.fahrenheit_temp}')

temp.fahrenheit_temp = 100

print(f'Celsius temperature is: {temp.celsius_temp}')
print(f'Fahrenheit temperature is: {temp.fahrenheit_temp}')
