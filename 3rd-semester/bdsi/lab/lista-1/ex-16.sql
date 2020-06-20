Select
  a.owner as a_owner,
  b.owner as b_owner
From
  pet a
  Join pet b on (a.species = b.species And a.owner > b.owner)