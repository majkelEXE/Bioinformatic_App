from aaindex import aaindex1 as aaindex

class LinearWeightCalculator:
    # def __init__(self, *args):
    #     self.sequence = args
    @staticmethod
    def calc_linear_weight(indice_id, *args):
        sequence = args
        values = [0] * len(sequence)
        polarity_dictionary = aaindex[indice_id]['values']
        
        for i in range(4, len(sequence) - 4):
            current_value = 0
            for j in range(i - 4, i + 5):
                current_value += polarity_dictionary[sequence[j]]
            values[i] = round(current_value / 9, 2)

        colors = []
        for value in values:
            if value >= 0:
                colors.append('#EE6666')
            elif value < 0:
                colors.append('#0390fc')
        
        return {"values": values, "colors": colors} 