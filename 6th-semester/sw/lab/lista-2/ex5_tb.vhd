library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;


entity ex5_tb is
end ex5_tb;


architecture behavior of ex5_tb is

    component ex5
    port(
        a: in std_logic;
        b: in std_logic;
        c: in std_logic;
        x: out std_logic
    );
    end component;

    -- inputs
    signal a: std_logic := '0';
    signal b: std_logic := '0';
    signal c: std_logic := '0';

    -- outputs
    signal x: std_logic;

    -- loop iteration period
    constant period: time := 10 ns;

begin

	-- instantiate the Unit Under Test (UUT)
    uut: ex5 port map (
        a => a,
        b => b,
        c => c,
        x => x
    );

    -- stimulus process
    stim_proc: process

    type pattern_type is record
        a, b, c: std_logic;
        x: std_logic;
    end record;

    type pattern_array is array (natural range <>) of pattern_type;
    constant patterns : pattern_array := (
        ('0', '0', '0', '0'),
        ('0', '0', '1', '0'),
        ('0', '1', '0', '0'),
        ('0', '1', '1', '1'),
        ('1', '0', '0', '1'),
        ('1', '0', '1', '1'),
        ('1', '1', '0', '1'),
        ('1', '1', '1', '1')
    );

    begin

        wait for 10 * period;

        --  check each pattern
        for i in patterns'range loop

            a <= patterns(i).a;
            b <= patterns(i).b;
            c <= patterns(i).c;

            wait for period;

            --  check the output
            assert x = patterns(i).x
            report "test failed" severity error;

        end loop;

        a <= '0';
        b <= '0';
        c <= '0';

        wait for 10 * period;

        wait;
    end process;

end;
