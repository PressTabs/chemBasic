from Matter import matter
from Composite_Id import composite_id


class PureSubstance(matter.Matter):
    def __init__(self, composition, mass, volume=None, state=None):
        matter.Matter.__init__(self, mass, volume, state)
        if composition != type(tuple):
            self.composition = composition
        else:
            self.composition = composite_id.composition(composition)

    def is_element(self):
        if (len(self.composition[1]) == 0) and len(self.composition[3]) == 1:
            return True
        return False

    def repackage(self):
        packaging_list = [self.composition, self.mass]
        if self.is_volume_defined():
            packaging_list.append(self.volume)
        if self.is_state_defined():
            packaging_list.append(self.state)
        packaging_list.insert(0, [len(packaging_list), self.is_volume_defined(), self.is_state_defined()])

        return packaging_list
