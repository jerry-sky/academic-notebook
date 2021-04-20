library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.numeric_std.ALL;

entity twoway is
	GENERIC (NBit : positive := 8);
    PORT ( clk : in  STD_LOGIC;
           q : out  STD_LOGIC_VECTOR (NBit-1 downto 0)
             := (OTHERS => '0')  -- stan power-on
    );
end twoway;

ARCHITECTURE Behavioral OF twoway IS
    BEGIN
    PROCESS(clk)
        VARIABLE x : UNSIGNED(NBit-1 downto 0) := (others => '0');
        VARIABLE dir: STD_LOGIC := '1';
	BEGIN
        IF (clk'event AND clk='1') THEN
            IF dir = '1' THEN
                x := x+1;
                IF x >= 2 ** NBit - 1 THEN
                    dir := '0';
                END IF;
            ELSE
                x := x-1;
                IF x = 0 THEN
                    dir := '1';
                END IF;
            END IF;
        END IF;
        q <= STD_LOGIC_VECTOR(x);
    END PROCESS;
END Behavioral;

