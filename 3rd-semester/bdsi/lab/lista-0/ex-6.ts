import { data } from './base';

data
    .then(data => {

        for (const row of data.rows) {

            if (row.remark && row.remark.indexOf('kitten') !== -1) {
                console.log(row.owner);
            }

        }

    });
