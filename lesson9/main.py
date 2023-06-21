from cmath import sqrt
import json
import csv
import random
from typing import Callable


def create_csv_file(rows_min=100, rows_max=1000, int_min=-1000, int_max=1000):
    with open('coefficients.csv', 'w', encoding='UTF-8') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
        for row in range(random.randint(rows_min, rows_max)):
            writer.writerow([random.randint(int_min, int_max), random.randint(int_min, int_max),
                             random.randint(int_min, int_max)])


def solve_csv(func: Callable):
    create_csv_file()

    def wrapper():
        with open('coefficients.csv', 'r', encoding='UTF-8') as file:
            data = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC)
            for coefficient in data:
                if coefficient and coefficient[0] != 0:
                    func(*coefficient)

    return wrapper


def json_result(func: Callable):
    result = []

    def wrapper(*args):
        roots = func(*args)
        solve_dict = {'a': args[0], 'b': args[1], 'c': args[2], 'roots': roots}
        result.append(solve_dict)
        with open("solutions.json", 'w', encoding='UTF-8') as file:
            json.dump(result, file, indent=2)
        return roots

    return wrapper


@solve_csv
@json_result
def get_roots(*args):
    a, b, c = args
    discr = b * b - 4 * a * c
    if discr > 0:
        x1 = (-b + sqrt(discr)) / (2 * a)
        x2 = (-b - sqrt(discr)) / (2 * a)
        return str(x1), str(x2)
    elif discr == 0:
        x = -b / (2 * a)
        return str(x)


get_roots()