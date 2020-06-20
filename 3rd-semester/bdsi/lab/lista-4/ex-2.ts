import { HobbyDatabase, getRandomString, getRandomFromList } from './base';
import { Db } from 'mongodb';
import { Sport } from './model';

HobbyDatabase((database: Db) => {

  const sporty: Sport[] = [];

  const sportTypy: Sport["typ"] = ['indywidualny', 'zespołowy'];
  const sportMiejsceWykonywania: Sport["miejsceWykonywania"] = ['hala', 'na zewnątrz'];

  return new Promise(resolve => {

    for (let i = 0; i < 10; i++) {
      sporty.push({
        nazwa: getRandomString(7),
        typ: getRandomFromList(sportTypy, 2),
        miejsceWykonywania: getRandomFromList(sportMiejsceWykonywania, 2),
      });
    }

    sporty.push(
      {
        nazwa: 'koszykówka',
        typ: ['zespołowy'],
        miejsceWykonywania: ['hala', 'na zewnątrz'],
      },
      {
        nazwa: 'hokej',
        typ: ['zespołowy'],
        miejsceWykonywania: ['hala']
      },
      {
        nazwa: 'strzelectwo',
        typ: ['indywidualny'],
        miejsceWykonywania: ['na zewnątrz', 'hala']
      },
      {
        nazwa: 'narciarstwo',
        typ: ['indywidualny'],
        miejsceWykonywania: ['na zewnątrz']
      },
      {
        nazwa: 'biatlon',
        typ: ['zespołowy'],
        miejsceWykonywania: ['hala', 'na zewnątrz']
      }
    );

    resolve(sporty);

  })
    .then((sporty: Sport[]) => {

      database.collection('sport').insertMany(sporty);

    });

});