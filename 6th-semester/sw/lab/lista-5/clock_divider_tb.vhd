LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
use ieee.numeric_std.all;

ENTITY Clock_Divider_tb IS
END Clock_Divider_tb;

ARCHITECTURE Behaviour OF Clock_Divider_tb IS

    -- base clock period
    constant clk_period_int: Natural := 8; -- 125MHz
    constant clk_period: time := clk_period_int * 1 ns;
    constant frq: Real := 125000000.0;

    component Clock_Divider
        generic (
            steps: Real
        );
        port (
            clk: in std_logic;
            stopp: in std_logic;
            clk_out: out std_logic
        );
    end component;

    component Clock_Exp_Divider
        generic (
            N: Natural
        );
        port (
            clk: in std_logic;
            stopp: in std_logic;
            clk_out: out std_logic_vector
        );
    end component;

    signal clk: std_logic := '0';
    signal clk_out_100Hz: std_logic := '0';
    signal clk_out_1100Hz: std_logic := '0';
    signal clk_out_50MHz: std_logic := '0';
    constant N: Natural := 5;
    signal clk_out_exp: std_logic_vector(N-1 downto 0);

    signal stopp: std_logic := '0';

BEGIN

    uut100Hz: Clock_Divider
    generic map (
        steps => frq / 100.0
    )
    port map (
        clk => clk,
        stopp => stopp,
        clk_out => clk_out_100Hz
    );

    uut1100Hz: Clock_Divider
    generic map (
        steps => frq / 1100.0
    )
    port map (
        clk => clk,
        stopp => stopp,
        clk_out => clk_out_1100Hz
    );

    uut50MHz: Clock_Divider
    generic map (
        steps => frq / 50000000.0
    )
    port map (
        clk => clk,
        stopp => stopp,
        clk_out => clk_out_50MHz
    );


    uutexp: Clock_Exp_Divider
    generic map (
        N => N
    )
    port map (
        clk => clk,
        stopp => stopp,
        clk_out => clk_out_exp
    );

    -- Clock process definitions
    clk_process: process
    begin
        if stopp = '1' then
            wait;
        end if;
        clk <= '1';
        wait for clk_period/2;
        clk <= '0';
        wait for clk_period/2;
    end process;

   -- Stimulus process
   process
   begin
        wait for 10000000 ns;
        stopp <= '1';
        wait;
   end process;

END;
