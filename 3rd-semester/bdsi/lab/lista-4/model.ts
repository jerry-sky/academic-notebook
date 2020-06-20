
export interface Osoba {
  imię: string,
  nazwisko: string,
  wiek: number,
  wzrost: number,
  zainteresowania: string[],
  narodowość: Narodowość[],
  pupile: Pupil[]
}

export type Narodowość = string | { kraj: string, krajZwiązkowy: string };

export interface Pupil {
  gatunek: string,
  imię: string
}

export interface Zwierzę {
  nazwa: string,
  rasy: string[],
  minWaga: number,
  maxWaga: number,
  ubarwienie: string,
  przewidywanaDługośćŻycia: number,
}

export interface Sport {
  nazwa: string,
  typ: ('indywidualny' | 'zespołowy')[],
  miejsceWykonywania: ('hala' | 'na zewnątrz')[],
}