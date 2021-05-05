--
-- implementacja sumy kontrolnej sCRC8 (HEC)
-- na podstawie Majewski, Zbysinski "Uklady FPGA w przykladach"
--
library IEEE;
use IEEE.STD_LOGIC_1164.all;

package pack is

    function nextCRC (
        data		: std_logic_vector(7 downto 0);
        prevCRC 	: std_logic_vector(7 downto 0)
    ) return std_logic_vector;

end pack;

package body pack is

    function nextCRC (
        data		: std_logic_vector(7 downto 0);
        prevCRC 	: std_logic_vector(7 downto 0)
    ) return std_logic_vector is

        variable D	      : std_logic_vector(7 downto 0);
        variable C	      : std_logic_vector(7 downto 0);
        variable newCRC   : std_logic_vector(7 downto 0);

    begin
        D := data;
        C := prevCRC;

        newCRC(0) := D(7) xor D(6) xor D(0) xor C(0) xor C(6) xor C(7);
        newCRC(1) := D(6) xor D(1) xor D(0) xor C(0) xor C(1) xor C(6);
        newCRC(2) := D(6) xor D(2) xor D(1) xor D(0) xor C(0) xor C(1)
                                                     xor C(2) xor C(6);
        newCRC(3) := D(7) xor D(3) xor D(2) xor D(1) xor C(1) xor C(2)
                                                     xor C(3) xor C(7);
        newCRC(4) := D(4) xor D(3) xor D(2) xor C(2) xor C(3) xor C(4);
        newCRC(5) := D(5) xor D(4) xor D(3) xor C(3) xor C(4) xor C(5);
        newCRC(6) := D(6) xor D(5) xor D(4) xor C(4) xor C(5) xor C(6);
        newCRC(7) := D(7) xor D(6) xor D(5) xor C(5) xor C(6) xor C(7);

        return newCRC;
    end nextCRC;

end pack;
