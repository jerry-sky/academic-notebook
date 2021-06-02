library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity Clock_Divider is
    generic (
        steps: Real := 1.0
    );
    port (
        clk: in std_logic;
        stopp: in std_logic;
        clk_out: out std_logic := '0'
    );
end Clock_Divider;

architecture Behaviour of Clock_Divider is
begin

    process
        variable counter: Natural := 0;
    begin
        if stopp = '1' then
            wait;
        end if;

        wait until clk'event;
        if Real(counter) >= steps then
            counter := 0;
            wait until clk = '1';
            clk_out <= '1';
        else
            clk_out <= '0';
        end if;
        if clk = '1' then
            counter := counter + 1;
        end if;
    end process;

end Behaviour;

