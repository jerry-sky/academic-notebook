import { data, Pet } from './base';
import { writeFileSync } from 'fs';

data
    .then(data => {

        const toAdd: Pet[] = [
            {
                name: 'Henry',
                owner: 'Otto',
                sex: 'm',
                species: 'dog',
                birth: new Date('2019-4-2'),
                death: null,
                date: new Date('2019-5-9'),
                type: 'birthday',
                remark: null,
            },
            {
                name: 'Stefan',
                owner: 'Alex',
                sex: 'f',
                species: 'dog',
                birth: new Date('2012-9-1'),
                death: null,
                date: new Date('2013-9-2'),
                type: 'litter',
                remark: '1 puppy, 1 female'
            },
            {
                name: 'Lukas',
                owner: 'Lukas',
                sex: 'm',
                species: 'hamster',
                birth: new Date('2005-4-5'),
                death: null,
                date: new Date('2011-12-23'),
                type: 'birthday',
                remark: null,
            },
            {
                name: 'Go-tee',
                owner: 'Lukas',
                sex: 'f',
                species: 'goat',
                birth: new Date('2006-2-2'),
                death: null,
                date: new Date('2011-12-23'),
                type: 'birthday',
                remark: null,
            },
            {
                name: 'Alex',
                owner: 'Lukas',
                sex: 'm',
                species: 'goat',
                birth: new Date('2001-7-25'),
                death: null,
                date: new Date('2011-12-22'),
                type: 'birthday',
                remark: null,
            },
            {
                name: 'Greatest',
                owner: 'Lukas',
                sex: 'f',
                species: 'goat',
                birth: new Date('1985-5-22'),
                death: null,
                date: new Date('2011-12-24'),
                type: 'birthday',
                remark: null,
            },
            {
                name: 'Heap',
                owner: 'Lukas',
                sex: 'm',
                species: 'sheep',
                birth: new Date('2004-2-1'),
                death: null,
                date: new Date('2011-12-22'),
                type: 'birthday',
                remark: null,
            }
        ];

        const output = data.rows.concat(toAdd);

        const outputRaw = [];

        for (const row of output) {
            const t: any = { ...row };
            for (const p of ['birth', 'death', 'date']) {
                if (t[p]) { t[p] = t[p].toISOString().substr(0, 10); }
                else { t[p] = null; }
            }
            outputRaw.push(t);
        }

        writeFileSync('output.json', JSON.stringify(outputRaw, null, 4));

    });
