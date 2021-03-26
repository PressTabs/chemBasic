from Composite_Id import Polyatomics
from Composite_Id import char_only


def composition(substance):

    open_parentheses = []
    for characterIndex in range(len(substance)):
        if substance[characterIndex] == '(':
            open_parentheses.append(characterIndex)

    closed_parentheses = []
    for characterIndex in range(len(substance)):
        if substance[characterIndex] == ')':
            closed_parentheses.append(characterIndex)

    polyatomics = []
    for parenthesis_index in range(len(open_parentheses)):
        polyatomics.append(substance[open_parentheses[parenthesis_index] + 1:closed_parentheses[parenthesis_index]])

    capital_character_indices = []
    for characterIndex in range(len(substance)):
        if substance[characterIndex].isupper():
            capital_character_indices.append(characterIndex)

    polyatomic_subscripts = []
    for parenthesis_index in range(len(closed_parentheses)):
        capital_list_index = 0
        while capital_list_index < len(capital_character_indices):
            if capital_character_indices[capital_list_index] > closed_parentheses[parenthesis_index]:
                polyatomic_subscripts.append(substance[closed_parentheses[parenthesis_index] + 1:capital_character_indices[capital_list_index]])
                capital_list_index = len(capital_character_indices) + 1
            capital_list_index += 1

        if capital_list_index == len(capital_character_indices):
            polyatomic_subscripts.append(substance[closed_parentheses[parenthesis_index] + 1:len(substance)])

    fixed_polyatomic_subscripts = []
    for subscript in range(len(polyatomic_subscripts)):
        fixed_polyatomic_subscripts.append(int(char_only.digits_only(polyatomic_subscripts[subscript])))

    polyatomic_subscripts = fixed_polyatomic_subscripts

    for parenthesis_index in range(len(open_parentheses)):
        substance = substance.replace(f'({polyatomics[parenthesis_index]}){polyatomic_subscripts[parenthesis_index]}', '')

    substance_composites = []
    initial_range = 0
    for composite in range(len(substance)):
        if substance[composite].isupper():
            substance_composites.append(substance[initial_range:composite])
            initial_range = composite

        if composite == len(substance) - 1:
            substance_composites.append(substance[initial_range:len(substance)])

    composite_index = 0
    while composite_index < len(substance_composites):
        if substance_composites[composite_index] == '':
            substance_composites.pop(composite_index)
            composite_index += 1
        composite_index += 1

    poly3_iterations = len(substance_composites) - 3
    counter = 0
    while counter <= poly3_iterations:
        if type(Polyatomics.SymbolsToName.get(substance_composites[counter] + substance_composites[counter + 1] + substance_composites[counter + 2])) == str:
            polyatomic = substance_composites[counter] + substance_composites[counter + 1] + substance_composites[counter + 2]
            substance_composites.pop(counter + 2)
            substance_composites.pop(counter + 1)
            substance_composites.pop(counter)
            substance_composites.insert(counter, polyatomic)
            poly3_iterations += -2
        counter += 1

    poly2_iterations = len(substance_composites) - 2
    counter = 0
    while counter <= poly2_iterations:
        if type(Polyatomics.SymbolsToName.get(substance_composites[counter] + substance_composites[counter + 1])) == str:
            polyatomic = substance_composites[counter] + substance_composites[counter + 1]
            substance_composites.pop(counter + 1)
            substance_composites.pop(counter)
            substance_composites.insert(counter, polyatomic)
            poly2_iterations += -1
        counter += 1

    subscripts = []
    for numberOfComposites in range(len(substance_composites)):
        if Polyatomics.SymbolsToName.get(substance_composites[numberOfComposites]) is None:
            element_digits = char_only.digits_only(substance_composites[numberOfComposites])
            if element_digits == '':
                subscripts.append(1)
            else:
                subscripts.append(int(element_digits))

        else:
            subscripts.append(1)

    fixed_substance_composites = []
    for composites in substance_composites:
        if Polyatomics.SymbolsToName.get(composites) is None:
            fixed_substance_composites.append(char_only.alpha_only(composites))

        else:
            fixed_substance_composites.append(composites)

    substance_composites = fixed_substance_composites

    return polyatomic_subscripts, polyatomics, subscripts, substance_composites
