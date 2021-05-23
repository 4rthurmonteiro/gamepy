from random import randint


class Calculate:

    def __init__(self: object, difficulty: int):
        self.__difficulty: int = difficulty
        self.__value1: int = self._generate_value
        self.__value2: int = self._generate_value
        self.__operation: int = randint(1, 3)
        self.__result: int = self._generate_result

    @property
    def difficulty(self):
        return self.__difficulty

    @property
    def value2(self):
        return self.__value2

    @property
    def value1(self):
        return self.__value1

    @property
    def operation(self):
        return self.__operation

    @property
    def result(self):
        return self.__result

    def __str__(self):
        op = ''
        if self.operation == 1:
            op = 'Sum'
        elif self.operation == 2:
            op = 'Subtract'
        elif self.operation == 3:
            op = 'Multiply'
        else:
            op = 'Unknown'

        return f'Value 1: {self.value1} \nValue 2: {self.value2} \nDifficulty: {self.difficulty}\nOperation: {op}'

    @property
    def _generate_value(self):
        if self.difficulty == 1:
            return randint(0, 10)
        elif self.difficulty == 2:
            return randint(0, 100)
        elif self.difficulty == 3:
            return randint(0, 1000)
        elif self.difficulty == 4:
            return randint(0, 10000)
        else:
            return randint(0, 100000)

    @property
    def _generate_result(self):
        if self.operation == 1:
            return self.value1 + self.value2
        elif self.operation == 2:
            return self.value1 - self.value2
        else:
            return self.value1 * self.value2

    @property
    def _operation_symbol(self):
        if self.operation == 1:
            return '+'
        elif self.operation == 2:
            return '-'
        else:
            return '*'

    def check_result(self, answer):
        success = False

        if self.result == answer:
            print('Right answer!')
            success = True
        else:
            print('Wrong!!')

        print(f'{self.value1} {self._operation_symbol} {self.value2} = {self.result}')

        return success

    def show_operation(self):
        print(f'{self.value1} {self._operation_symbol} {self.value2} = ?')
