import { HobbyDatabase } from "./base";
import { Db } from "mongodb";

HobbyDatabase((database: Db) => {

  return database.collection('osoby')
    .find({
      pupile: {
        '$elemMatch': {
          // gatunek: 'kot',
          gatunek: 'pies'
        }
      }
    },
      {
        projection: {
          imię: 1,
          nazwisko: 1,
          narodowość: 1,
          // wiek: 1,
          // pupile: 1,
        }
      })
    .sort({ wiek: 1 })
    .toArray()
    .then((results) => {
      results.forEach(value => {
        console.log(value);
      })
    })

})