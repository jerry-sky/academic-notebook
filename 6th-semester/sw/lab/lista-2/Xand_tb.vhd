LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
use ieee.numeric_std.all;

ENTITY Xand_tb IS
END Xand_tb;

ARCHITECTURE behavior OF Xand_tb IS

component Xand is
    generic (width : integer);
    port ( clk : in std_logic;
    A,B : in std_logic_vector(width-1 downto 0);
    C : out std_logic_vector(width-1 downto 0)
    );
    end component;

    constant width : integer := 12;

    signal A : std_logic_vector(width-1 downto 0):= (others => '0');
    signal B : std_logic_vector(width-1 downto 0):= (others => '0');
    signal C : std_logic_vector(width-1 downto 0):= (others => '0');

    signal clk : std_logic := '0';

    signal RESET : std_logic_vector(width-1 downto 0) := (others => '0');

BEGIN

    UUT : Xand generic map (width => width) port map (clk => clk, A => A, B => B, C => C);

    stim_proc: PROCESS
    BEGIN

    wait for 100 ns;

    A <= std_logic_vector(unsigned(A) + 20);
    B <= std_logic_vector(unsigned(B) + 24);

    wait for 10 ns;
    A <= RESET;
    B <= RESET;
    wait for 10 ns;

    A <= std_logic_vector(unsigned(A) + 1093);
    B <= std_logic_vector(unsigned(B) + 1295);

    wait for 10 ns;
    A <= RESET;
    B <= RESET;
    wait for 10 ns;

    A <= std_logic_vector(unsigned(A) + 3855);
    B <= std_logic_vector(unsigned(B) + 4095);

    wait for 10 ns;
    A <= RESET;
    B <= RESET;
    wait for 10 ns;


    wait for 100 ns;

    wait;
    END PROCESS;

END;
