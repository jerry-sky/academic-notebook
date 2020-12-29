import { HobbyDatabase } from "./base";
import { Db } from "mongodb";

HobbyDatabase((database: Db) => {

  return database
    .collection('osoby')
    .updateMany(
      {
        narodowość: {
          '$elemMatch': {
            kraj: 'Rosja'
          }
        }
      },
      {
        '$set': { 'narodowość.$': 'Rosja' }
      }
    )
    // .toArray()
    .then((results) => {
      console.log(JSON.stringify(results, null, 2));
      // results.forEach(value => {
      //   console.log(value);
      // });
      return database.collection('osoby');
    })
    .then((collection) => {
      return collection.find({
        narodowość: {
          '$all': ['Rosja']
        }
      }).toArray();
    })
    .then((results) => {
      results.forEach(value => {
        console.log(value);
      });
    })

});