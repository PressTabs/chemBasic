from Chemistry_Units import chem_unit


class Matter:
    def __init__(self, mass, volume=None, state=None):
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

        if {'solid': 0, 'liquid': 1, 'gas': 2, 'be': 3, 'plasma': 4}.get(state) != -1:
            self.state = state

    def is_volume_defined(self):
        if hasattr(self, 'volume'):
            return True
        return False

    def is_state_defined(self):
        if hasattr(self, 'state'):
            return True
        return False
