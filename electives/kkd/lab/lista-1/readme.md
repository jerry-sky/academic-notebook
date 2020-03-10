# Lista-1

[kod](lista-1.ts)

## Entropia warunkowa

$P(y|x) = \frac{P(y~\cap~x)}{P(x)} = \frac{|y~\cap~x|}{|x|}$

$I(y|x) = -\log_2(~P(y|x)~)$

$H(Y|x) = \sum_{y \in Y}P(y|x)\cdot I(y|x)$

$H(Y|X) = \sum_{x \in X}P(x)\cdot H(Y|x)$

podstawmy:\
$H(Y|X) = \sum_{x \in X}(~P(x)\cdot \sum_{y \in Y}P(y|x)\cdot I(y|x)~)$\
$H(Y|X) = \sum_{x \in X}(~P(x)\cdot \sum_{y \in Y}P(y|x)\cdot (-\log_2(~P(y|x))~)$

mamy przecież:
$$
P(x) = \frac{|x|}{|\Omega|}
$$
oraz:
$$
P(y|x) = \frac{P(y \cap x)}{P(x)} = \frac{|y \cap x|}{|x|}
$$
wówczas:
$$
H(Y|X) = \sum_{x \in X}(~\frac{|x|}{|\Omega|}\cdot \sum_{y \in Y}\frac{|y \cap x|}{|x|}\cdot (-\log_2(~\frac{|y \cap x|}{|x|})~)
$$
$$
H(Y|X) = \sum_{x \in X}(~\sum_{y \in Y} \frac{|x|}{|\Omega|} \cdot \frac{|y \cap x|}{|x|}\cdot (-\log_2(~\frac{|y \cap x|}{|x|})~)
$$
$$
H(Y|X) = \sum_{x \in X}(~\sum_{y \in Y} \frac{|y \cap x|}{|\Omega|}\cdot (-\log_2(~\frac{|y \cap x|}{|x|})~)
$$
$$
H(Y|X) = \sum_{x \in X}(~\sum_{y \in Y} \frac{|y \cap x|}{|\Omega|}\cdot (-\log_2(~|y \cap x|)~ + log_2|x|)
$$
$$
H(Y|X) = \sum_{x \in X}(~\sum_{y \in Y} \frac{|y \cap x|}{|\Omega|}\cdot (-\log_2(~|y \cap x|)~ + log_2|x|)
$$

## Zwykła entropia

$$
H(X) = \sum_{x \in X}P(x)\cdot I(x)
$$
przy czym $I(x) = -\log_2 P(x)$
$$
H(X) = \sum_{x \in X}\frac{|x|}{|\Omega|}\cdot (-\log_2 \frac{|x|}{|\Omega|})
$$
$$
H(X) = \frac{1}{|\Omega|}\cdot\sum_{x \in X}|x|\cdot (-\log_2 \frac{|x|}{|\Omega|})
$$
$$
H(X) = \frac{1}{|\Omega|}\cdot\sum_{x \in X}|x|\cdot (-\log_2 |x| + log_2 |\Omega|)
$$
$$
H(X) = \frac{1}{|\Omega|}\cdot\sum_{x \in X}|x|\cdot (-\log_2 |x|) + \frac{1}{|\Omega|} \cdot log_2 |\Omega| \cdot \sum_{x \in X} |x|)
$$
$$
H(X) = \frac{1}{|\Omega|}\cdot\sum_{x \in X}|x|\cdot (-\log_2 |x|) + log_2 |\Omega|
$$
