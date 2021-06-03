from itertools import permutations, combinations_with_replacement


def generate_formula(numbers, target):
    number_str_list = list(map(str, numbers))
    operators = ["+", "-"]
    formulas = set()
    for operCombo in combinations_with_replacement(operators, len(number_str_list) - 1):
        for oper in permutations(operCombo, len(number_str_list) - 1):
            formula = "".join(o + v for o, v in zip([""] + list(oper), number_str_list))
            if formula not in formulas and eval(formula) == target:
                print(formula, "=", target)
                formulas.add(formula)
    if len(formulas) < 1:
        print('None')


generate_formula([2, 5, 60, -5, 3], 69)
generate_formula([1, 2, 3, 4, 5], 9)
generate_formula([2, 5, 10], 50)
