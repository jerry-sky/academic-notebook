import { data } from './base';

data
    .then(data => {

        data.rows.sort((a, b) => a.name < b.name ? -1 : a.name > b.name ? 1 : 0);

        for (const row of data.rows) {

            console.log(row.owner, '-', row.name);

        }

    });
