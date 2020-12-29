import { MongoClient, Db } from 'mongodb';

/**
 * The connection string needed to connect to the MDBHobby database.
 */
// spellchecker: disable-next-line
const connectionString = "mongodb://vscode:verysecretivepassword@localhost:27017/MDBHobby";

/**
 * MongoDB connection to the Hobby database
 */
const Connection = MongoClient.connect(connectionString, { useUnifiedTopology: true })
  .catch((error: Error) => {
    console.error('error occurred while trying to connect to the database', error);
  })

/**
 * The connection method for the exercises to connect to the database
 * @param toExecute
 */
export const HobbyDatabase = (toExecute: (client: Db) => Promise<any>) => {

  return Connection.then((client: MongoClient) => {

    const database = client.db("MDBHobby");

    return toExecute(database)
      .catch((error) => {

        console.error(error);
      })
      .finally(() => {
        client.close();
      });

  })

}

export const getRandomString = (length: number) => {

  // spellchecker: disable-next-line
  const spectrum = 'qwertyuiopasdfghjklzxcvbnm';

  let result = '';

  for (let i = 0; i < length; i++) {
    result += spectrum.substr(Math.random() * (spectrum.length - 1), 1);
  }

  return result;
}

export const getRandomFromList = (list: any[], maxLength = 1, minLength = 1) => {
  let listLeft = [...list];
  const result = [];
  for (let i = 0; i < (minLength + Math.round((Math.random() * (maxLength - minLength)))) && listLeft.length > 0; i++) {
    let index = Math.round(Math.random() * (listLeft.length - 1));
    if (index < 0) index = 0;
    result.push(listLeft[index]);
    listLeft.splice(index, 1);
  }
  return result;
}
