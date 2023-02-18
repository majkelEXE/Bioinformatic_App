import string

# CORRECT
aminoacidToProtein = {
    'UUU': 'F', 'UUC': 'F',
    'UUA': 'L', 'UUG': 'L',
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
    'UAU': 'Y', 'UAC': 'Y',
    'UAA': '[STOP]', 'UAG': '[STOP]',
    'UGU': 'C', 'UGC': 'C',
    'UGA': '[STOP]',
    'UGG': 'W',
    'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'CAU': 'H', 'CAC': 'H',
    'CAA': 'Q', 'CAG': 'Q',
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I',
    'AUG': 'M',
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'AAU': 'N', 'AAC': 'N',
    'AAA': 'K', 'AAG': 'K',
    'AGU': 'S', 'AGC': 'S',
    'AGA': 'R', 'AGG': 'R',
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'GAU': 'D', 'GAC': 'D',
    'GAA': 'E', 'GAG': 'E',
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
}

result = {
    'option1': [],
    'option2': [],
    'option3': []
}


# translate split RNA to protein
def translate_to_protein(rna, option):
    # remove last element if not possible to convert to protein
    if len(rna[len(rna) - 1]) != 3:
        rna.pop()
    # convert RNA to protein
    protein = []
    for i in rna:
        protein.append(aminoacidToProtein.get(i))
    protein = ''.join(protein)
    # print('---' +protein)
    # find start and stop codons
    # show only the part between start and stop codons
    find_start_and_stop(protein, option)


def find_start_and_stop(protein, option):
    index_start = protein.find('M')
    if index_start != -1:
        # startStop = protein[index:]
        # index_stop = protein.find('[STOP]')
        # find first occurance of [STOP] after index_start
        try:
            index_stop = protein.index("[STOP]", index_start)
        except ValueError:
            return
        
        if index_stop != -1:
            # if option == 3:
            # print(protein)
            startStop = protein[index_start:index_stop + 6]
            protein = protein[index_stop + 6:]
            # print(protein)
            # save to dictionary
            if option == 1:
                if startStop not in result['option1']:
                    result['option1'].append(startStop)
            elif option == 2:
                if startStop not in result['option2']:
                    result['option2'].append(startStop)
            elif option == 3:
                if startStop not in result['option3']:
                    result['option3'].append(startStop)
            find_start_and_stop(protein, option)


def get_from_file(name):
    # read file
    with open(name) as file:
        rna = file.read().replace('\n', '')
        check_sequence(rna)


def check_sequence(rna):
    # check if sequence contains 'T' and replace it with 'U'
    rna = rna.upper()
    print(rna)
    if 'T' in rna and 'U' not in rna:
        rna = rna.replace('T', 'U')
    # check if sequence is correct
    lettersToCheck = list(string.printable)
    lettersToCheck.remove('U')
    lettersToCheck.remove('A')
    lettersToCheck.remove('G')
    lettersToCheck.remove('C')
    if any(letter in rna for letter in lettersToCheck) or len(rna) == 0:
        return 0
    else:
        # split RNA sequence into threes with offset
        option1 = [rna[i:i + 3] for i in range(0, len(rna), 3)]
        option2 = [rna[i:i + 3] for i in range(1, len(rna), 3)]
        option3 = [rna[i:i + 3] for i in range(2, len(rna), 3)]

        translate_to_protein(option1, 1)
        translate_to_protein(option2, 2)
        translate_to_protein(option3, 3)

        return result


# example RNA sequence
# sequence = 'AAUGUCGGUCAGCUUUGAGAAAACCAUGGUCAAAAUGAGCGCUUUGAAGCAUUUCGGCCAGAAGCAUGCGGGUAUGCCAGCCUUACCAGACGCAAUUAGGCACAGUGCCCCCUCAGCUCCGACUGAGAACCGCGCAGACCUAUUAUAUGCAAGUGUGAUGCGCCAGCUAACAGUGUACAGACACGUGCGUUAGUCCCUGCGUCCCGAUCCCAACGGAAAAGGUGAUAUUGCGGGGUUCGCACUGGGCUUCACUAAAGGCUAGGGACCUCGAAGUCUUUUCAGCCGUUAACUCUUACAUAC'
# dna = 'CCGGGAAGGGGTTCGCAAGTCGCACCCTAAACGATGTTGAAGGCTCAGGATGTACACGCACTAGTACAATACATACGTGTTCCGGCTCTTATCCTGCATCGGAAGCTCAATCATGCATCGCACCAGCGTGTTCGTGTCATCTAGGAGGGGCGCGTAGGATAAATAATTCAATTAAGATATCGTTATGCTAGTATACGCCTACCCGTCACCGGCCAACAGTGTGCAGATGGCGCCACGAGTTACTGGCCCTGATTTCTCCGCTTCTAATACCGCACACTGGGCAATACGAGCTCAAGCCAG'

#
#READY EXAMPLES
#

# sequence = "AAUGUCGGUCAGCUUUGAGAAAACCAUGGUCAAAAUGAGCGCUUUGAAGCAUUUCGGCCAGAAGCAUGCGGGUAUGCCAGCCUUACCAGACGCAAUUAGGCACAGUGCCCCCUCAGCUCCGACUGAGAACCGCGCAGACCUAUUAUAUGCAAGUGUGAUGCGCCAGCUAACAGUGUACAGACACGUGCGUUAGUCCCUGCGUCCCGAUCCCAACGGAAAAGGUGAUAUUGCGGGGUUCGCACUGGGCUUCACUAAAGGCUAGGGACCUCGAAGUCUUUUCAGCCGUUAACUCUUACAUAC"
# print(check_sequence(sequence))

#
#sequence = "taagaggctacacagtcttgaggaaactagaattagaaactaacgctactctcgtctccgtccccgttcttaaaggtaagccgcgtgcactaggtcagcgggcgggatcctcttcgttatcctcccccaaaaggtcttgcggcaccaaggatccccaccataaaactcatgcctatcactagtcgcgactggatgcttataagcgacagcggcctagtgaagggtggtagacaatctcagtgtcttacaaacggtatacctgacctgcgacggctaattacgcactttcaatcttaagttgaggttatcagccggaccaaacactctgtgctcttacttgctgggttccaggagtgcgcgccacgtgaagtcgacaaacttcaaaagcttcgcaggactccacgcagggactccaacggaccttctaacctacccgtgatgtctgctccacgccagctagactcatgccgtcaatgtctggctatattggttaaaagctctcatcaccgtcgatttttttgtggttcgaggccacggctttactagtcccgtaagaccgtggtggtatgggcagcctacgatatgtttagcatcggagaacgtgaagtaaagatattggagatactggacctgattcgatgcactacacaaggccagtctctataggggccctctttgtgtccttagaattacgagcgagattaatgctacaaaggaaagagaaggtcggatgagggtgttagtgacaaatactatgtggtgggccacgaacattacatcacctccacggcacggaggcatggtacgcatatatctttttccctgtttgaccagggggttgatcagacgattcttttgccagtaacagtaacgcgtcagcattgctacgtcatgagtgattcgctagcagaccttgtccacgaataatggcgcacaaactccgcgaacccctcgttcactgaatcaatggttgtgccagcgttggcggtgtgacatacgg"
#print(check_sequence(sequence))

#sequence = "caaccacactggagaacgagtaagggatcgggcgagcggtactctaaatccaaacggtataataagagctccgcgtaaagtcaaggattctgaaagatttgagtgtctcgccgcattccgctacaaagatctggcatattggtcaccttctatcggttaattccgaaaaatttggctaccagatatggatatgagttagatttaaagcggtagtgagaagttccaccacattgcgccgatcagtagaatggcccaaaagtcgcctatctgcctagtcagaaactgaccgagagcgggagtccgtagcactctcaagagagacgttgtatagtgtgcagtcacttcggtgccctactgcgtaacctggggtccagccggccaatgcgggtcggcgtcggacgatacgtgcagctacgctaaaactcccagagggaggcagacaccaaggggtcaccatccagtgccacaaagagcctataatggttggatggcttcttattataaaagaaggagagcataactgcggtggtggtaggtttacaatccagcgagccgggcgtcgtactgattagagcatataaacctggattaatcaacacccttcatcacggctcgattccatcggacggcagacgaaagcagactggcttttgcggcacggggatatgcggtaagccaggataagaacaacattttacttcgcaaatgacctggtgcgcttttacgacaataataggtcgtttttgggaagtcacgggtcggcggattcgggatcagcgggttatctagatcggcgcgtttagcaagggtgccgcaggccgtactgtactattgacacttaatacccgtactaatggatgaacagcgttctaatactgtcacggtacctcatgcatgacctagaacaagtccatatcgaagcttgttcgagcatcgtgaaaccggccgagcacccggtcttgctactggctcccattatctaacggctaacaagggacc"
#print(check_sequence(sequence))

# sequence = "cttgccgaaagtgtatccaaagcgtcgggttttcaagtttggactgacacatacgttcacaggcaatgaatcaaggatgagcgtagaccacatcaactaacagtattgatctgcgttgccataacgaggaccaaagccaacccacagtcagcgcggtagattcgctgtttctatgcacgccttagcgttaactgtcgctgatcaaaactcggccactccagtcgcaggctatacattcagtcttgccaacagcgaggacccgcagcttaggtggcagaactaatgcacgggtgcgcgagataactagagtacaaagtagcagcatcaggatcgttacatggagccgtgatcgacgaaaggcaggtgcgtgtaacgagtgtattcttca"
# print(check_sequence(sequence))

#not sure about it
# sequence = "gatctcggaggtcacgtggacgttcccacttagggattacgtttgactattagagaagcgaagcatagtgactcatccggacatactggcctcggccctagagctcccccatgtggtcggtgcaattaagtgtgagtcgagtcagccagacagcggtgcctaacgggttataaatttgatgcaagtttccagctgcgaggaccacgtaatacgggacttgtttcgaccacgacgaaggtgcgggaatcacccttagagccctttatttataacttcgaaaataacatatttatcgctatcctatactcaaggttcaaaacatcatccctcacgattcttgggtaccatcgtcgctacgtttttataacgactcctaaggtgcaatcaaaccgccaacgatcggttccggttttccctgtcgacactatccgcgtattcggtcgaccgggacatcggtcatgtctcttttgtgccgaatgacgcacagtatgacatcggtcatcccatataaattaacctatgagggggaacccggtctttttcctggcaacttttctcttgactacc"
# print(check_sequence(sequence))


