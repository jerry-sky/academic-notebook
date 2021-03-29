

-- bramka AND
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity gateAND is
port (
	X: in std_logic;
	Y: in std_logic;
	Z: out std_logic
);
end gateAND;

architecture Behavioral of gateAND is
begin
 Z <= X and Y after 1 ns;
end Behavioral;



-- bramka OR
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity gateOR is
port (
	X: in std_logic;
	Y: in std_logic;
	Z: out std_logic
);
end gateOR;

architecture Behavioral of gateOR is
begin
 Z <= X or Y after 1 ns;
end Behavioral;




-- bramka XOR
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity gateXOR is
port (
	X: in std_logic;
	Y: in std_logic;
	Z: out std_logic
);
end gateXOR;

architecture Behavioral of gateXOR is
begin
 Z <= X xor Y after 1 ns;
end Behavioral;



-- bramka NOT
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity gateNOT is
port (
   X: in std_logic;
	Z: out std_logic
);
end gateNOT;

architecture Behavioral of gateNOT is
begin
  Z <= not X after 1 ns;
end Behavioral;



-- multiplekser czterowejisciowy
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity mux is
port (
  a,b,c,d : in std_logic;
  s0,s1   : in std_logic;
  x       : out std_logic
);
end mux;

architecture zachowanie of mux is
begin
process (a,b,c,d, s0,s1)
  variable sel: integer;
  begin
    if s0='0' and s1='0' then
	   sel := 0;
	 elsif s0='1' and s1='1' then
	   sel := 1;
	 elsif s0='0' and s1='1' then
	   sel := 2;
	 else
	   sel := 3;
	 end if;
	 case sel is
	   when 0 =>
		    x <= a;
	   when 1 =>
		    x <= b;
	   when 2 =>
		    x <= c;
	   when others =>
		    x <= d;
	 end case;
  end process;
end zachowanie;
