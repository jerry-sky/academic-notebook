import { HobbyDatabase } from "./base";
import { Db } from "mongodb";


HobbyDatabase((database: Db) => {

  return database
    .collections()
    .then((collections) => collections
      .forEach(collection => {
        collection.find().toArray().then(list => {
          // if (list.length === 0) return;
          console.log('---', collection.collectionName.toUpperCase(), '---');
          for (let i = 0; i < 5; i++)
            console.log(list[i]);
          if (list.length > 5) console.log('...');
          console.log('\n');
        })
      }));

});