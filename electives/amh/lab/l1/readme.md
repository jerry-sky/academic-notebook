# Lista 1

## Zadanie 1

[code](z1/main.cpp)

(a) `HappyCat`:
$$
h(\overline{x})=\left[\left(||\overline{x}||^2 - 4\right)^2\right]^\frac{1}{8} + \frac{1}{4}\left(\frac{1}{2}||\overline{x}||^2+\sum_{i=1}^{4}x_i\right)+\frac{1}{2}
$$
$$
\overline{x} = (x_1,~x_2,~x_3,~x_4)
$$
$$
||\overline{x}|| := \sqrt{x_1^2 + \dotsb + x_n^2}
$$

(b) `Griewank`:
$$
g(\overline{x}) = 1 + \sum_{i+1}^{4}\frac{x^2_i}{4000} - \prod_{i=1}^{4}\cos\left(\frac{x_i}{\sqrt{i}}\right)
$$
$$
\overline{x} = (x_1,~x_2,~x_3,~x_4)
$$

## Zadanie 2

[code](z2/main.py)

## Zadanie 3

[code](z3/main.py)
