"""
Write a function that prints a dictionary where the keys are numbers between 1 and 5 and the values are cubes of the keys.
"""


def dict_cube():
    values = {'1': '', '2': '', '3': '', '4': '', '5': '', }
    for i in values.keys():
        values.update({i: (int(i) ** 3)})
    return values


print(dict_cube())
