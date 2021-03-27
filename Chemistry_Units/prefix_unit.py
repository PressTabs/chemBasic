from Chemistry_Units import chemistry_units


class PrefixUnit:
    def __init__(self, prefix_unit):
        self.prefix_unit = prefix_unit
        self.prefix_unit_comp = chemistry_units.prefix_unit[prefix_unit]
        self.prefix = self.prefix_unit_comp[0]
        self.unit = self.prefix_unit_comp[1]
        self.prefix_value = chemistry_units.value_conversion[self.prefix]
