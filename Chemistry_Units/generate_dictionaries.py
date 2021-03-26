import json


def gen_prefix_unit():
    prefix_unit_instructions = open('Chemistry_Units/prefix_unit_instructions.json')
    instructions = json.load(prefix_unit_instructions)
    units = instructions["units"]
    prefixes = instructions["prefixes"]
    abbreviated_units = instructions["abbreviated_units"]
    abbreviated_prefixes = instructions["abbreviated_prefixes"]
    others = instructions["others"]
    prefix_unit_instructions.close()

    prefix_unit = {}
    for prefix in prefixes:
        for unit in units:
            prefix_unit[prefix + unit] = [prefix, unit]

    for abbreviated_prefix in abbreviated_prefixes:
        for abbreviated_unit in abbreviated_units:
            prefix_unit[abbreviated_prefix + abbreviated_unit] = [abbreviated_prefix, abbreviated_unit]

    for other in others:
        prefix_unit[other] = ['', other]

    return prefix_unit


def gen_master_conversion():
    prefix_unit_instructions = open('Chemistry_Units/prefix_unit_instructions.json')
    instructions = json.load(prefix_unit_instructions)
    prefixes = instructions["prefixes"]
    abbreviated_prefixes = instructions["abbreviated_prefixes"]
    prefix_unit_instructions.close()

    master_conversion = {}
    for prefix_index in range(len(prefixes)):
        master_conversion[prefixes[prefix_index]] = abbreviated_prefixes[prefix_index]

    for prefix_index in range(len(abbreviated_prefixes)):
        master_conversion[abbreviated_prefixes[prefix_index]] = prefixes[prefix_index]

    return master_conversion
