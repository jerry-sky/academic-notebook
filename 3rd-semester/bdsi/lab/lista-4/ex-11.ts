import { HobbyDatabase } from "./base";
import { Db } from "mongodb";

HobbyDatabase((database: Db) => {

  return database.collection('osoby')
    .updateMany(
      {
        zainteresowania: {
          '$all': ['strzelectwo', 'narciarstwo']
        }
      },
      {
        '$push': {
          'zainteresowania': 'biatlon'
        }
      }
    )
    .then((results) => {
      console.log(results);

      return database.collection('osoby').updateMany(
        {
          zainteresowania: {
            '$all': ['strzelectwo', 'narciarstwo']
          }
        },
        {
          '$pull': {
            zainteresowania: { '$in': ['strzelectwo', 'narciarstwo'] }
          }
        }
      )
    })
    .then((results) => {
      console.log(results);
      return database.collection('osoby')
        .find()
        .toArray();
    })
    .then((results) => {
      results.forEach(value => {
        console.log(value);
      })
    })

})