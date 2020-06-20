import { HobbyDatabase } from "./base";
import { Db } from "mongodb";

HobbyDatabase((database: Db) => {

  return database
    .collection('osoby')
    .find({
      // imię: 'Jan',
      '$or': [
        { narodowość: {'$all': ['Polska']} },
        {
          narodowość: { '$exists': true },
          '$where': 'this.narodowość.length>2'
        }
      ]
    })
    .toArray()
    .then((results) => {
      results.forEach(value => {
        console.log(value);
      })
    })

});