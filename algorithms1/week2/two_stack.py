
OPERATORS = {'*', '+', '-', '/'}

""" Djikstra's Two Stack Arithmetic expression evaluation algorithm """


def two_stack(arithmetic_expression):
    value_stack = []
    operator_stack = []

    for string in arithmetic_expression:
        try:
            if isinstance(int(string), int):
                value_stack.append(int(string))
        except:
            if string in OPERATORS:
                operator_stack.append(string)

        if string == ')':
            operator = operator_stack.pop()
            value_1 = value_stack.pop()
            value_2 = value_stack.pop()
            result_value = 0
            if operator == '*':
                result_value = value_1 * value_2
            elif operator == '+':
                result_value = value_1 + value_2
            elif operator == '-':
                result_value = value_1 - value_2
            elif operator == '/':
                result_value = value_1 / value_2
            value_stack.append(result_value)
    return value_stack.pop()


arithmetic = '(1 + ((2 + 3) * ( 4 * 5)))'
print(two_stack(arithmetic))