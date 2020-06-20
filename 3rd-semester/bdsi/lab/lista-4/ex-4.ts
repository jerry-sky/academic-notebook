import { HobbyDatabase, getRandomString, getRandomFromList } from './base';
import { Db } from 'mongodb';
import { Osoba, Narodowość, Pupil } from './model';

HobbyDatabase((database: Db) => {

  const osoby: Osoba[] = [];
  const kraje: Narodowość[] = [
    'Polska',
    'Czechy',
    'Chorwacja',
    'Francja',
    'Wielka Brytania',
    {
      kraj: 'USA',
      krajZwiązkowy: 'Kentucky'
    },
    {
      kraj: 'USA',
      krajZwiązkowy: 'New York'
    },
    {
      kraj: 'USA',
      krajZwiązkowy: 'Pennsylvania'
    },
    {
      kraj: 'Niemcy',
      krajZwiązkowy: 'Bayern'
    },
    {
      kraj: 'Niemcy',
      krajZwiązkowy: 'Brandenburg'
    },
    {
      kraj: 'Niemcy',
      krajZwiązkowy: 'Hamburg'
    },
    {
      kraj: 'Rosja',
      // spellchecker: disable-next-line
      krajZwiązkowy: 'Stavropol Krai'
    },
    {
      kraj: 'Rosja',
      // spellchecker: disable-next-line
      krajZwiązkowy: 'Vladimir Oblast'
    },
    {
      kraj: 'Rosja',
      // spellchecker: disable-next-line
      krajZwiązkowy: 'Novosibirsk Oblast'
    }
  ];
  const sporty: string[] = [];
  const zwierzęta: string[] = [];

  return new Promise(resolve => {

    resolve(
      database
        .collection('sport')
        .find({}, { projection: { nazwa: 1, _id: 0 } })
        .toArray()
        .then((sportyWrapped: { nazwa: string }[]) => {
          sportyWrapped.forEach(sport => {
            sporty.push(sport.nazwa);
          });
        })
    );

  })
    .then(() => {

      return database
        .collection('zwierzęta')
        .find({}, { projection: { nazwa: 1, _id: 0 } })
        .toArray()
        .then((zwierzętaWrapped: { nazwa: string }[]) => {
          zwierzętaWrapped.forEach(zwierzę => {
            zwierzęta.push(zwierzę.nazwa);
          })
        })

    })
    .then(() => {

      for (let i = 0; i < 50; i++) {

        const zainteresowania: string[] = getRandomFromList(sporty, 4, 2);
        const narodowość: Narodowość[] = getRandomFromList(kraje, 3);

        const pupile: Pupil[] = [];
        for (let j = 0; j < Math.round(1 + Math.random() * 3); j++) {
          pupile.push({
            gatunek: zwierzęta[Math.round(Math.random() * (zwierzęta.length - 1))],
            imię: getRandomString(5)
          });
        }

        osoby.push({
          imię: getRandomString(6),
          nazwisko: getRandomString(9),
          wiek: Math.round(18 + Math.random() * 67),
          wzrost: Math.round(160 + Math.random() * 45),
          zainteresowania,
          narodowość,
          pupile,
        });

      }
      const pupile: Pupil[] = [];
      for (let j = 0; j < Math.round(1 + Math.random() * 3); j++) {
        pupile.push({
          gatunek: zwierzęta[Math.round(Math.random() * (zwierzęta.length - 1))],
          imię: getRandomString(5)
        });
      }
      osoby.push(
        {
          imię: 'Jan',
          nazwisko: 'Nowak',
          wiek: 25,
          wzrost: 190,
          zainteresowania: getRandomFromList(sporty, 4, 2),
          narodowość: getRandomFromList(kraje, 3),
          pupile,
        }
      );

    })
    .then(() => {
      // console.log(JSON.stringify(osoby));
      database.collection('osoby').insertMany(osoby);

    });

});