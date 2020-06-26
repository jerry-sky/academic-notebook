# Klauzule Horna

Klauzulami Horna nazywamy zbiór formuł logicznych wykorzystywany do przeprowadzenia wnioskowania np. w automatycznym dowodzeniu twierdzeń i systemach eksperckich.

- [Input](#input)
  - [Przykład klauzul](#przykład-klauzul)
- [Def Literał](#def-literał)
- [Rodzaje formuł](#rodzaje-formuł)
  - [1. Formuły implikacyjne](#1-formuły-implikacyjne)
    - [Przykłady formuły implikacyjnej](#przykłady-formuły-implikacyjnej)
  - [2. Formuły negacyjne](#2-formuły-negacyjne)
    - [Przykład formuły negacyjnej](#przykład-formuły-negacyjnej)
- [Cel](#cel)
- [Przykładowy algorytm](#przykładowy-algorytm)
  - [Poprawność algorytmu](#poprawność-algorytmu)

## Input

Podstawowym obiektem jest zmienna logiczna przyjmująca wartość $\mathrm{True}$ lub $\mathrm{False}$.

### Przykład klauzul

Dla przykładu, zmienne $x,y,z$ mogą oznaczać następujące możliwości:
- $x \equiv$ morderstwo miało miejsce w kuchni
- $y \equiv$ lokaj jest niewinny
- $z \equiv$ pułkownik spał o 8 wieczorem
- $u \equiv$ pułkownik jest niewinny
- $w \equiv$ morderstwo odbyło się o 8 wieczorem

## Def Literał

Literałem nazywamy zmienną np. $x$ lub jej negację $\overline{x}$.

## Rodzaje formuł

### 1. Formuły implikacyjne
*deklaracja procedury*

Lewa strona implikacji jest koniunkcją pozytywnych literałów (niezanegowanych zmiennych), prawa strona implikacji składa się z jednego pozytywnego literału. Formuła taka odpowiada stwierdzeniom: jeśli warunki po lewej stronie zachodzą to stwierdzenie po prawej stronie również musi być prawdziwe.

#### Przykłady formuły implikacyjnej

1. *rozszerzenie [wcześniejszego przykładu](#przykład-klauzul)*\
Formuła $(z \land w) \Rightarrow u$ może oznaczać: jeśli pułkownik spał o 8 wieczorem i morderstwo odbyło się o 8 wieczorem to pułkownik jest niewinny.
2. Możemy zapisać również implikację z pustą lewą stroną, np. $\Rightarrow x$ oznaczającą po prostu, że $x$ jest prawdą.

### 2. Formuły negacyjne
*formuła celu*

Formuła negacyjna jest alternatywną negatywnych literałów (zanegowanych zmiennych).

#### Przykład formuły negacyjnej
*rozszerzenie [wcześniejszego przykładu](#przykład-klauzul)*\
Dla przykładu $(\overline{u} \lor \overline{y})$ może oznaczać: obie postacie nie mogą być niewinne.

---

## Cel

Celem znalezienie takiego wartościowania zmiennych występujących w klauzuli Horna, aby wszystkie jej formuły miały wartościowanie spełniające.\
Zauważmy, że [dwa rodzaje formuł](#rodzaje-formuł) sprzyjają nadawaniu różnych wartościowań zmiennym:
- [formuły implikacyjne](#1-formuły-implikacyjne) sprzyjają nadawaniu zmiennym wartości $\mathrm{True}$ aby były spełnione,
- [formuły negacyjne](#2-formuły-negacyjne) sprzyjają nadawaniu zmiennym wartości $\mathrm{False}$ aby były spełnione.

## Przykładowy algorytm

Użyjmy następującego zachłannego rozwiązania problemu znalezienia wartościowania spełniającego:

`Horn`$(\text{klauzula wejściowa})$:
1. ustaw wartość wszystkich zmiennych na $\mathrm{False}$
2. `while` istnieje niespełniona implikacja:
   1. ustaw zmienną po prawej stronie implikacji na $\mathrm{True}$
3. `if` wszystkie formuły negacyjne są spełnione:
   1. `return` wartościowanie spełniające wejściową klauzulę
4. `else`:
   1. `return` wartościowanie spełniające nie istnieje

### Poprawność algorytmu

Jeśli algorytm zwróci wartościowanie spełniające to nie ma czego dowodzić, bo wartościowanie to rzeczywiście musi spełniać wejściową klauzulę Horna.\
Zatem jedyny przypadek, który wymaga udowodnienia, to ten kiedy algorytm zwróci, że wartościowanie spełniające wejściową klauzulę Horna nie istnieje. Musimy pokazać, że rzeczywiśćie nie da się znaleźć innego przypisania wartości zmiennym, które spełni wejściową klauzulę.\
W tym celu zauważmy, że nasze zachłanne nadawanie wartości $\mathrm{True}$ zmiennym w pętli `while` spełnia następujący niezmiennik:
> Jeśli zmienna ustawiona na $\mathrm{True}$ w pętli `while`, to musi ona mieć wartość $\mathrm{True}$ w każdym spełniającym wartościowaniu.

Zatem, jeśli wartościowanie znalezione po pętli `while` nie spełnia wszystkich formuł negacyjnych wejściowej klauzuli, to nie istnieje takie wartościowanie.
