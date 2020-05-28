# Lista-2
*Grafy Eulerowskie i ścieżki Hamiltona*

## Zadanie 21

> 1. Dla jakich $n$ grafy $K_n$ są eulerowskie; dla jakich $n$ są one hamiltonowskie?
> 2. Dla jakich par liczb $n, m$ grafy $K_{n,m}$ są eulerowskie lub zawierają ścieżką Eulera?
> 3. Dla jakich par liczb $n, m$ grafy $K_{n,m}$ są hamitonowskie lub zawierają ścieżką Hamiltona?

1. Grafy $K_n$ są eulerowskie dla $n$ nieparzystych, bo jeśli $n-1$ jest parzyste mamy pewność, że stopień każdego wierzchołka jest parzysty przez co mamy graf eulerowski. Graf $K_n$ jest hamiltonowski dla wszystkich $n$.
2. ×
   1. Znowu, wszystkie wierzchołki muszą mieć parzystą liczbą wierzchołków (w przypadku cyklu Eulera). Każdy wierzchołek $v$ ma $\deg(v) = m$ bądź też $\deg(v) = n$. Przez co obie te liczby muszą być parzyste.\
   Specjalnym przypadkiem jest tutaj graf $K_{1,2}$, który oczywiście jest jednocześnie grafem $K_3$, ale ten graf został rozważony w punkcie (1.) powyżej.
   2. W przypadku ścieżki Eulera musimy mieć dwa wierzchołki o nieparzystym $\deg$ (żeby z jednego wyjść a na drugim skończyć). W takim wypadku musimy mieć sytuację gdzie $m = 2$ oraz $n$ jest nieparzyste.\
   Specjalnym przypadkiem byłby graf $K_{1,1}$, który jest jednocześnie grafem $K_2$.
3. ×
   1.
