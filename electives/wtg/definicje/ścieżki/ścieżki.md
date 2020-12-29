---
lang: 'pl'
title: 'Definicje - ścieżki (nie dosłownie)'
author: 'Jerry Sky'
---

---

- [Ścieżka Eulera](#ścieżka-eulera)
- [Cykl Eulera](#cykl-eulera)
- [Ścieżka Hamiltona](#ścieżka-hamiltona)
- [Cykl Hamiltona](#cykl-hamiltona)
- [Bridge](#bridge)

---

## Ścieżka Eulera

W ścieżce Eulera odwiedzamy **każdą krawędź tylko raz**.

W każdym grafie mamy taką ścieżkę jeśli ma w sobie **co najwyżej dwa wierzchołki o $\deg$ równym liczbie nieparzystej**.

## Cykl Eulera

Cykl Eulera jest ścieżką Eulera przy czym **początek i koniec tej ścieżki to ten sam wierzchołek**.

W każdym grafie mamy taką ścieżkę jeśli **każdy z wierzchołków ma $\deg$ równy liczbie parzystej**.

## Ścieżka Hamiltona

W ścieżce Hamiltona odwiedzamy **każdy wierzchołek tylko raz**.

## Cykl Hamiltona

Cykl Hamiltona jest ścieżką Hamiltona przy czym **początek i konieć tej ścieżki to ten sam wierzchołek**.

Graf $G(V,E): |V| = n \ge 3$  gdzie $\forall v \in V: \deg(v) \ge \frac{n}{2}$ jest hamiltonowski.\
*[(Dirac's Theorem)](https://en.wikipedia.org/wiki/Hamiltonian_path#Bondy%E2%80%93Chv%C3%A1tal_theorem)*

## Bridge
*or isthmus, cut-edge or cut arc*

Krawędź po której **usunięciu dostalibyśmy większą liczbę składowych grafu**.

Alternatively, an edge is a **bridge iff it is not contained in any cycle**.
