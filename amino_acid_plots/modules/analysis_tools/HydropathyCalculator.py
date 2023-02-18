from modules.analysis_tools.generic_calc_tools.LinearWeightCalculator import LinearWeightCalculator
class HydropathyCalculator:
    @staticmethod
    def hydropathy(*args):
        return LinearWeightCalculator.calc_linear_weight("KYTJ820101", *args)
        