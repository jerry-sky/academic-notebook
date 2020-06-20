Update
  `event`,
  pet
Set
  `event`.performer = pet.owner
Where
  pet.name = `event`.name
  And `event`.type Not In ('vet', 'litter');
--
Update
  `event`
Set
  `event`.performer = 'Soros'
Where
  `event`.type = 'vet';
--
Update
  `event`
Set
  `event`.performer = 'Trump'
Where
  `event`.type = 'litter';