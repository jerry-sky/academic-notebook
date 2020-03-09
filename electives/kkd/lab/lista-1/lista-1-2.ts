#!/usr/bin/env ts-node

import * as fs from 'fs';
import * as  math from 'mathjs';

export class CharacterCount {
  [x: string]: math.BigNumber
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

  private Omega = math.bignumber(0);

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
      if (!this.countOne[current]) { this.countOne[current] = math.bignumber(1); }
      else {
        this.countOne[current] = this.countOne[current].add(1);
      }

      // handle a character after another
      // const previous = i == 0 ? String.fromCharCode(0) : this.file[i - 1];

      if (!this.countTwo[previous]) { this.countTwo[previous] = {} }

      if (!this.countTwo[previous][current]) { this.countTwo[previous][current] = math.bignumber(1); }
      else {
        this.countTwo[previous][current] = this.countTwo[previous][current].add(1);
      }

      // console.log(current, this.countOne[current]);

      this.Omega = this.Omega.add(1);
    }

    console.log(this.Omega.toString());
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
  public ConditionalProbability(x: string, y: string): math.BigNumber {
    return math.divide(this.countTwo[x][y], this.countOne[x]) as math.BigNumber;
  }

  /**
   * The information function that takes a pair of characters.
   */
  public ConditionalInformation(x: string, y: string): math.BigNumber {
    return math.multiply(
      -1,
      math.log2(this.ConditionalProbability(x, y))
    ) as math.BigNumber;
    // return -1 * Math.log2(this.ConditionalProbability(x, y));
  }

  public Information(x: string) {
    return math.multiply(
      -1,
      math.log2(this.Probability(x))
    );
    // return -1 * Math.log2(this.Probability(x));
  }

  private CondEntrPart(Y: string[], x: string): math.BigNumber {
    let output = math.bignumber(0);
    Y.forEach(y => {
      const tmp =
        math.multiply(
          this.countTwo[x][y],
          this.ConditionalInformation(x, y)
        ) as math.BigNumber;
      output = output.add(tmp);
    }
    );

    return math.divide(output, this.Omega) as math.BigNumber;
  }

  private Probability(x: string): math.BigNumber {
    return math.divide(this.countOne[x], this.Omega) as math.BigNumber;
  }

  public ConditionalEntropy(): math.BigNumber {
    let output = math.bignumber(0);

    Object.keys(this.countOne).forEach(x =>
      output = output.add(
        // this.Probability(x)
        // *
        this.CondEntrPart(
          Object.keys(this.countTwo[x]),
          x
        )
      )
    )

    return output;
  }

  public Entropy(): math.BigNumber {
    let output = math.bignumber(0);
    Object.keys(this.countOne).forEach(x => {
      const tmp = math.multiply(
        this.countOne[x],
        math.multiply(
          -1,
          math.log2(this.countOne[x])
        )
      ) as math.BigNumber;
      // output += this.countOne[x] * (-1) * Math.log2(this.countOne[x])
      output = output.add(tmp);
    });
    output = math.divide(output, this.Omega) as math.BigNumber;

    // return output + Math.log(this.Omega) / Math.log(2);
    return math.add(output, math.log2(this.Omega)) as math.BigNumber;
  }

}


const printResults = (fa: FileAnalysis) => {
  const e = fa.Entropy();
  const ce = fa.ConditionalEntropy();
  console.log('  entropy:            ', e.toString());
  console.log('  conditional entropy:', ce.toString());
  console.log('  difference:         ', math.subtract(e, ce).toString());
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

