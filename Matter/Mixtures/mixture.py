from Matter.Pure_Substances import pure_substance


class Mixture:
    def __init__(self, composition):
        self.composition = composition

    def volume_composition(self, precision=3):
        can_comp = True
        for comp_pure_substance in self.composition:
            if not comp_pure_substance.is_volume_defined():
                can_comp = False

        if can_comp:
            vol_comp = []
            volume_sum = 0
            for comp_pure_substance in self.composition:
                volume_sum += round(comp_pure_substance.volume.amount / comp_pure_substance.volume.prefix_value, precision)
                vol_comp.append(round(comp_pure_substance.volume.amount / comp_pure_substance.volume.prefix_value, precision))

            percent_vol = []
            for volume in vol_comp:
                percent_vol.append(round(volume / volume_sum, precision) * 100)

            pure_substance_compositions = []
            for comp_pure_substance in self.composition:
                pure_substance_compositions.append(comp_pure_substance.formula)

            interpolated_percent_vol_formula = []
            for index in range(len(self.composition)):
                interpolated_percent_vol_formula.append([percent_vol[index], vol_comp[index], pure_substance_compositions[index]])

            return interpolated_percent_vol_formula
