from aaindex import aaindex1 as aaindex

class LinearWeightCalculator:
    @staticmethod
    def calc_linear_weight(indice_id, *args):
        sequence = args
        values = [0] * len(sequence)
        polarity_dictionary = aaindex[indice_id]['values']

        window_size = 9
        edge_size = 4
        if len(sequence) < 6:
            return values
        if len(sequence) < 18:
            window_size = 3
            edge_size = 1
        
        for i in range(edge_size, len(sequence) - edge_size):
            current_value = 0
            for j in range(i - edge_size, i + edge_size + 1):
                current_value += polarity_dictionary[sequence[j]]
            values[i] = round(current_value / window_size, 2)

        print(values)
        return values