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
  
  pip install -e git+https://github.com/IgorBialek/pikachu.git@main#egg=pikachu-chem

  python main.py
```

## Example

After installation and running the program, you have to provide amino acid sequence and then click "Analyse sequence" button. As the result plots will be displayed: hydropathy, polarity, disorder and disorder binding.
![Program visualization](https://i.imgur.com/TnrSabF.jpg)
