---
lang: 'pl'
title: 'Lista-1'
author: 'Jerry Sky'
date: '2020-10-25'
---

---

- [Treść zadania](#treść-zadania)
- [Uruchomienie programów](#uruchomienie-programów)

---

## Treść zadania

> Przeanalizuj i zaimplementuj algorytmy wyszukiwania wzorca z wykorzystaniem automatów skończonych i Knutha-Morrisa-Pratta (opisane w książce: Cormen T.H., Leiserson Ch.E., Rivest R.L.: Wprowadzenie do algorytmów, rozdział 34.3 i 34.4).
>
> Programy powinny być oddane z plikiem README opisującym dostarczone pliki i zawierającym dane autora, oraz z plikiem `makefile`, jeśli wymagana jest jego kompilacja. W przypadku użycia innych języków niż C/C++, Java i Python3, należy także zamieścić dokładne instrukcje, co należy doinstalować dla systemu Ubuntu. Wywołanie programów powinno wyglądać następująco:
> ```
> FA <wzorzec> <nazwa pliku> oraz KMP <wzorzec> <nazwa pliku>
> ```
> czyli dane są podawane jako parametry wywołania programów (szukamy wszystkich wystąpień wzorca w podanym pliku). Przy przesyłaniu do prowadzącego programy powinny być spakowane programem zip, a archiwum nazwane numerem indeksu studenta. Archiwum nie powinno zawierać żadnych zbędnych plików.

---

## Uruchomienie programów

Pliki źródłowe:
- [`FA`](fa.py)
- [`KMP`](kmp.py)

W celu uruchomienia programów należy wykonać te same polecenia, co podane w [treści zadania](#treść-zadania) dodając przedrostek „`./`” na początku polecenia.

W trakcie działania programów wyświetlane są kolejne indeksy reprezentujące początki wystąpień żądanego wzorca. Jako że są one drukowane na `stderr` można ograniczyć output programu dodając ` 2>/dev/null` na końcu polecenia — wówczas jedynym wynikiem, który zostanie wyświetlony, będzie lista wszystkich indeksów po analizie całego pliku.
