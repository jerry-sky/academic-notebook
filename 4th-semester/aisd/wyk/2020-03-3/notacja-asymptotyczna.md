# Notacja asymptotyczna
*(2020-03-2)*

## Duże $O$

$f,g: \natnums \to \reals$

$$
f(n) = O\big( g(n) \big) \equiv
\big(~
  \exists{c}~\exists{n_0}~\forall{n>n_0}:
  \big|f(n)\big| \le c \big|g(n)\big|
~\big)
$$

### Example $O$ #1

Dla
$$
f(n) = n^3 + O(n^2) \equiv
\exists{h(n)} = O(n^2)
$$
takie że
$$
f(n) = n^3 + h(n)
$$

### Example $O$ #2

$$
f(n) = 10^{10}n + O\big(ln(n)\big) = O(n)
$$

---
## Duże $\Omega$

$$
f(n) = \Omega\big(g(n)\big) \equiv
\big(~
  \exists{c}~\exists{n_0}~\forall{n\ge{n_0}}: c|g(n)| \le |f(n)|
~\big)
$$

### Example $\Omega$

$$
\sqrt{n} = \Omega\big(\log_2(n)\big)
$$
$$
\sqrt{n} \neq O\big(\ln(n)\big)
$$

---
## Duże $\Theta$

$$
f(n) = \Theta\big(g(n)\big) \equiv f(n) = O\big(g(n)\big) \land f(n) = \Omega\big(g(n)\big)
$$
$$
\equiv \exists{c_1, c_2} \forall{n\ge{n_0}}: c_1\big|g(n)\big| \le f(n) \le c_2 \big|g(n)\big|
$$

---
## Małe $o$

$$
f(n) =
o\big(g(n)\big) \equiv
\big(~
  \forall{c}~\exists{n_0}~\forall{n\ge{n_0}}: \big|f(n)\big| \le c\big|g(n)\big|
~\big)
$$

### Example $o$

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

---
## Mała $\omega$

$$
f(n) = \omega\big(g(n)\big) \equiv
\big(~
  \forall{c}~\exists{n_0}~\forall{n\ge{n_0}}:
  c\big|g(n)\big| \le \big|f(n)\big|
~\big)
$$


