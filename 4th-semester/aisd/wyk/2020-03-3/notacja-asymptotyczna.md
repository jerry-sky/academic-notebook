# Notacja asymptotyczna
2-03-2020

## Duże $O$

$f,g: \natnums \to \reals$

$$
f(n) = O( g(n) ) \equiv
(
  \exists{c}~\exists{n_0}~\forall{n>n_0}:
  |f(n)| \le c |g(n)|
)
$$

### Example

Dla
$$
f(n) = n^3 + O(n^2) \equiv
\exists{h(n)} = O(n^2)
$$
takie że
$$
f(n) = n^3 + h(n)
$$

$$
f(n) = 10^{10}n + O(ln(n)) = O(n)

$$

## Duże $\Omega$

$$
f(n) = \Omega(g(n)) \equiv (\exists{c}~\exists{n_0}~\forall{n\ge{n_0}}: c\cdot|g(n)| \le |f(n)|)
$$

### Example

$$
\sqrt{n} = \Omega(\log_2(n))
$$
$$
\sqrt{n} \neq {O(\ln(n))}
$$

## Duże $\Theta$

$$
f(n) = \Theta(g(n)) \equiv f(n) = O(g(n)) \land f(n) = \Omega(g(n))
$$
$$
\equiv \exists{c_1, c_2}\forall{n\ge{n_0}}: c_1|g(n)| \le f(n) \le c_2 |g(n)|
$$

## Małe $o$

$$
f(n) = o(g(n)) \equiv \forall{c}\exists{n_0}\forall{n\ge{n_0}}: |f(n)| \le c|g(n)|
$$

### Example

$$
13n^2 = O(n^2)
$$
$$
13n^2 = o(n^3)
$$
ale
$$
13n^2 \not ={o(n^2)}
$$

## Mała $\omega$

$$
f(n) = \omega(g(n)) \equiv (
  \forall{c}\exists{n_0}\forall{n\ge{n_0}}:
  c|g(n)| \le |f(n)|
)
$$


