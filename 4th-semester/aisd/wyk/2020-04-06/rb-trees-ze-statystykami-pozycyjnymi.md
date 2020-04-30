# Rozszerzone RB-Trees
*(2020-04-06)*

## Goal

Mając dynamiczny zbiór danych (dane będą usuwane i dodawane) chcemy szybko wyznaczyć $i$tą statystykę ($i$ty najmniejszy element) oraz zwracać stat. poz. zadanego elementu.

## Steps

1. Używamy [RB-Trees](../2020-03-30/red-black-tree.md) jako, że chcemy osiągnąć złoż. oblicz. $O(\log(n))$.
2. Do definicji węzła dodajemy $\text{size}$ gdzie dla węzłów przechowujących wartość $\text{size}=1$ a dla liści $\text{NIL}$ mamy $\text{size}=0$.

    Wówczas dla węzła $x$ w RB-Tree mamy $x.\text{size} = x.\text{left}.\text{size} + x.\text{right}.\text{size} + 1$ jeśli $x$ nie jest $\text{NIL}$.

3. Wykonując operacje dodawania/ usuwania węzłów RB-Tree musimy pamiętać o aktualizowaniu rozmiarów pod-drzew, których rozmiar ulega zmianie (zwiększanie/ zmniejszanie $\text{size}$ pod-drzewa jeszcze przed rekonstrukcją drzewa).

    Dodatkowo, musimy zapewnić, że rekonstrukcja drzewa nadal będzie wykonywała się w asymptotycznie tej samej złożoności obliczeniowej. Rekonstrukcja RB-Tree przywracająca jego własności polega na wykonywaniu procedur [$\text{Recolour}(x, \text{colour})$](../2020-03-30/red-black-tree.md#mathrmrecolorx-color), [$\mathrm{Rotate_{right}}(T,x)$ oraz $\mathrm{Rotate_{left}}(T,x)$](../2020-03-30/red-black-tree.md#mathrmrotaterighttx-mathrmrotatelefttx) odpowiednią liczbę razy.\
    W standardowym RB-Tree procedury te mają złożoność $O(1)$. Zatem aby wzbogacona struktura danych zachowała asymptotaycznie złożoności struktury podstawowej musimy pokazać, że procedury te możemy wykonać w złożoności $O(1)$ zachowując odpowiednie wartości pól $\mathrm{size}$ w węzłach drzewa.

      1. $\mathrm{Recolour}(x, \mathrm{colour})$ — procedura ta zmienia kolor węzła, ale nie modyfikuje rozmiaru pod-drzewa zaczepionego w węźle $x$, więc nie jest wymagana aktualizacja poza $\mathrm{size}$ w żadnym węźle drzewa.
      2. $\mathrm{Rotate_{right}}(T,x)$, $\mathrm{Rotate_{left}}(T,x)$ — rotacja nie zmienia rozmiaru pod-drzewa zaczepionego w korzeniu rotowanego pod-drzewa, ale może zmieniać rozmiar nowo powstałego pod-drzewa. Zauważmy, że musimy obliczyć rozmiar jednego nowo-powstałego pod-drzewa (powstaje ono przez przeniesienie więzła $x$ do prawego/ lewego pod-drzewa i przypięcie reszty pod-drzew pod nim) i możemy do tego wykorzystać wzór: $x.\mathrm{size} = x.\mathrm{left}.\mathrm{size} + x.\mathrm{right}.\mathrm{size} + 1$.\
      Ważne jest, że zmiana rozmiaru pod-drzewa odbywa się lokalnie i nie trzeba uaktualniać rozmiarów pod drzewa w węzłach oddalonych od rotowanego węzła. Złożoność obliczeniowa tak zmodyfikowanej operacji rotacji pozostaje $O(1)$.

4. Dodajemy nowe operacje:

### `OS-Select`
`OS-Select`$(\mathrm{root}, i)$ — operacja zwracająca $i$ty najmniejszy element zbioru zawartego w RB-Tree zaczepionym w węźle $\mathrm{root}$.

```
OS-Select(x, i)
  k = x.left.size + 1
  if i == k then return x
  if i < k then return OS-Select(x.left, i)
  else return OS-Select(x.right, i-k)
```

`OS-Select` działa analogicznie jak operacja `Search` na [BSTs](../2020-03-25/binary-search-tree.md) tylko porównuje liczbę elementów mniejszych równych od węzła w którym się znajduje.\
`OS-Select` działa w czasie $O(h) = O(\log n)$

### `OS-Rank`
`OS-Rank`$(\mathrm{root}, x)$ — operacja zwracająca statystykę pozycyjną węzła $x$ w RB-Tree zaczepionym w węźle $\mathrm{root}$.

```
OS-Rank(root, x)
  r = x.left.size + 1
  y = x
  while y != root:
    if y == y.parent.right:
      r += y.parent.left.size + 1
    y = y.parent
  return r
```

`OS-Rank` jest swoistym odwróceniem [`OS-Select`](#os-select) – zliczamy liczbę elementów mniejszych (po lewej stronie w drzewie) na drodze od zadanego węzła do korzenia. `OS-Rank` działa w czasie $O(h) = O(\log n)$.

### Final thoughts

Zauważmy, że jeśli w węzłach drzewa chcielibyśmy przechowywać po prostu statystykę pozycyjną węzła to operacje [`OS-Select`](#os-select) oraz [`OS-Rank`](#os-rank) miałyby złożoność $O(1)$, ale złożoność obliczeniowa operacji modyfikujących RB-Tree byłaby asymptotycznie równa $O(n)$.
