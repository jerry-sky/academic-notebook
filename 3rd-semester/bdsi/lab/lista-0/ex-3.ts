import { data } from './base';

data
    .then(data => {

        for (const row of data.rows) {

            if (row.species === 'dog' && row.birth.getMonth() < 6) {
                console.log(row.name, row.date.toLocaleDateString());
            }

        }

    });
