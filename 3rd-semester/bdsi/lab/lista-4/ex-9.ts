import { HobbyDatabase } from "./base";
import { Db } from "mongodb";

HobbyDatabase((database: Db) => {

  return database
    .collection('osoby')
    .aggregate([
      {
        '$match': {
          nazwisko: 'Nowak'
        }
      },
      { '$unwind': '$zainteresowania' },
      {
        '$lookup': {
          from: 'sport',
          localField: 'zainteresowania',
          foreignField: 'nazwa',
          as: 'sport'
        }
      },
      // { '$unwind': '$sport' },
      {
        '$project': {
          '_id': 0,
          imię: 1,
          nazwisko: 1,
          narodowość: 1,
          nazwaSportu: '$zainteresowania',
          typSportu: '$sport.typ'
        }
      },
      { '$unwind': '$typSportu' },
    ])
    .toArray()
    .then((results) => {
      results.forEach(value => {
        console.log(value);
      })
    })

});