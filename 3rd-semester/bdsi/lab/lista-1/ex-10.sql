Select 
  owner, name
From
  pet
Where
  species = 'dog' And
  name not in (Select `name` From `event` Where `type` = 'birthday')
Order by name Desc