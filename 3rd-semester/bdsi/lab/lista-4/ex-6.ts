import { HobbyDatabase } from "./base";
import { Db } from "mongodb";

HobbyDatabase((database: Db) => {

  return database
    .collection('osoby')
    .aggregate([
      { '$unwind': '$pupile' },
      { '$match': { 'pupile.gatunek': 'kot' } },
      {
        '$project': {
          '_id': 0,
          'pupile': 1,
          'imię': 1,
        }
      }
      // { '$project': }
    ])
    // .find(
    //   { 'pupile.gatunek': 'kot' },
    //   {
    //     projection: {
    //       imię: 1,
    //       nazwisko: 1,
    //       'pupile.gatunek': 'kot'
    //     }
    //   })
    .toArray()
    .then((osoby) => {
      osoby.forEach(osoba => {
        console.log(osoba);
      });
    });

});