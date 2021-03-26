from Chemistry_Units import prefix_unit


class ChemUnit(prefix_unit.PrefixUnit):
    def __init__(self, amount, prefix_w_unit):
        if isinstance(prefix_w_unit, prefix_unit.PrefixUnit):
            prefix_unit.PrefixUnit.__init__(self, prefix_w_unit.prefix + prefix_w_unit.unit)
        else:
            prefix_unit.PrefixUnit.__init__(self, prefix_w_unit)
        self.amount = amount
