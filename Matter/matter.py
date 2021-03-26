from Chemistry_Units import chem_unit


class Matter:
    def __init__(self, mass, volume=None):
        if isinstance(mass, chem_unit.ChemUnit):
            self.mass = mass
        else:
            mass_comp = mass.split(' ')
            self.mass = chem_unit.ChemUnit(mass_comp[0], mass_comp[1])

        if isinstance(volume, chem_unit.ChemUnit):
            self.volume = volume
        elif volume == type(str):
            volume_comp = volume.split(' ')
            self.volume = chem_unit.ChemUnit(volume_comp[0], volume_comp[1])

    def is_volume_defined(self):
        if hasattr(self, 'volume'):
            return True
        return False
