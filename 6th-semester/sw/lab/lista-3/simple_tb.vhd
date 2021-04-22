LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
USE ieee.numeric_std.ALL;

ENTITY simple_tb IS
END simple_tb;

ARCHITECTURE behavior OF simple_tb IS

    -- UUT (Unit Under Test)
    COMPONENT simple
    PORT(
        clk : IN  std_logic;
        rst : IN  std_logic;
        q : INOUT  unsigned(7 downto 0)
        );
    END COMPONENT;

    -- input signals
    signal clk : std_logic := '0';
    signal rst : std_logic := '0';

    -- input/output signal
    signal qq : unsigned(7 downto 0);

    signal stopp : std_logic := '0';

    -- set clock period
    constant clk_period : time := 20 ns;

BEGIN
	-- instantiate UUT
    uut: simple PORT MAP (
        clk => clk,
        rst => rst,
        q   => qq
    );

   -- clock management process
   -- no sensitivity list, but uses 'wait'
    clk_process: PROCESS
    BEGIN
        clk <= '0';
        WAIT FOR clk_period/2;
        clk <= '1';
        WAIT FOR clk_period/2;

        IF stopp = '1' THEN
            WAIT;
        END IF;

    END PROCESS;


   -- stimulating process
    stim_proc: PROCESS
    BEGIN
        -- let it run
        wait for 50 ns;

        -- apply reset
        rst <= '1';

        wait for 700 ns;
        -- and let it go
        rst <= '0';

        wait for 50 ns;

        -- apply reset
        rst <= '1';

        wait for 440 ns;
        -- and let it go
        rst <= '0';

        -- stop
        stopp <= '1';
        wait;
    END PROCESS;
END;
