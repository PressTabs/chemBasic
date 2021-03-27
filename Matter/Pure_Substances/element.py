from Matter.Pure_Substances import pure_substance


class Element(pure_substance.PureSubstance):
    def __init__(self, composition, mass, volume=None, state=None):
        pure_substance.PureSubstance.__init__(self, composition=composition, mass=mass, volume=volume, state=state)
