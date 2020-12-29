Select
  owner
From
  pet
Where
  owner not In(
    Select
      owner
    From
      pet
      Join `event` On pet.name = `event`.name
    Where
      `type` = 'birthday'
  )
Group by
  owner;