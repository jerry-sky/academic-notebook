# Lista-1 *Wstęp do teorii grafów*

## Index
  - [Zadanie 1](#zadanie-1)

## Zadanie 1

1.
   1. Jeśli $G$ jest spójny to *done*.
   2. *Oth*
      1. Weźmy trójkę wierzchołków $v, w, z$ z grafu $G$ przy czym $v$ oraz $w$ są połączone kiedy $z$ jest w innej składowej niż para $v$ oraz $w$.
      2. W dopełnieniu $\overline{G}$ tracimy połączenie $v$ a $w$, ale uzyskujemy połączenia pomiędzy $v$ a $z$ oraz $w$ a $z$.
      3. Wówczas nadal mamy połączenie pomiędzy $v$ a $w$ poprzez $z$ oraz uzyskujemy połączenie pomiędzy składowymi, które wcześniej były oddzielone.

    $G$:

      <img width="256px" src="lista-1-zadanie-1-graph.png"/>

    $\overline{G}$:

      <img width="256px" src="lista-1-zadanie-1-graph-complement.png"/>
