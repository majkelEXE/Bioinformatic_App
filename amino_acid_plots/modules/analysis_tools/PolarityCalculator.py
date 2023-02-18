from modules.analysis_tools.generic_calc_tools.LinearWeightCalculator import LinearWeightCalculator

class PolarityCalculator:
    @staticmethod
    def polarity(*args):
        return LinearWeightCalculator.calc_linear_weight("ZIMJ680103", *args)