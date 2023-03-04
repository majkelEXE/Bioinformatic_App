# Bioinformatic App

[comment]: <> (App showing physical properties of given amino acid sequence.)
Aplikacja analizująca ciąg DNA lub RNA. Wynikiem programu jest lista białek w podanej sekwencji, wraz z wizualizacją ich struktury oraz zestawieniem właściwości fizycznych.

## Instalacja

[comment]: <> (Installation, Follow below steps to install and run Bioinformatic App in the correct way.)
Aby w poprawny sposób zainstalować aplikację, wykonaj poniższe polecenia(Python 3.10.6 lub nowszy):

```bash
  git clone git@github.com:majkelEXE/Bioinformatic_App.git

  cd Bioinformatic_App

  py -3 -m venv .venv

  .venv\scripts\activate

  pip install -r requirements.txt

  python main.py
```

Przykładowe sekwencje do sprawdzenia poprawności zainstalowanej aplikacji:

- _taagaggctacacagtcttgaggaaactagaattagaaactaacgctactctcgtctccgtccccgttcttaaaggtaagccgcgtgcactaggtcagcgggcgggatcctcttcgttatcctcccccaaaaggtcttgcggcaccaaggatccccaccataaaactcatgcctatcactagtcgcgactggatgcttataagcgacagcggcctagtgaagggtggtagacaatctcagtgtcttacaaacggtatacctgacctgcgacggctaattacgcactttcaatcttaagttgaggttatcagccggaccaaacactctgtgctcttacttgctgggttccaggagtgcgcgccacgtgaagtcgacaaacttcaaaagcttcgcaggactccacgcagggactccaacggaccttctaacctacccgtgatgtctgctccacgccagctagactcatgccgtcaatgtctggctatattggttaaaagctctcatcaccgtcgatttttttgtggttcgaggccacggctttactagtcccgtaagaccgtggtggtatgggcagcctacgatatgtttagcatcggagaacgtgaagtaaagatattggagatactggacctgattcgatgcactacacaaggccagtctctataggggccctctttgtgtccttagaattacgagcgagattaatgctacaaaggaaagagaaggtcggatgagggtgttagtgacaaatactatgtggtgggccacgaacattacatcacctccacggcacggaggcatggtacgcatatatctttttccctgtttgaccagggggttgatcagacgattcttttgccagtaacagtaacgcgtcagcattgctacgtcatgagtgattcgctagcagaccttgtccacgaataatggcgcacaaactccgcgaacccctcgttcactgaatcaatggttgtgccagcgttggcggtgtgacatacgg_
- _caaccacactggagaacgagtaagggatcgggcgagcggtactctaaatccaaacggtataataagagctccgcgtaaagtcaaggattctgaaagatttgagtgtctcgccgcattccgctacaaagatctggcatattggtcaccttctatcggttaattccgaaaaatttggctaccagatatggatatgagttagatttaaagcggtagtgagaagttccaccacattgcgccgatcagtagaatggcccaaaagtcgcctatctgcctagtcagaaactgaccgagagcgggagtccgtagcactctcaagagagacgttgtatagtgtgcagtcacttcggtgccctactgcgtaacctggggtccagccggccaatgcgggtcggcgtcggacgatacgtgcagctacgctaaaactcccagagggaggcagacaccaaggggtcaccatccagtgccacaaagagcctataatggttggatggcttcttattataaaagaaggagagcataactgcggtggtggtaggtttacaatccagcgagccgggcgtcgtactgattagagcatataaacctggattaatcaacacccttcatcacggctcgattccatcggacggcagacgaaagcagactggcttttgcggcacggggatatgcggtaagccaggataagaacaacattttacttcgcaaatgacctggtgcgcttttacgacaataataggtcgtttttgggaagtcacgggtcggcggattcgggatcagcgggttatctagatcggcgcgtttagcaagggtgccgcaggccgtactgtactattgacacttaatacccgtactaatggatgaacagcgttctaatactgtcacggtacctcatgcatgacctagaacaagtccatatcgaagcttgttcgagcatcgtgaaaccggccgagcacccggtcttgctactggctcccattatctaacggctaacaagggacc_

# Spis treści

[I. Wstęp](#_Toc128342665)

[&emsp;1. Podział dokumentacji](#_Toc128342666)

[&emsp;2. Organizacja pracy](#_Toc128342667)

[&emsp;3. Proces developmentu](#_Toc128342668)

[&emsp;4. Ogólne spostrzeżenia](#_Toc128342669)

[II. Funkcjonalnośc aplikacji](#_Toc128342670)

[&emsp;1. Interfejs](#_Toc128342671)

[&emsp;2. Analiza sekwencji](#_Toc128342672)

[&emsp;3. Wizualizacja białka](#_Toc128342673)

[&emsp;4. Wykres właściwości fizycznych białka](#_Toc128342674)

[III. Struktura aplikacji](#_Toc128342675)

[&emsp;1. Główna architektura aplikacji](#_Toc128342676)

[&emsp;2. amino_acid_interpreter](#_Toc128342677)

[&emsp;3. amino_acid_plots](#_Toc128342678)

[&emsp;4. amino_acid_visualizer](#_Toc128342679)

[&emsp;5. tests](#5-tests)

# **I. Wstęp**

## 1\. Podział dokumentacji

Dokumentacja została podzielona na 4 główne sekcje:

\- _Wstęp_ – informacje o przebiegu, organizacji oraz indywidualnych odczuciach związanych z pracą nad aplikacją

\- _Funkcjonalność aplikacji_ – „właściwa dokumentacja” określająca sposób użytkowania aplikacji, wraz z wszelkimi informacjami na temat jej działania

\- _Struktura aplikacji_ – sekcja opisująca techniczną architekturę aplikacji, poświęcona w głównej mierze opisie autorskich modułów, z których została utworzona

\- _Źródła_ – artykuły, poradniki, bądź badania, które w szczególny sposób przysłużyły się rozwojowi aplikacji

## 2\. Organizacja pracy

Nietypowa tematyka aplikacji - bioinformatyka zmusiła nas do podziału drużyna na 2 obozy. Wśród nich jeden stanowiły osoby zajmujące się poszukiwaniem informacji na temat aminokwasów, następnie segregacją znalezionych danych, przygotowaniem funkcjonalnych przykładów a także edukacją drugiej części drużyny. Ta odpowiedzialna była za utworzenie funkcjonalnego programu w oparciu o zdobytą wiedzę oraz szablony utworzone przez osoby zajmujące się częścią teoretyczną.

## 3\. Proces developmentu

Aplikacja zaczęła powstawać od końca listopada, a pracę nad nią trwały aż do końca lutego. Wspomniany okres był szczególnie intensywny na początku grudnia, kiedy to aby odpowiedzieć sobie na pytanie jak coś funkcjonuje, musieliśmy najpierw postawić przed sobą dwa zupełnie nowe pytania. Każdy początkowy krok do przodu wymagał od nas dwóch kroków w tył, co pierwotnie sprawiało błędne wrażenie, że zamiast iść do przodu – cofamy się. Wraz ze zdobyciem informacji, przygotowaniem danych do testów oraz czasochłonną edukacją pozostałych członków drużyny, rozpoczął się proces właściwego powstawania aplikacji – wreszcie pojawiły się pierwsze linijki kodu.

Do napisania aplikacji zdecydowaliśmy się posłużyć językiem Python ze względu na jego wszechstronność oraz satysfakcję z pracy. Wadą tego rozwiązania okazała się być wydajność, lecz istotna była dla nas przede wszystkim zabawa. Zdecydowaliśmy jej sobie nie odbierać i użyć języka, w którym każdy się odnajduje. Pełny kształt aplikacja osiągnęła na początku lutego, lecz ilość rzeczy do poprawy, bądź przebudowy wciąż była przytłaczająco duża. Mimo narastającej presji czasu pod koniec lutego aplikacja osiągnęła swój finalny kształt oraz została zabezpieczona przed błędami.

## 4\. Ogólne spostrzeżenia

Wszyscy członkowie drużyny musieli zmierzyć się z ogromnym wyzwaniem, aby zająć się tematem zupełnie dla nas obcym. Zdecydowanie dobrym pomysłem był podział drużyny na dwie podgrupy, gdyż część zawodników naszej drużyny ma naturalną zdolność do przyswajania nowej wiedzy na wszelkie tematy, podczas gdy dla pozostałych temat biologii i chemii to obcy i dość przerażający świat. To rozwiązanie pomogło przydzielić każdemu zajęcie, które sprawia mu najmniej trudności i daje siłę do dalszej pracy. Ostatecznie każdy czuje zadowolenie z wykonanej aplikacji, ponieważ wyzwanie którego się podjęliśmy nie należało do najprostszych. Mówiąc szczerze mogliśmy wybrać coś innego, co wykonalibyśmy po najprostszej linii oporu, jednak to by nas tak nie usatysfakcjonowało. Koniec końcu stworzyliśmy coś z czego jesteśmy niesamowicie dumni, niezależnie czy przyniesie nam to przepustkę do trzeciego etapu czy też nie.

# **II. Funkcjonalnośc aplikacji**

## 1\. Interfejs

![Interfejs](https://i.imgur.com/at0S1Dy.png)

**_A_** – input służący do wczytania sekwencji DNA, bądź RNA

**_B_** – przycisk do importu sekwencji DNA lub RNA z pliku tekstowego, wczytana sekwencja pojawia się w inpucie A

**_C_** – przycisk do wykonania analizy podanego DNA lub RNA. Jest on zablokowany, aż do momentu gdy w inpucie A znajdzie się całkowicie poprawna sekwencja DNA lub RNA

**_D_** – przyciski wyboru ramek odczytu(Frame 1: +1; Frame 2: +2; Frame 3: +3). Stają się one aktywne dopiero po przeanalizowaniu sekwencji za pomocą przycisku C

**_E_** – białka zawarte w danej ramce odczytu. Treść tej sekcji pojawia się dopiero przeanalizowaniu sekwencji, a następnie wybraniu danej ramki. Blok E może być pusty, gdy w danej ramce odczytu nie udało się znaleźć żadnego białka, bądź zawierać listę przeanalizowanych białek

## 2\. Analiza sekwencji

Wprowadź poprawną sekwencję RNA(litery: A,U,C,G) lub DNA(litery: A,T,C,G) ręcznie, bądź wybierz przycisk _„Import”_ aby zaimportować sekwencję z pliku tekstowego. Do momentu aż prawidłowa sekwencja nie pojawi się w inpucie - program nie umożliwi wykonywania dalszej części operacji.

_UWAGA!_

_Wprowadzana sekwencja nie może zawierać żadnych białych znaków(spacji, enterów itp.) ani w inpucie, ani w pliku tekstowym._

![Wczytanie](https://i.imgur.com/jDbD7jT.png)

Po przeanalizowaniu białek należy wybrać jedną z trzech ramek odczytu(Frame 1: +1; Frame 2: +2; Frame 3: +3). Ramka odczytu, definiuje od którego nukleotydu podana sekwencja będzie zamieniana na kodony.

![Analiza](https://i.imgur.com/jDbD7jT.png)

Po wybraniu jednej spośród trzech dostępnych ramek odczytu, pojawiają się zawarte w niej białka. Obok każdego białka będą są dostępne dwa przyciski*: „Visualization”*(wizualizacja białka) oraz *„Plots”(*właściwości fizyczne białka).

![Ramki](https://i.imgur.com/NjTDBV1.png)

## 3\. Wizualizacja białka

Po wczytaniu sekwencji RNA lub DNA, a następnie wybraniu ramki odczytu, pojawia się lista białek wraz z dwoma widocznymi przyciskami obok każdego elementu. Aby wyświetlić wzór strukturalny wybranego białka należy kliknąć w podany obok niego przycisk _„Visualization”_.

![Wizualizacja przycisk](https://i.imgur.com/mLFxBsW.png)

Po kliknięciu pojawia się load screen, który znika w momencie gdy wizualizacja białka jest gotowa do wyświetlenia.

_Uwaga!_

_Im dłuższa sekwencja tym dłuższy czas oczekiwania na wygenerowanie wzoru strukturalnego. W skrajnych przypadkach proces generacji może się wydłużyć nawet do kilku minut._

![Splash screen](https://i.imgur.com/KvlcjJD.png)

Po wygenerowaniu wizualizacji użytkownik otrzymuje rezultat w postaci dwóch wzorów strukturalnych. _Pierwszy_ z nich jest przedstawiony w sposób szablonowy, bez wyszczególnionych aminokwasów, podczas gdy _drugi_ umożliwia rozróżnienie konkretnych aminokwasów we wzorze za pomocą kolorów(legenda po kliknięciu we wzór). Aby uzyskać bardziej szczegółowy widok należy kliknąć w jeden z dwóch wzorów.

Co więcej tuż nad przyciskiem „Save Svgs” znajduje informacja o masie wybranego białka.

![Główna wizualizacja](https://i.imgur.com/TdNdwJZ.png)

Po kliknięciu w pierwszy wzór strukturalny otwiera się okienko przedstawiające wizualizacje w powiększeniu.

![Bazowa wizualizacja](https://i.imgur.com/YBdmalX.png)

Kliknięcie w drugi spośród wzorów również poskutkuje otwarciem okienka wraz z powiększoną wizualizacją, w tym wypadku w prawym górnym rogu widoczna jest legenda, przypisującą kolory konkretnym aminokwasom.

![Kolorowa wizualizacja](https://i.imgur.com/BZ92aDt.png)

Użytkownik ma także możliwość zapisu wygenerowanych wzorów strukturalnych w postaci plików SVG(zawierających kompresję bezstratną). Aby zapisać wzory należy kliknąć w przycisk „Save Svgs” głównego okienka wizualizacji.

![Save Svgs przycisk](https://i.imgur.com/yQ03uKN.png)

## 4\. Wykres właściwości fizycznych białka

W celu analizy właściwości fizycznych białka, należy uprzednio podać poprawną sekwencję RNA lub DNA, następnie ją przeanalizować i wybrać jedną z pośród trzech ramek odczytu. Następnie obok każdego białka w wybranej ramce odczytu pokaże się przycisk „Plots”, który należy kliknąć w celu uzyskania konkretnej analizy właściwości fizycznych białka.

![Wykresy przycisk](https://i.imgur.com/t2KOi2h.png)

Po kliknięciu przycisku pojawi się gotowa analiza właściwości fizycznych białka. Na osi pionowej Y znajdują się wartości, z kolei na osi X pozycje aminokwasów w sekwencji. Nad wykresami znajduje się również informacja o wartości punktu izoelektrycznego.

_Uwaga!_

_Niezwykle krótkie białka(składające się z mniej niż 6 aminokwasów) mogą uniemożliwić jego pełną analizę, dlatego niektóre właściwości nie zostaną obliczone._

![Wykresy główna](https://i.imgur.com/r5hu215.png)

Przedstawiona analiza umożliwia użytkownikowi interakcję. W celu przybliżenia wykresów należy posłużyć się scroll’em myszki.

Ponadto poza przybliżeniem wykresu użytkownik może również przesuwać wykres, w celu skupienia się na interesujących go fragmentach sekwencji. Aby przesunąć wykres należy kliknąć lewy przycisk myszki a następnie przesunąć go w daną stronę(kierunek przesuwania zgodny jest z metodą drag).

![Wykresy przybliżone](https://i.imgur.com/146njz8.png)

# **III. Struktura aplikacji**

## 1\. Główna architektura aplikacji

Aplikacja została podzielona na trzy główne moduły wykonawcze oraz jeden moduł testowy. Każdy z konkretnych modułów odpowiada za inne funkcje:

\- _amino_acid_interpreter_ – analiza wprowadzonej sekwencji RNA lub DNA oraz zwrócenie białek zawartych w podanej sekwencji, wraz z rozróżnieniem na konkretne ramki odczytu

\- _amino_acid_plots_ – algorytmy obliczające wartości właściwości fizycznych dla wybranego białka wraz z architekturą i implemetacją okienka przedstawiającego wyliczone wartości

\- _amino_acid_visualizer_ – generowanie wzorów strukturalnych, a także masy podanego białka, wraz z architekturą okienka oraz jego implementacją

\- _tests_ – testy jednostkowe sprawdzające poprawność zaimplementowanej funkcjonalności

\- _main.py_ – główny plik definiujący interfejs aplikacji

## 2\. amino_acid_interpreter

Moduł odpowiedzialny za analizę otrzymanej sekwencji DNA lub RNA. Zaimplementowano w nim autorski algorytm interpretujący sekwencję w trzech ramkach odczytu, a także zabezpieczający przed wczytaniem niepoprawnych znaków w sekwencji. Jako rezultat zwracany jest słownik zawierający białka w konkretnych ramkach odczytu.

TECH STACK: Python

## 3\. amino_acid_plots

Moduł implementujący interfejs umożliwiający wgląd w konkretne właściwości fizyczne białka, jak również interakcję z uzyskanymi wynikami(przybliżenie i przesuwanie wykresów). Ponadto zawiera on algorytmy obliczające właściwości fizyczne dla danego białka. Wyszczególniony moduł podzielony jest na dwa podmoduły:

\- _analysis_tools_ – zawierający definicję algorytmów obliczających właściwości fizyczne

\- _plots_tools_ – zawierający definicję algorytmów umożliwiających interakcje z wykresem

TECH STACK: Python, PySide6, Matplotlib

## 4\. amino_acid_visualizer

Moduł generujący wizualizację białka, a także interfejs graficzny umożliwiający wgląd w jego dokładną strukturę. Zawiera on również algorytm obliczającą masę białka. Moduł generuje strukturę jako plik SVG, dzięki czemu użytkownik ma możliwość zapisu go na własnym urządzeniu.

TECH STACK: Python, PySide6, Rdkit, Pickachu, Pickachu-Chem

## 5\. tests

Moduł odpowiedzialny za przeprowadzenie testów jednostkowych sprawdzających poprawność wykonywanej aplikacji.

TECH STACK: Unittest

## Autorzy

- [Jakub Kowal](https://github.com/KubiO24)
- [Michał Dubrowski](https://github.com/majkelEXE)
- [Igor Białek](https://github.com/IgorBialek)
