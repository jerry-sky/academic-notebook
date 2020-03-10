#!/usr/bin/env ts-node

import * as fs from 'fs';

export class CharacterCount {
  [x: string]: number
}

export class PairOfCharactersCount {
  [x: string]: CharacterCount
}

/**
 * An analysis of a file's characters.
 */
export class FileAnalysis {

  /**
   * Count of all characters.
   */
  private countOne: CharacterCount = {};
  /**
   * Count of all characters adjacent to another character.
   */
  private countTwo: PairOfCharactersCount = {};

  private Omega: number = 0;

  constructor() {
  }

  public async init(filePath: string) {
    // read the file
    const fd: number = await (new Promise(resolve => {
      fs.open(filePath, 'r', (err, fd) => resolve(fd));
    }) as Promise<number>);

    let buffer = Buffer.from('0');
    let num = 1;

    let current = 0;
    let previous = 0;

    while (num !== 0) {
      num = fs.readSync(fd, buffer, 0, 1, null);
      // handle single character
      previous = current;
      current = buffer[0];
      // console.log(current);
      if (!this.countOne[current]) { this.countOne[current] = 1; }
      else { this.countOne[current]++; }

      // handle a character after another
      // const previous = i == 0 ? String.fromCharCode(0) : this.file[i - 1];

      if (!this.countTwo[previous]) { this.countTwo[previous] = {} }

      if (!this.countTwo[previous][current]) { this.countTwo[previous][current] = 1; }
      else { this.countTwo[previous][current]++; }

      // console.log(current, this.countOne[current]);

      this.Omega++;
    }
  }

  public get getCountOne(): CharacterCount {
    return this.countOne;
  }

  public get getCountTwo(): PairOfCharactersCount {
    return this.countTwo;
  }


  /**
   * Calculate conditional probability of a pair of two characters.
   */
  private ConditionalProbability(x: string, y: string): number {
    return this.countTwo[x][y] / this.countOne[x];
  }

  /**
   * The information function that takes a pair of characters.
   */
  public ConditionalInformation(x: string, y: string): number {
    return -1 * Math.log2(this.ConditionalProbability(x, y));
  }

  public Information(x: string) {
    return -1 * Math.log2(this.Probability(x));
  }

  private CondEntrPart(Y: string[], x: string): number {
    let output = 0;
    Y.forEach(y =>
      output +=
      // this.ConditionalProbability(x, y)
      (this.countTwo[x][y] / this.Omega)
      * this.ConditionalInformation(x, y)
    );

    return output;
  }

  private Probability(x: string): number {
    return this.countOne[x] / this.Omega;
  }

  public ConditionalEntropy(): number {
    let output = 0;

    Object.keys(this.countOne).forEach(x =>
      output +=
      // this.Probability(x)
      // *
      this.CondEntrPart(
        Object.keys(this.countTwo[x]),
        x
      )
    )

    return output;
  }

  public Entropy(): number {
    let count = 0;
    let output = 0;
    Object.keys(this.countOne).forEach(x => {
      output += this.countOne[x] * (-1) * Math.log2(this.countOne[x])
      count++;
    });
    output = output / this.Omega;

    return output + Math.log(this.Omega) / Math.log(2);
  }

}


const printResults = (fa: FileAnalysis, precision = 8) => {
  const e = fa.Entropy();
  const ce = fa.ConditionalEntropy();
  console.log(
    '  entropy:            ',
    e.toFixed(precision)
  );
  console.log(
    '  conditional entropy:',
    ce.toFixed(precision)
  );
  console.log(
    '  difference:         ',
    (e - ce).toFixed(precision)
  );
  console.log('---');
}


const files = ['pan-tadeusz.txt', 'test1.bin', 'test2.bin', 'test3.bin'];
// const files = ['test3.bin'];
// const files = ['pan-tadeusz.txt'];
files.forEach(async file => {
  const fa = new FileAnalysis();
  await fa.init(file);
  console.log(file + ':');
  printResults(fa);
});

