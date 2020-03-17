# Sortowanie
*(2020-02-26)*

## Input
$\sigma = (a_1, a_2, ... a_n) = A$

## Output
permutacja ciągu $\sigma$ taka że\
$a_{\sigma(1)} \le a_{\sigma(2)} \le ... \le a_{\sigma(n)}$

---

## Insertion sort $(A,n)$

1. $8,\underline2,4,9,3,6$
2. `temp = 2`
3. $8,8,4,9,3,6$
4. $2,8,\underline4,9,3,6$
5. `temp = 4`
6. $2,8,8,9,3,6$
7. $2,4,8,9,3,6$
8. $2,4,8,9 | \underline3,6$
9. `temp = 3`
10. $2,4,8,9 | 9,6$
11. $2,4,8,8 | 9,6$
12. $2,4,4,8 | 9,6$
13. $2,3,4,8 | 9,6$
14. ...
15. $2,3,4,6,8,9$

