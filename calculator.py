

class Matematic:
    
    def sum(self, x: float, y:float)->float:
        """
        Функция сложения
        """    
        return f'Результат сложения: {x + y}'

    def subtract(self, x: float, y:float)->float:
        """
        Функция вычитания
        """
        return f'Результат вычитания: {x - y}'
        
    def multiply(self, x: float, y:float)->float:
        """
        Функция умножения
        """
        return f'Результат умножения: {x * y}'

    def divide(self, x: float, y: float) -> float:
        """
        Функция деления
        """
        try:
            result = x / y
        except ZeroDivisionError:
            return 'Ошибка! Делить на ноль нельзя!'
        
        return f'Результат деления: {result}'


def input_number()->(int, int):
    """
    Функция ввода чисел для дальнейших математических действий
    """

    while True:
        num_1 = input('Введите первое число: ')
        num_2 = input('Введите второе число: ')

        try:
            num_1 = int(num_1)
            num_2 = int(num_2)
            return num_1, num_2
        
        except ValueError:
            print('Ошибка ввода! Введите число!')


def func_action()->int:
    """
    Функция выполняющая действия в соответствии с вводом от пользователя
    """

    calculator = Matematic()
    operations = {1: calculator.sum, 2: calculator.subtract,
                  3: calculator.multiply, 4: calculator.divide}
    
    action = int(input('''Какое действие вы хотите совершить:
    1.Сложение
    2.Вычитание
    3.Умножение
    4.Деление
    '''))
    
    if action in operations:
        num_1, num_2 = input_number()
        result = operations[action](num_1, num_2)
        print(f'{result}')
    else:
        print('Вы ввели не верное значение действия!')


if __name__ == '__main__':
    func_action()