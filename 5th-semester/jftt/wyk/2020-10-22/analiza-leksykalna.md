# Analiza leksykalna

*(2020-10-22)*

- [1. DEF](#1-def)
- [2. Podstawowe pojęcia](#2-podstawowe-pojęcia)
- [3. Przykład symboli leksykalnych](#3-przykład-symboli-leksykalnych)
- [4. Zapis wzorca](#4-zapis-wzorca)
- [5. Implementacja analizatora leksykalnego](#5-implementacja-analizatora-leksykalnego)
    - [5.1. Złożoność pamięciowa i czasowa automatów skończonych](#51-złożoność-pamięciowa-i-czasowa-automatów-skończonych)
- [6. Koncepcja *FLEX*-a](#6-koncepcja-flex-a)
    - [6.1. Specyfikacja pliku źródłowego](#61-specyfikacja-pliku-źródłowego)
    - [6.2. Podstawowe reguły działania](#62-podstawowe-reguły-działania)
    - [6.3. Przykład programu](#63-przykład-programu)
    - [6.4. Wyrażenia regularne](#64-wyrażenia-regularne)
    - [6.5. Zmienne wbudowane](#65-zmienne-wbudowane)
    - [6.6. Niejednoznaczność](#66-niejednoznaczność)

---

## 1. DEF

Rozbicie ciągu znaków wejściowych na symbole leksykalne (wyrazy posiadające określone znaczenie). Ciąg symboli leksykalnych stanowi wejście dla analizatora składniowego.

---

## 2. Podstawowe pojęcia

1. symbol leksykalny (token)
2. leksem (symbol leksykalny może mieć wiele leksemów)
3. wzorzec (coś w rodzaju wyrażenia regularnego)

---

## 3. Przykład symboli leksykalnych

Weźmy kawałek kodu w `C`:
```c
double sqr(double x)
{
    return x*x;
}
```

| Token                | Leksem   |
| -------------------- | -------- |
| `Identyfikator_typu` | `double` |
| `Identyfikator`      | `sqr`    |
| «`(`»                | `(`      |
| `Identyfikator`      | `x`      |
| «`)`»                | `)`      |
| «`{`»                | `{`      |
| `KW_return`          | `return` |
| `Operator_binarny`   | `*`      |
| «`;`»                | `;`      |
| «`}`»                | `}`      |

---

## 4. Zapis wzorca

- wzorce zapisujemy jako wyrażenia regularne
- składnia wyrażeń rozszerzona, aby umożliwić zwięzły zapis
- w opisie przez wyrażenia regularne używamy następujących priorytetów: gwiazdka Kleen’ego, złożenie, suma

| Symbol leksykalny  | Wyrażenie regularne    |
| ------------------ | ---------------------- |
| `Identyfikator`    | `[a-zA-Z][a-zA-Z0-9]*` |
| «`(`»              | `\(`                   |
| «`{`»              | `\{`                   |
| `Operator_binarny` | `\*`                   |
| `KW_return`        | `return`               |

---

## 5. Implementacja analizatora leksykalnego

- wykorzystanie generatorów analizatorów leksykalnych (np. *LEX*, *FLEX*)
- napisanie analizatora bezpośrednio w jakimś języku programowania

### 5.1. Złożoność pamięciowa i czasowa automatów skończonych

| Automat | Pamięć                  | Czas                                       |
| ------- | ----------------------- | ------------------------------------------ |
| DFA     | $O(2^{\lvert r \rvert})$ | $O(\lvert x \rvert)$                       |
| NFA     | $O(\lvert r \rvert)$    | $O(\lvert x \rvert \cdot \lvert r \rvert)$ |

gdzie:
- $|r|$ — długość wyrażenia regularnego
- $|x|$ — długość łańcucha wejściowego

Jednak implementacja DFA jest duża łatwiejsza, a wielkość zmniejsza się w trakcie minimalizacji.

---

## 6. Koncepcja *FLEX*-a

- generowanie kodu analizatora na podstawie zadanej specyfikacji
- domyślnie analizator jest w języku *C*
- wygenerowany kod źródłowy kompilujemy, jako samodzielny program lub moduł programu
- `yylex()` — funkcja wygenerowana przez *LEX*-a odpowiedzialna za działanie leksera (można ją wykorzystać w innej aplikacji)

`scan.l` $\to$ *flex* $\to$ `scan.c` $\to$ `gcc` $\to$ `scan[.exe]`

---

### 6.1. Specyfikacja pliku źródłowego

1. Sekcja definicji
2. Sekcja reguł przetwarzania, gdzie regułą składa się z dwóch części
    1. wzorca (wyrażenie regularne)
    2. operacji (zapisanej w *C*)
3. Sekcja podprogramów

### 6.2. Podstawowe reguły działania

- niedopasowane znaki są przepisywane na wyjście
- można definiować operacje puste (wzorzec bez reguły przetwarzania)
- znaki specjalne poprzedzamy znakiem `\`
- wzorce zawierające spacej ujmujemy w `""`

---

### 6.3. Przykład programu

```c
%{// sekcja — biblioteki i inne ustawienia w normalnym C
#include<stdio.h>

int yywrap();
int yylex();
int NL=0;
%}
%%// tutaj określamy definicje znaków
^[[:blank:]]*register[[:blank:]]+	;
long[[:blank:]]+int	printf("long");
unsigned[[:blank:]]+int	printf("unsigned int");
signed[[:blank:]]+int	printf("int");
\n			{ printf("\n"); NL++; }
%%
int yywrap() {
    printf("---\n\%d\n",NL);
    return 1;
}
int main() {
    return yylex();
}
```

### 6.4. Wyrażenia regularne

| Wyrażenie | Opis                                                 |
| --------- | ---------------------------------------------------- |
| `^x`      | wzorzec od początku linii                            |
| `x$`      | wzorzec do końca linii                               |
| `xy`      | konkatenacja wzorców                                 |
| `x|y`     | alternatywa wzorców                                  |
| `x*`      | domknięcie zwrotne                                   |
| `x+`      | domknięcie dodatnie                                  |
| `x?`      | opcjonalność (występuje 0 lub 1 raz)                 |
| `x{3}`    | występuje dokładnie trzy razy                        |
| `x{2,4}`  | występuje 2, 3, lub 4 razy                           |
| `x{2,}`   | występuje co najmniej dwa razy                       |
| `(x|y)z`  | nawiasy wyrażają priorytet                           |
| `[a-z]`   | klasa znaków, tu: jeden znak ze zbiour od `a` do `z` |
| `[^a-z]`  | dowolny znak spoza klasy                             |
| `.`       | dowolny znak (poza znakiem `\n`)                     |

---

### 6.5. Zmienne wbudowane

- `yytext` — wskaźnik na ostatnio rozpoznany (dopasowany)
- `yyleng` — długość dopasowanego leksema

---

### 6.6. Niejednoznaczność

*Co zrobi LEX jeśli tekst może się dopasować do kilku wzorców?*

Stosujemy zasady:
1. Zasada najdłuższego dopasowania
2. Zasada wcześniejszego dopasowania

---
