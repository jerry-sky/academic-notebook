import { data } from './base';

data
    .then(data => {

        for (const row of data.rows) {

            console.log(row.owner, '-', row.name);

        }

    });
