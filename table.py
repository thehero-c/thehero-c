from prettytable import PrettyTable
from string import ascii_lowercase


def cutter(expression):
    """
    function to cut all spaces in expression string
    """
    return ''.join(expression.split())


def note_minus(expression):
    """
    this function returns a string of expression without negation
    """
    list_expression = list(expression)
    for i, char in enumerate(list_expression):
        if char == '-':
            list_expression[i + 1] = str(int(not int(list_expression[i + 1])))
            del list_expression[i]
    return ''.join(list_expression)  # here ^-^


def returner(expression, core, row):
    """
    function to solve a expression string and return a result (1 or 0)
    """

    if core == 3:
        x, y, z = row[:3]
        updated_expression = ''
        for char in expression:
            # loop for making a expression with meanings instead variables for 3
            try:
                if char == '-':
                    updated_expression += char
                else:
                    updated_expression += str(eval(char))
            except SyntaxError:
                if char != '-':
                    updated_expression += char
        f'{x,y,z}'  # It matters nothing do not pay attention, it made for being good for pep8, fuck it :)

        expression = note_minus(updated_expression)
        ex0, ex2 = expression[0], expression[2]
        if expression[1] == '^':
            return int(eval(ex0) and eval(ex2))
        elif expression[1] == '+':
            return int(eval(ex0) or eval(ex2))
        elif expression[1] == '!':
            return int(eval(ex0) != eval(ex2))
        elif expression[1] == '>':
            return int(eval(ex0) <= eval(ex2))
        elif expression[1] == '=':
            return int(eval(ex0) == eval(ex2))

    elif core == 2:
        x, y = row[:2]
        updated_expression = ''
        for char in expression:
            # loop for making a expression with meanings instead variables for 2
            try:
                if char == '-':
                    updated_expression += char
                else:
                    updated_expression += str(eval(char))
            except SyntaxError:
                if char != '-':
                    updated_expression += char
        f'{x, y}'  # It matters nothing do not pay attention, it made for being good for pep8, fuck it :)

        expression = note_minus(updated_expression)
        ex0, ex2 = expression[0], expression[2]
        if expression[1] == '^':
            return int(eval(ex0) and eval(ex2))
        elif expression[1] == '+':
            return int(eval(ex0) or eval(ex2))
        elif expression[1] == '!':
            return int(eval(ex0) != eval(ex2))
        elif expression[1] == '>':
            return int(eval(ex0) <= eval(ex2))
        elif expression[1] == '=':
            return int(eval(ex0) == eval(ex2))


def boolean(main_string, list_of_acts):
    str_acts = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
    order_for_3d = [
        [0, 0, 0],
        [0, 0, 1],
        [0, 1, 1],
        [1, 1, 1],
        [1, 1, 0],
        [1, 0, 0],
        [0, 1, 0],
        [1, 0, 1]
    ]  # order of possible meanings for 3 variables
    done_acts_for_3d = [
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
    ]
    order_for_2d = [
        [0, 0],
        [0, 1],
        [1, 1],
        [1, 0]
    ]  # order of possible meanings f or 2 variables
    done_acts_for_2d = [
        [],
        [],
        [],
        [],
        []
    ]

    amount_of_acts = len(list_of_acts)
    # '-', '^', '+', ">" '=', '!'

    alphabet = ascii_lowercase
    lst_variables = tuple(set([i for i in list(main_string) if i in alphabet]))  # all variables in expression
    core = len(lst_variables)

    score_list = [f'{i}-ое' for i in range(1, len(list_of_acts) + 1)]

    my_table = PrettyTable(sorted(list(lst_variables)) + score_list)
    # создание столбцов таблицы
    if core == 3:
        """
        loop for solving expressions for 3 variables/cores
        """

        for j in range(amount_of_acts):
            for i in range(2 ** core):

                cat_act = cutter(list_of_acts[j])
                minus_holder = False

                if ')' in cat_act or '(' in cat_act:
                    minus_holder = True
                    cat_act = cat_act[2:-1]

                if cat_act[0] in str_acts:
                    cat_act = cat_act.replace(cat_act[0], str(done_acts_for_3d[i + 1][eval(cat_act[0]) - 1]))

                if cat_act[2] in str_acts:
                    cat_act = cat_act.replace(cat_act[2], str(done_acts_for_3d[i + 1][eval(cat_act[2]) - 1]))

                if minus_holder:
                    done_act = int(not returner(cat_act, core, order_for_3d[i]))

                else:
                    done_act = returner(cat_act, core, order_for_3d[i])
                order_for_3d[i] += [done_act]
                done_acts_for_3d[i + 1] += [done_act]

        for i in range(2 ** core):
            my_table.add_row(order_for_3d[i])

    elif core == 2:
        """
        loop for solving expressions for 2 variables/cores 
        """

        for j in range(amount_of_acts):
            for i in range(2 ** core):
                cat_act = cutter(list_of_acts[j])
                minus_holder = False

                if ')' in cat_act or '(' in cat_act:
                    minus_holder = True
                    cat_act = cat_act[2:-1]

                if cat_act[0] in str_acts:
                    cat_act = cat_act.replace(cat_act[0], str(done_acts_for_2d[i + 1][eval(cat_act[0]) - 1]))

                if cat_act[2] in str_acts:
                    cat_act = cat_act.replace(cat_act[2], str(done_acts_for_2d[i + 1][eval(cat_act[2]) - 1]))

                if minus_holder:
                    done_act = int(not returner(cat_act, core, order_for_2d[i]))

                else:
                    done_act = returner(cat_act, core, order_for_2d[i])
                order_for_2d[i] += [done_act]
                done_acts_for_2d[i + 1] += [done_act]

        for i in range(2 ** core):
            my_table.add_row(order_for_2d[i])

    print('\n\n', main_string)
    print(my_table)


def main_func(have_to_solve):
    """function, where you can give to know the program
    how many acts, and give to know all of them apart"""

    times = input('Сколько действий в выражении?: ')
    x = 1
    my_dict = {
    }  # dictionary of all acts, keys are from 1 to how many acts in whole

    print("Нужно ввести действие по порядку вычисления")
    while x <= int(times):
        x += 1
        my_dict[x] = input(f'Введи {x - 1} действие: ')

    list_of_acts = list(my_dict.values())
    print(boolean(have_to_solve, list_of_acts))


#  hope next line of code doesn't need to explain, hope you are not stupid so much :))
main_func(have_to_solve=input("Введи полное выражение: "))
