Select
  species,
  count(*) as `count`
From
  pet
Group by
  species
Order by
  `count` Desc