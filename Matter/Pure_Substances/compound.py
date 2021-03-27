from Matter.Pure_Substances import pure_substance
from math import gcd


class Compound(pure_substance.PureSubstance):
    def __init__(self, composition, mass, volume=None, state=None):
        pure_substance.PureSubstance.__init__(self, composition=composition, mass=mass, volume=volume, state=state)
        self.ratio = self.compute_ratio()

    def compute_ratio(self):
        all_subscripts = []
        for subscript in self.composition[0]:
            all_subscripts.append(subscript)
        for subscript in self.composition[2]:
            all_subscripts.append(subscript)

        math_gcd = gcd(*all_subscripts)

        poly_subscripts = [sub / math_gcd for sub in self.composition[0]]
        subscripts = [sub / math_gcd for sub in self.composition[2]]

        return [poly_subscripts, self.composition[1], subscripts, self.composition[3]]
