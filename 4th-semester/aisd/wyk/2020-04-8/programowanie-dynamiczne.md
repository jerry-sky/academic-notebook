# Programowanie dynamiczne
*(2020-04-8)*

## Zarys

Programowanie dynamiczne jest kolejną metodologią budowy algorytmów pozwalająca na rozwiązywanie szerokiej gamy problemów (często tam gdzie [D&C](../2020-03-9/divide-and-conquer.md) nie może być użyta) choć głównie jest stosowana do tzw. **problemów optymalizacyjnych**.\
Niestety przez jej ogólność rozwiązania nie muszą mieć optymalnej złożoności obliczeniowej.

## How does it work

Podobnie jak w D&C w programowaniu dynamicznym rozwiązujemy zadany problem dzieląc go na pod-problemy, a następnie łączymy je. Różnica natomiast polega na tym, że **w metodologii D&C pod-problemy są niezależne**, a w **programowaniu dynamicznym pod-problemy mogą zależeć od siebie** (wykorzystuje się to zapamiętując rozwiązania pod-problemów i wykorzystując je w innych miejscach).

## Przykład #1

Problem: [Znalezienie najkrótszej ścieżki w skierowanym grafie acyklicznym](najkrótsza-ścieżka-dag.md) ([DAG](https://en.wikipedia.org/wiki/Directed_acyclic_graph)).

## Przykład #2

Problem: [Najdłuższy podciąg rosnący](najdłuższy-podciąg-rosnący.md).

## Przykład #3

Problem: [Longest Common Subsequence (LCS)](../2020-04-20/longest-common-subsequence.md).

## Przykład #4

Problem: `Edit-distance` — znalezienie odpowiednio zdefiniowanej odległości pomiędzy dwoma ciągami. Jest to problem, który również można rozwiązać przy pomocy programowania dynamicznego w stosunkowo podobny sposób jak problem [LCS](#przyk%c5%82ad-3).

[More here (Chapter 6.3)](http://algorithmics.lsi.upc.edu/docs/Dasgupta-Papadimitriou-Vazirani.pdf)

## Summary

Kluczowa własność metodologii programowania dynamicznego: rozwiązując zadany problem jesteśmy w stanie zdefiniować:
- zbiór pod-problemów
- kolejność tych pod-problemów
- relację pomiędzy pod-problemami, która pozwala rozwiązać większy (późniejszy w zdefiniowanej kolejności) pod-problem mając rozwiązania mniejszych (wcześniejszych w zdefiniowanej kolejności) pod-problemów

    W przypadku [problemu znalezienia najkrótszej ścieżki w DAG-ach](#przyk%c5%82ad-1) relacją tą jest:
    $d(v_s,v) = \min\{d(v_s,u) + c(u,v): (u,v) \in E\}$.

    W przypadku [problemu problemu najdłuższego podciągu rosnącego](#przyk%c5%82ad-2) relacją tą jest:
    $L(i) = 1 + \max\{L(j): (j,i) \in E\}$.

## More

Więcej na temat programowania dynamicznego:
- [Chapter 6](http://algorithmics.lsi.upc.edu/docs/Dasgupta-Papadimitriou-Vazirani.pdf)
- [aisd05.pdf](https://drive.google.com/drive/folders/0B83LMR1NBoUXLXdYZ2hsNFBqTTA)
