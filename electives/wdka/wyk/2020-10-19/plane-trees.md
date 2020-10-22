# Przykładowe zastosowanie — Plane Trees

*(2020-10-19)*

- [Drzewa uporządkowane](#drzewa-uporządkowane)
- [Klasa kombinatoryczna](#klasa-kombinatoryczna)

---

## Drzewa uporządkowane

Drzewa takie, w których zachowujemy orientację całego drzewa\
![](plane-trees-orientacja.png)\
i dokładną pozycję każdego z węzłów.

Nie chodzi nam o drzewa w rozumieniu grafów.

Lista możliwych drzew dla liczby węzłów $[0;4]$:\
![](plane-trees-lista.png)


---

## Klasa kombinatoryczna

Spójrzmy na drzewa uporządkowane nieco „z góry”:\
![](plane-trees-z-góry.png)

Można zauważyć, że każde drzewo jest zbudowane z korzenia oraz z pewnej liczby poddrzew.

$$
\mathcal{T} \cong \mathcal{Z} \times \operatorname{SEQ}(\mathcal{T})
$$

czyli mamy OGF: $T(z) = z \cdot \frac{1}{1 - T(z)}$
- $T(z)(1-T(z)) = z$
- $(T(z))^2 - T(z) + z = 0$
    - $\bold{T(z) = \frac{1}{z}\left( 1 - \sqrt{1 - 4z} \right)}$
    - $\sout{T(z) = \frac{1}{2}\left( 1 + \sqrt{1 - 4z} \right)}$

Możemy też rozwinąć tę OGF:\
$T(z) = \sum_{n\ge1} \frac{1}{n} \binom{2n-2}{n-1}2^n$

---

Możemy też podejść do sprawy nieco inaczej:\
$T^{(i)}$ — klasa drzew o głębokości $<i$
- $T^{(1)} = \mathcal{Z} \times \operatorname{SEQ}(\emptyset)$
- $T^{(2)} = \mathcal{Z} \times \operatorname{SEQ}(\mathcal{T}^{(1)})$
- $T^{(3)} = \mathcal{Z} \times \operatorname{SEQ}(\mathcal{T}^{(2)})$

wizualnie:\
![](plane-trees-klasy.png)

- $\mathcal{T}^{(i)} \subseteq \mathcal{T}^{(i+1)}$
- $\bigcup_{i=1}^{\infty} \mathcal{T}^{(i)} \cong \lim_{i\to\infty} \mathcal{T}^{(i)}$
- $\lim_{i\to \infty} T^{(i)}(z) = T(z)$

---
