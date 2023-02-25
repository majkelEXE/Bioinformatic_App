from amino_acid_plots.modules.analysis_tools.generic_calc_tools.LinearWeightCalculator import LinearWeightCalculator

class PolarityCalculator:
    @staticmethod
    def polarity(*args):
        result = LinearWeightCalculator.calc_linear_weight("ZIMJ680103", *args)
        return {"values": result, "colors": "#ff9b3d"} 
    