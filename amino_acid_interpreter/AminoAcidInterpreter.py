#CORRECT
aminoacidToPtotein = {
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
def translateToProtein(rna, option):
    # remove last element if not possible to convert to protein
    if len(rna[len(rna)-1]) != 3:
        rna.pop()
    # convert RNA to protein
    protein = []
    for i in rna:
        protein.append(aminoacidToPtotein.get(i))
    protein = ''.join(protein)
    print('---' +protein)
    # find start and stop codons
    # show only the part between start and stop codons
    findStartAndStop(protein, option)


def findStartAndStop(protein, option):
    index_start = protein.find('M')
    if index_start != -1:
        # startStop = protein[index:]
        # index_stop = protein.find('[STOP]')
        #find first occurance of [STOP] after index_start
        index_stop = protein.index("[STOP]", index_start)
        if index_stop != -1:
            if option == 3:
                print(protein)
            startStop = protein[index_start:index_stop+6]
            protein = protein[index_stop+6:]
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
            findStartAndStop(protein, option)

def getFromFile(name):
    # read file
    with open(name) as file:
        rna = file.read().replace('\n', '')
        executeAll(rna)

import string

def executeAll(rna):
    # check if sequence contains 'T' and replace it with 'U'
    if 'T' in rna and 'U' not in rna:
        rna = rna.replace('T', 'U')
    # check if sequence is correct
    lettersToCheck = list(string.printable)	
    lettersToCheck.remove('U')
    lettersToCheck.remove('A')
    lettersToCheck.remove('G')
    lettersToCheck.remove('C')
    if any(letter in rna for letter in lettersToCheck) or len(rna) == 0:
        print('Incorrect sequence!')
    else:
        # split RNA sequence into threes with offset
        option1 = [rna[i:i+3] for i in range(0, len(rna), 3)]
        option2 = [rna[i:i+3] for i in range(1, len(rna), 3)]
        option3 = [rna[i:i+3] for i in range(2, len(rna), 3)]

        translateToProtein(option1, 1)
        translateToProtein(option2, 2)
        translateToProtein(option3, 3)

        print(result)

# example RNA sequence
#rna = 'AAUGUCGGUCAGCUUUGAGAAAACCAUGGUCAAAAUGAGCGCUUUGAAGCAUUUCGGCCAGAAGCAUGCGGGUAUGCCAGCCUUACCAGACGCAAUUAGGCACAGUGCCCCCUCAGCUCCGACUGAGAACCGCGCAGACCUAUUAUAUGCAAGUGUGAUGCGCCAGCUAACAGUGUACAGACACGUGCGUUAGUCCCUGCGUCCCGAUCCCAACGGAAAAGGUGAUAUUGCGGGGUUCGCACUGGGCUUCACUAAAGGCUAGGGACCUCGAAGUCUUUUCAGCCGUUAACUCUUACAUAC' 
# dna = 'CCGGGAAGGGGTTCGCAAGTCGCACCCTAAACGATGTTGAAGGCTCAGGATGTACACGCACTAGTACAATACATACGTGTTCCGGCTCTTATCCTGCATCGGAAGCTCAATCATGCATCGCACCAGCGTGTTCGTGTCATCTAGGAGGGGCGCGTAGGATAAATAATTCAATTAAGATATCGTTATGCTAGTATACGCCTACCCGTCACCGGCCAACAGTGTGCAGATGGCGCCACGAGTTACTGGCCCTGATTTCTCCGCTTCTAATACCGCACACTGGGCAATACGAGCTCAAGCCAG'

# read from variable
rna = "AAUGUCGGUCAGCUUUGAGAAAACCAUGGUCAAAAUGAGCGCUUUGAAGCAUUUCGGCCAGAAGCAUGCGGGUAUGCCAGCCUUACCAGACGCAAUUAGGCACAGUGCCCCCUCAGCUCCGACUGAGAACCGCGCAGACCUAUUAUAUGCAAGUGUGAUGCGCCAGCUAACAGUGUACAGACACGUGCGUUAGUCCCUGCGUCCCGAUCCCAACGGAAAAGGUGAUAUUGCGGGGUUCGCACUGGGCUUCACUAAAGGCUAGGGACCUCGAAGUCUUUUCAGCCGUUAACUCUUACAUAC"
executeAll(rna)

# getFromFile('data.txt')