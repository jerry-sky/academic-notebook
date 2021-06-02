library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.math_real.all;

entity Clock_Exp_Divider is
    generic (
        N: Natural := 0
    );
    port (
        clk: in std_logic;
        stopp: in std_logic;
        clk_out: out std_logic_vector(N-1 downto 0) := (others => '0')
    );
end Clock_Exp_Divider;

architecture Behaviour of Clock_Exp_Divider is
begin

    process
        variable counter: Natural := 0;
    begin
        if stopp = '1' then
            wait;
        end if;

        wait until clk = '1';
        for I in 0 to N-1 loop
            if counter > 0 and counter mod (2 ** (I+1)) = 0 then
                if I = N-1 then
                    counter := 0;
                end if;
                clk_out(I) <= '1';
            else
                clk_out(I) <= '0';
            end if;
        end loop;
        counter := counter + 1;
    end process;

end Behaviour;

