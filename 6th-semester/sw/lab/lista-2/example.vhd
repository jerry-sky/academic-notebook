library IEEE;
use IEEE.STD_LOGIC_1164.ALL;


entity example is
port (
  a,b,c : in std_logic;
  x     : out std_logic
);
end example;

architecture Synthetic of example is
 component gateNOT
   port (X: in std_logic;
	      Z: out std_logic);
 end component;
 component gateOR
   port (X,Y: in std_logic;
	        Z: out std_logic);
 end component;

 signal NOT_OR,
        OR_OR,
		  OR_NOT : std_logic;
begin
 G1: gateNOT port map (a,NOT_OR);
 G2: gateOR  port map (b,c,OR_OR);
-- alternatywne sposoby opisu mapowania portow
 --G3: gateOR  port map (NOT_OR,OR_OR,OR_NOT);
 G3: gateOR port map (X => NOT_OR, Y => OR_OR, Z => OR_NOT);
 G4: gateNOT port map (OR_NOT, x);
end Synthetic;


