import { data } from './base';

data
    .then(data => {

        const speciesCounts: { [s: string]: number } = {};

        for (const row of data.rows) {

            if (!speciesCounts[row.species]) {
                speciesCounts[row.species] = 1;
            } else {
                speciesCounts[row.species]++;
            }

        }

        for (const species of Object.keys(speciesCounts)) {

            console.log(species + ':', speciesCounts[species]);

        }

    });
