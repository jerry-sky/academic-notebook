import { HobbyDatabase } from "./base";
import { Db } from "mongodb";

HobbyDatabase((database: Db) => {

  return database.collection('osoby')
    .find({
      // spell-checker: disable-next-line
      imię: { '$regex': /^[^vxqłąz]+$/ },
      // spell-checker: disable-next-line
      nazwisko: { '$regex': /^[^vxqłąz]+$/ },

      narodowość: {
        '$not': { '$all': ['Polska'] }
      }

    })
    .toArray()
    .then((results) => {

      results.forEach(value => {
        console.log(value);
      })

    })

})