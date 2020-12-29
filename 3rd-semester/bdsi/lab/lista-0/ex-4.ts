import { data } from './base';

data
    .then(data => {

        const ownersPets: { [s: string]: number } = {};

        for (const row of data.rows) {

            if (ownersPets[row.owner]) {
                ownersPets[row.owner]++;
            } else {
                ownersPets[row.owner] = 1;
            }

        }

        for (const o of Object.keys(ownersPets)) {

            if (ownersPets[o] > 1) {
                console.log(o);
            }
        }

    });
