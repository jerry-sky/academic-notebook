LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
USE ieee.numeric_std.ALL;

USE std.textio.ALL;

ENTITY lfsr_tb IS
    generic (quantity : natural := 1);
END lfsr_tb;

ARCHITECTURE behavior OF lfsr_tb IS

    -- UUT (Unit Under Test)
    COMPONENT lfsr
    PORT(
        clk : IN  std_logic;
        q : INOUT  STD_LOGIC_VECTOR (15 downto 0)
    );
    END COMPONENT;

    -- input signals
    signal clk : std_logic := '0';

    -- input/output signal
    signal qq : STD_LOGIC_VECTOR (15 downto 0);

    signal stopp : std_logic := '0';

    -- set clock period
    constant clk_period : time := 10 ns;

BEGIN
	-- instantiate UUT
    uut: lfsr PORT MAP (
        clk => clk,
        q   => qq
    );

   -- clock management process
   -- no sensitivity list, but uses 'wait'
    clk_process: PROCESS
        VARIABLE l : line;
    BEGIN

        write(l, "" & std_logic'image(qq(0))(2));
        writeline(output, l);

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
        wait for clk_period * 8 * quantity - clk_period/2;

        -- stop
        stopp <= '1';
        wait;
    END PROCESS;
END;
