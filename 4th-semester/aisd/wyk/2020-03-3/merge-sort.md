# Merge Sort
2-03-2020

## Funkcja $MergeSort(A, n)$

```
if n == 1 then done
else
  B = MergeSort( A[ 1,..., floor(n/2) ] )
  C = MergeSort( A[ floor(n/2), ..., n ] )
  merge(B, C)

```

### Example

```
[10] [2] [5] [3] [7] [13] [1] [6]
   \/       \/     \/        \/
 [2,10]   [3,5]  [7,13]     [1,6]
 ...
 [1, 2, 3, 5, 6, 7, 10, 13]
```

## Funkcja $merge$

### Example
$merge( \{2,7,13,20\}, \{1,9,11,12\} )$:

| B     | C         |
| ----- | --------- |
| **2** | ~~**1**~~ |
| 7     | 9         |

---
| B         | C         |
| --------- | --------- |
| ~~**2**~~ | ~~**1**~~ |
| 7         | 9         |

---
| B         | C         |
| --------- | --------- |
| ~~**2**~~ | ~~**1**~~ |
| ~~**7**~~ | 9         |

---
| B         | C         |
| --------- | --------- |
| ~~**2**~~ | ~~**1**~~ |
| ~~**7**~~ | ~~**9**~~ |

---
| B         | C          |
| --------- | ---------- |
| ~~**2**~~ | ~~**1**~~  |
| ~~**7**~~ | ~~**9**~~  |
| 13        | ~~**11**~~ |
itd...

$output = \{ 1, 2, 7, 9, 11, 12, 13, 20 \}$

## Właściwości

1. `merge` ma złożoność $O(n)$ dla input'u wielkości $n$
$$
\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}
\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}
T(n) = T( \floor{\frac{n}{2}} ) + T( \ceil{\frac{n}{2}} ) + O(n)
$$

$$
\widetilde{T}(n) = 2 T(\frac{n}{2}) + O(n)
$$
$$
\widetilde{T}(1) = O(1)
$$

## Nierekurencyjna wersja

`iterativeMergeSort(A, n)`\
`inject(Q, x)` - działa jak `push` na liście `Q`\
`eject(Q)` - działa jak `pop` na liście `Q`


```
Q = []
for i = 1 to n
  inject(Q, A[i])
while |Q| > 1
    inject(Q, merge(eject(Q), eject(Q)))
return eject(Q)
```

### Example

$Q = \{10, 2, 5, 3, 7, 13, 1, 6\}$

$Q$:\
`[10] [2] [5] [3] [7] [13] [1] [6]`\
`[5] [3] [7] [13] [1] [6] [2,10]`\
`[7] [13] [1] [6] [2,10] [3,5]`\
`[1] [6] [2,10] [3,5] [7,13]`\
`[2,10] [3,5] [7,13] [1,6]`\
`[2,3,5,10] [7,13] [1,6]`\
`[2,3,5,7,10,13] [1,6]`\
`[1,2,3,5,6,7,10,13]`\
*done.*

