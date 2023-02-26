from amino_acid_plots.modules.analysis_tools.generic_calc_tools.LinearWeightCalculator import LinearWeightCalculator
class HydropathyCalculator:
    @staticmethod
    def hydropathy(*args):
        result = LinearWeightCalculator.calc_linear_weight("KYTJ820101", *args)
        print(result)

        colors = []
        for value in result:
            if value >= 0:
                colors.append('#EE6666')
            elif value < 0:
                colors.append('#0390fc')
        
        return {"values": result, "colors": colors} 

        