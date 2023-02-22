# Bioinformatic App

App showing physical properties of given amino acid sequence.

## Installation

Follow below steps to install and run Bioinformatic App in the correct way.

```bash
  git clone https://github.com/majkelEXE/Bioinformatic_App.git

  cd Bioinformatic_App

  py -3 -m venv .venv

  .venv\scripts\activate

  pip install -r requirements.txt

  python main.py
```

## Example

After installation and running the program, you have to provide RNA sequence(you can find example RNA at the bottom of README) in Input or simply use the "Import" from file button. Then click "Analyse" button. As the result, program will fullfill content of each frame. You have to select one of them.
![Program start](https://i.imgur.com/0kLvLhU.jpg)

After selecting you will see proteins found within this Frame.
![Program after providing RNA](https://i.imgur.com/TnrSabF.jpg)

After selecting you will see proteins found within this Frame.
![Program after providing RNA](https://i.imgur.com/tskqcOt.jpg)

You can click on the visualization or plot button next to protein to see it's physical proteperties described with plots or to generate protein visualization.
![Visualization](https://i.imgur.com/RiKuFTG.jpg)
![Plots](https://i.imgur.com/TnrSabF.jpg)

Example RNA: caaccacactggagaacgagtaagggatcgggcgagcggtactctaaatccaaacggtataataagagctccgcgtaaagtcaaggattctgaaagatttgagtgtctcgccgcattccgctacaaagatctggcatattggtcaccttctatcggttaattccgaaaaatttggctaccagatatggatatgagttagatttaaagcggtagtgagaagttccaccacattgcgccgatcagtagaatggcccaaaagtcgcctatctgcctagtcagaaactgaccgagagcgggagtccgtagcactctcaagagagacgttgtatagtgtgcagtcacttcggtgccctactgcgtaacctggggtccagccggccaatgcgggtcggcgtcggacgatacgtgcagctacgctaaaactcccagagggaggcagacaccaaggggtcaccatccagtgccacaaagagcctataatggttggatggcttcttattataaaagaaggagagcataactgcggtggtggtaggtttacaatccagcgagccgggcgtcgtactgattagagcatataaacctggattaatcaacacccttcatcacggctcgattccatcggacggcagacgaaagcagactggcttttgcggcacggggatatgcggtaagccaggataagaacaacattttacttcgcaaatgacctggtgcgcttttacgacaataataggtcgtttttgggaagtcacgggtcggcggattcgggatcagcgggttatctagatcggcgcgtttagcaagggtgccgcaggccgtactgtactattgacacttaatacccgtactaatggatgaacagcgttctaatactgtcacggtacctcatgcatgacctagaacaagtccatatcgaagcttgttcgagcatcgtgaaaccggccgagcacccggtcttgctactggctcccattatctaacggctaacaagggacc
