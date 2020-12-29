---
lang: 'pl'
title: 'Definicje — grafy'
author: 'Jerry Sky'
---

---

- [Graf spójny](#graf-spójny)
- [Graf dwudzielny](#graf-dwudzielny)

---

## Graf spójny

Graf $G(V,E)$ jest spójny jeśli $\forall v_i,v_j \in V$ istnieje droga od $v_i$ do $v_j$

## Graf dwudzielny

Graf $G(V,E)$ jest dwudzielny jeśli $V$ możemy podzielić na dwa podzbiory $A,B: A \dot\cup B = V$ przy czym wierzchołki z każdego z tych podzbiorów mogą się łączyć tylko z wierzchołkami z drugiego podzbioru, nie pomiędzy sobą.

Innymi słowy, graf w którym każdy cykl ma parzystą długość.

![bipartite graph](graphs/bipartite-graph.png)

[dowód z wykładu](../../wyk/2020-03-11/2020-03-11.md#grafy-dwudzielne)
