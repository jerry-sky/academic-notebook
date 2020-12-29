---
lang: 'pl'
title: 'Kompilatory — Wprowadzenie'
author: 'Jerry Sky'
date: '2020-10-08'
keywords: 'wykład, jftt, pwr, kompilator, wprowadzenie, analiza, leksykalna, składniowa, semantyczna, symbol, symbole, kod, pośredni, wynikowy, kompilatora, przód, tył'
---

---

- [1. DEF: Kompilator](#1-def-kompilator)
- [2. Kompilacja typu analiza-synteza](#2-kompilacja-typu-analiza-synteza)
    - [2.1. Narzędzia dokonujące analizy](#21-narzędzia-dokonujące-analizy)
    - [2.2. Programy przypominające kompilatory](#22-programy-przypominające-kompilatory)
- [3. Kontekst kompilatora](#3-kontekst-kompilatora)
- [4. Fazy kompilatora](#4-fazy-kompilatora)
    - [4.1. Analiza leksykalna](#41-analiza-leksykalna)
    - [4.2. Analiza Składniowa](#42-analiza-składniowa)
    - [4.3. Analiza semantyczna](#43-analiza-semantyczna)
    - [4.4. Zarządzanie tablicą symboli](#44-zarządzanie-tablicą-symboli)
    - [4.5. Wykrywanie i zgłaszanie błędów](#45-wykrywanie-i-zgłaszanie-błędów)
    - [4.6. Generowanie kodu pośredniego](#46-generowanie-kodu-pośredniego)
    - [4.7. Optymalizacja kodu](#47-optymalizacja-kodu)
    - [4.8. Generowanie kodu wynikowego](#48-generowanie-kodu-wynikowego)
- [5. Grupowanie faz](#5-grupowanie-faz)
    - [5.1. Przód kompilatora](#51-przód-kompilatora)
    - [5.2. Tył kompilatora](#52-tył-kompilatora)

---

## 1. DEF: Kompilator

*Program czytający kod napisany w języku źródłowym i tłumaczący go na równoważny kod w języku wynikowym.*

$$
\text{Program źródłowy} \rightarrow \underset{\underset{\text{Komunikaty o błędach}}{\downarrow}}{\text{Kompilator}} \rightarrow \text{Program wynikowy}
$$

---

## 2. Kompilacja typu analiza-synteza

1. Analiza — rozłożenie programu na części składowe i stworzenie jego pośredniej reprezentacji.
2. Synteza — przekształcenie reprezentacji pośredniej na program wynikowy.

---

### 2.1. Narzędzia dokonujące analizy

- edytory strukturalne
- formatory kody programu
- kontrolery statyczne
- interpretery

### 2.2. Programy przypominające kompilatory

- formatory tekstu
- kompilatory do układów scalonych

---

## 3. Kontekst kompilatora

1. Szkieletowy program źródłowy
2. *Preprocesor*
3. Program źródłowy
4. *Kompilator*
5. Program w asemblerze
6. *Assembler*
7. Przemieszczalny kod maszynowy
8. *Konsolidator $\leftarrow$ Biblioteki*
9. Bezwzględny kod maszynowy

---

## 4. Fazy kompilatora

1. *Program źródłowy*
2. [Analizator leksykalny](#41-analiza-leksykalna)
3. [Analizator składniowy](#42-analiza-składniowa)
4. [Analizator semantyczny](#43-analiza-semantyczna)
5. [Generator kodu pośredniego](#46-generowanie-kodu-pośredniego)
6. [Optymalizacja kodu](#47-optymalizacja-kodu)
7. [Generator kodu](#48-generowanie-kodu-wynikowego)
8. *Program wynikowy*

*~w tle: [Obsługa błędów](#45-wykrywanie-i-zgłaszanie-błędów) oraz [Zarządzanie tablicą symboli](#44-zarządzanie-tablicą-symboli)~*

### 4.1. Analiza leksykalna
Ciąg znaków składający się na program źródłowy jest przekształcany w ciąg tokenów (symboli leksykalnych).

### 4.2. Analiza Składniowa
Grupowanie symboli leksykalnych programu źródłowego w wyrażenia gramatyczne (tworzenia drzewa wyprowadzenia).

### 4.3. Analiza semantyczna
Kontrola programu pod względem poprawności semantycznej (np. kontrola typów) i zbierani informacji do generowania kodu.

### 4.4. Zarządzanie tablicą symboli
Zapamiętywanie identyfikatorów używanych w programie źródłowym i zbieranie informacji o różnych atrybutach tych identyfikatorów.

### 4.5. Wykrywanie i zgłaszanie błędów
Obsługa błędów taki sposób, aby nie przerywać kompilacji po pierwszym błędzie. Błędy wykrywane są w fazie analizy.

### 4.6. Generowanie kodu pośredniego
Reprezentacja programu dla pewnej abstrakcyjnej maszyny (łatwa do utworzenia i tłumaczenia na program wynikowy).

### 4.7. Optymalizacja kodu
Poprawienie kodu pośredniego w taki sposób, aby kod maszynowy działał szybciej.

### 4.8. Generowanie kodu wynikowego
~ najczęściej w Assemblerze.

---

## 5. Grupowanie faz

### 5.1. Przód kompilatora
Fazy zależne przede wszystkim od języka źródłowego i praktycznie niezależne od języka wynikowego. Zwykle składa się z analizatora leksykalnego, składniowego i semantycznego oraz tablicy symboli, generatora kodu pośredniego i obsługi błędów.

### 5.2. Tył kompilatora
Fazy zależne od maszyny docelowej a niezależne od języka źródłowego. Zwykle składa się z optymalizacji i generowania kodu z tablicą symboli i obsługą błędów.

---
