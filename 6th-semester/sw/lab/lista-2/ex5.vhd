library IEEE;
use IEEE.STD_LOGIC_1164.ALL;


entity ex5 is
port (
  a, b, c: in std_logic;
  x: out std_logic
);
end ex5;


architecture behaviour of ex5 is

    component gateNOT
    port (
        X: in std_logic;
        Z: out std_logic
    );
    end component;

    component gateAND
    port (
        X, Y: in std_logic;
        Z: out std_logic
    );
    end component;

    signal
        b_AND_c,
        NOT_b_AND_c,
        NOT_a,
        last_AND: std_logic;

begin

    G1: gateNOT port map (a, NOT_a);
    G2: gateAND port map (b, c, b_AND_c);
    G3: gateNOT port map (b_AND_c, NOT_b_AND_c);
    G4: gateAND port map (NOT_a, NOT_b_AND_c, last_AND);
    G5: gateNOT port map (last_AND, x);

end behaviour;


