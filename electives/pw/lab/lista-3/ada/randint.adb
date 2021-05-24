with Ada.Numerics.Discrete_Random;

package body RandInt is

   gen: RA.Generator;

   function Next(n: in Natural) return Natural is
   begin
      return RA.Random(gen) mod n+1;
   end Next;

begin
   RA.Reset(gen);
end RandInt;
