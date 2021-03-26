def alpha_only(string):
    alpha_only_string = ''
    for char in string:
        if char.isalpha():
            alpha_only_string += char

    return alpha_only_string


def digits_only(string):
    digits_only_string = ''
    for digit in string:
        if digit.isdigit():
            digits_only_string += digit

    return digits_only_string
