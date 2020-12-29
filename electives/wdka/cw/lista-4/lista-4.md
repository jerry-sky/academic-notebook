---
lang: 'pl'
title: 'Lista-4'
author: 'Jerry Sky'
date: '2020-12-20'
---

---

- [Zadanie 1.](#zadanie-1)
- [Zadanie 2.](#zadanie-2)
- [Zadanie 3.](#zadanie-3)

---

## Zadanie 1.

> Niech struktura $\alpha$ o wadze $3$ będzie etykietowana za pomocą permutacji $2–1–3$. Niech struktura $\beta$ o wadze $2$ będzie etykietowana permutacją $2–1$. Opisz $\alpha \star \beta$.

Mamy:
- $\alpha = 2–1–3$
- $\beta = 2–1$

Wówczas $\alpha \star \beta$ będzie postaci $(a–b–c, d–e)$ gdzie $(a,b,c,d,e)$ jest permutacją na zbiorze $\{1,\dots,5\}$ z zachowaniem porządku:
- $b < a < c$
- $e < d$

Przykładowe elementy:
- $(2–1–3, 5–4)$
- $(3–2–4, 5–1)$
- $(4–3–5, 2–1)$
- $\dots$

Będzie takich kombinacji oczywiście $\binom{|\alpha| + |\beta|}{|\alpha|} = \binom{5}{2}$, bo za każdym razem musimy wybrać względem, której struktury dobierać odpowiednie układy.

---

## Zadanie 2.

> Napisać EGF dla klasy permutacji, które składają się z co najwyżej $5$ cykli.

Rozumiemy klasę permutacji jako zbiór cykli:
$$
\mathcal{P} = \operatorname{SET}\left( \operatorname{CYC}(\mathcal{Z}) \right),
$$
tutaj wprowadzamy ograniczenie na liczbę możliwych cykli:
$$
\mathcal{P}' = \operatorname{SET}_{\le 5}\left( \operatorname{CYC}(\mathcal{Z}) \right).
$$

EGF dla zbioru definiujemy przez funkcję eksponenty — naturalnie możemy ją rozwinąć w sumę:
$$
e^z = \sum_{n\le0} \frac{z^n}{n!}.
$$

Biorąc powyższą równość pod uwagę, jesteśmy w stanie określić EGF dla naszej klasy $\mathcal{P}'$:
$$
P'(z) = \sum_{n=0}^5 \frac{\left( \ln \frac{1}{1-z} \right)^n}{n!},
$$
jako że EGF dla funkcji cykli to logarytm naturalny z funkcji sekwencji funkcji wejściowej, czyli tutaj funkcji EGF dla klasy atomowej $\mathcal{Z}$.

---

## Zadanie 3.

> Napisać EGF dla $k$-suriekcji zbioru $n$-elementowego $N = \{1,\dots,n\}$ na zbiór $r$-elementowy, czyli funkcji takich, że każda wartość ze zbioru $R = \{1,\dots,r\}$ ma przeciwobraz co najmniej $k$-elementowy.

Dla każdego elementu ze zbioru $R$ przypisujemy zbiór (pudełko, urnę), do którego trafiają elementu ze zbioru $N$. Czyli będziemy mieć sekwencję długości $r$ takich pudełek. Co do zbiorów (pudełek) musimy wprowadzić ograniczenie, że mamy przynajmniej $k$ elementów z $N$ w danym pudełku.

Definiujemy klasę kombinatoryczną:
$$
\mathcal{S_k} = \operatorname{SEQ}_{=r}(\operatorname{SET}_{\ge k}(\mathcal{Z}))
$$
oraz odpowiadającej jej EGF:
$$
S_k(z) = \left( \sum_{n\ge0}\frac{z^n}{n!} - \sum_{m=0}^{k-1} \frac{z^m}{m!} \right)^r.
$$
W środku tej funkcji mamy funkcję eksponenty odpowiadającej za EGF dla klasy $\operatorname{SET}$ przy czym odejmujemy te zbiory, gdzie mamy $k-1$ bądź mniej elementów — dlatego też odejmujemy pierwsze $k$ elementów (od $0$ do $k$) sumy rozwinięcia Taylora funkcji eksponenty.

---
