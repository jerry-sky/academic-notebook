with Ada.Numerics.Discrete_Random;

package RandInt is

    package RA is new Ada.Numerics.Discrete_Random(Natural);

    function Next(n: in Natural) return Natural;

end RandInt ;
