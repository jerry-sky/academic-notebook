import { HobbyDatabase } from "./base";
import { Db } from "mongodb";

HobbyDatabase((database: Db) => {

  return database
    .collection('osoby')
    .aggregate([
      { '$unwind': '$zainteresowania' },
      {
        '$project': {
          '_id': 0,
          imię: 1,
          zainteresowania: 1,
        }
      },
      {
        '$group': {
          _id: '$zainteresowania',
          count: { '$sum': 1 }
        }
      },
      {
        '$match': {
          count: { '$gte': 5 }
        }
      }
    ])
    .toArray()
    .then((results) => {
      results.forEach(value => {
        console.log(value);
      })
    })

});