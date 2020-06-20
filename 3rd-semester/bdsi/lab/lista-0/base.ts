import axios from 'axios';

export interface Pet {
    name: string,
    owner: string,
    species: string,
    sex: 'f' | 'm',
    birth: Date,
    death: Date,
    date: Date,
    type: string,
    remark: string,
}

export const data = axios.get('https://cs.pwr.edu.pl/syga/arch/w2019/db/menagerie.json')
    .then(response => {

        const data = response.data;

        const dataProcessed: {
            table: string,
            rows: Pet[]
        } = { table: data.table, rows: [] };

        for (const row of data.rows) {
            const t: Pet = { ...row };

            for (const d of ['birth', 'death', 'date']) {
                if (t[d]) { t[d] = new Date(row[d]); }
                else { t[d] = null; }
            }

            dataProcessed.rows.push(t);
        }

        return dataProcessed;

    });
