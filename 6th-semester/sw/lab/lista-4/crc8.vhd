--
-- implementacja sumy kontrolnej sCRC8 (HEC)
-- na podstawie Majewski, Zbysinski "Uklady FPGA w przykladach"
--
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use work.pack.all;

entity crc8 is
    Port ( clk : in  STD_LOGIC;
           data_in : in  STD_LOGIC_VECTOR (7 downto 0);
           crc_out : out  STD_LOGIC_VECTOR (7 downto 0));
end crc8;

architecture Behavioral of crc8 is
    signal newCRC : std_logic_vector(7 downto 0) := (others => '0');
begin

    process (clk, data_in, newCRC)
    begin
        if clk = '1' and rising_edge(clk) then
            newCRC <= nextCRC(data_in, newCRC);
        else
            null;
        end if;
    end process;

    crc_out <= newCRC;

end Behavioral;

