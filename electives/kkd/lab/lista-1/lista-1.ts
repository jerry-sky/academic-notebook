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

  private file: string;

  /**
   * Count of all characters.
   */
  private countOne: CharacterCount = {};
  /**
   * Count of all characters adjacent to another character.
   */
  private countTwo: PairOfCharactersCount = {};

  private Omega: number = 0;

  constructor(filePath: string) {
    // read the file
    this.file = fs.readFileSync(filePath, { encoding: 'ascii' });

    for (let i = 0; i < this.file.length; i++) {
      // handle single character
      const current = this.file[i];
      if (!this.countOne[current]) { this.countOne[current] = 1; }
      else { this.countOne[current]++; }

      // handle a character after another
      const previous = i == 0 ? String.fromCharCode(0) : this.file[i - 1];

      if (!this.countTwo[previous]) { this.countTwo[previous] = {} }

      if (!this.countTwo[previous][current]) { this.countTwo[previous][current] = 1; }
      else { this.countTwo[previous][current]++; }

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
    let output = 0;
    Object.keys(this.countOne).forEach(x => {
      output += this.countOne[x] * this.Information(x)
    });
    return output / this.Omega;
  }

}


const printResults = (fa: FileAnalysis) => {
  const e = fa.Entropy();
  const ce = fa.ConditionalEntropy();
  console.log('entropy:            ', e);
  console.log('conditional entropy:', ce);
  console.log('difference:         ', e - ce);
}


const files = ['pan-tadeusz.txt', 'test1.bin', 'test2.bin', 'test3.bin'];
files.forEach(file => {
  const fa = new FileAnalysis(file);
  console.log(file + ':');
  printResults(fa);
});

