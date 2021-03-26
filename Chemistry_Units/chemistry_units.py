from Chemistry_Units import generate_dictionaries

value_conversion = {
    'tera': 1e+12,
    'giga': 1e+9,
    'mega': 1e+6,
    'kilo': 1e+3,
    'hecto': 1e+2,
    'deca': 1e+1,
    '': 1e+0,
    'deci': 1e-1,
    'centi': 1e-2,
    'milli': 1e-3,
    'micro': 1e-6,
    'nano': 1e-9,
    'pico': 1e-12,
    'T': 1e+12,
    'G': 1e+9,
    'M': 1e+6,
    'k': 1e+3,
    'h': 1e+2,
    'da': 1e+1,
    'd': 1e-1,
    'c': 1e-2,
    'm': 1e-3,
    'q': 1e-6,
    'n': 1e-9,
    'p': 1e-12,
}

prefix_unit = generate_dictionaries.gen_prefix_unit()
master_conversion = generate_dictionaries.gen_master_conversion()
