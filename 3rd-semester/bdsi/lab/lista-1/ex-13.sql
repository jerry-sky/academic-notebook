Select
  *
From
  pet
Where
  birth = (
    Select
      Max(`birth`)
    From
      pet
    Where
      death is null
  );