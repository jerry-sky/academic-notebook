# The Basics

[book]: http://ce.sharif.edu/courses/94-95/1/ce414-2/resources/root/Text%20Books/Automata/John%20E.%20Hopcroft,%20Rajeev%20Motwani,%20Jeffrey%20D.%20Ullman-Introduction%20to%20Automata%20Theory,%20Languages,%20and%20Computations-Prentice%20Hall%20(2006).pdf

*Based on the book “Introduction to Automata Theory, Languages, and Computation”.*

- [1. Alphabets](#1-alphabets)
    - [1.1. Examples](#11-examples)
- [2. Words (Strings)](#2-words-strings)
    - [2.1. Examples](#21-examples)
    - [2.2. Length of a word](#22-length-of-a-word)
    - [2.3. Powers of an Alphabet](#23-powers-of-an-alphabet)
        - [2.3.1. Notation of set of words of all lengths](#231-notation-of-set-of-words-of-all-lengths)
    - [2.4. Concatenation](#24-concatenation)
- [3. Languages](#3-languages)
    - [3.1. Examples](#31-examples)
- [4. Problems](#4-problems)
    - [4.1. Example](#41-example)

---

## 1. Alphabets

An *alphabet* is a finite, non-empty set of symbols.

### 1.1. Examples
- $\Sigma = \{0,1\}$
- $\Sigma = \{a,b,\dots,z\}$
- $\Sigma =$ `[insert a set of all ASCII characters]`

---

## 2. Words (Strings)

A *word (string)* is a finite sequence of symbols chosen from a given alphabet.

### 2.1. Examples
- $11011$ is a word chosen from the binary alphabet $\Sigma = \{0,1\}$
- $\epsilon$ is an empty word of [length](#22-length-of-a-word) equal to zero (this word exists in all alphabets)

### 2.2. Length of a word
— the number of **positions** for symbols in a given word

Distinction between the expressions *‘the number of symbols’* and *‘the number of positions’*:\
the word $11011$ has **2** symbols, but **5** positions, meaning the word is of length **5**.

### 2.3. Powers of an Alphabet

We can define sets of all words of a given length.

Notation: $\Sigma^k$ — all words of length $k$ with symbols chosen from $\Sigma$.

The slight confusion about $\Sigma$ and $\Sigma^1$: the difference is in *the semantics* — the former is an **Alphabet** whilst the latter is **the set of all words of length equal to one**.\
However, usually the $\Sigma$ notation is used and the context tells whether it’s one or the other.

#### 2.3.1. Notation of set of words of all lengths

- $\Sigma^+ = \Sigma^1 \cup \Sigma^2 \cup \Sigma^3 \cup \dotsb$
- $\Sigma^* = \Sigma^+ \cup \{\epsilon\}$

### 2.4. Concatenation

Let $x$ and $y$ be words of length $n$ and $m$ respectively and be defined as following:
- $x = x_1x_2 \dots x_n$
- $y = y_1y_2 \dots y_m$

then
$$
xy = x_1x_2 \dots x_n y_1y_2 \dots y_m
$$

Also, for any word $w$:
$$
\epsilon w = w \epsilon = w
$$

---

## 3. Languages

Given an alphabet $\Sigma$ a set $L \subseteq \Sigma^*$ is a *language over $\Sigma$*.

*A set of some selected words from all possible words over a given Alphabet.*

### 3.1. Examples
- $L = \{\epsilon, 01, 0011, 000111, \dots\}$
- $L = \{10, 11, 101, 111, 1011, \dots \}$
- $L = \Sigma^*$ is a language for any alphabet $\Sigma$
- $L = \emptyset$ is a language over any alphabet
- $\{\epsilon\}$ is a language over any alphabet

> The only important constraint on what can be a language is that all alphabets are finite. Thus languages, although they can have an infinite number of strings, are restricted to consist of strings drawn from one fixed, finite alphabet.

---

## 4. Problems

In automata theory a *problem* is the question of deciding whether a given string is a member of some particular language. More precisely, if $\Sigma$ is an alphabet, and $L$ is a language over $\Sigma$, them the problem $L$ is:\
*Given a string $w$ in $\Sigma^*$, decide whether or not $w$ is in $L$.*

### 4.1. Example

*Is a given number $x$ prime?* can be expressed as a *problem*:

*Is `bin(`$x$`)` in the language $L_p$ which consists of all prime numbers in their binary string form.*
