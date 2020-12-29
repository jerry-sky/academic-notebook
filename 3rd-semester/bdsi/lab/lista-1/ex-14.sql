Select
  owner
From pet
Join `event` On pet.name = `event`.name
Where `event`.date > (Select date From `event` Where name = 'Slim' And `type` = 'vet')