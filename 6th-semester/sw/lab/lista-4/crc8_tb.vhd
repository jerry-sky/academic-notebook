LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
use ieee.numeric_std.all;
use work.pack.all;

ENTITY crc8_tb IS
END crc8_tb;

ARCHITECTURE behavior OF crc8_tb IS
    -- main component counting CRC sums
    COMPONENT crc8
    PORT(
         clk : IN  std_logic;
         data_in : IN  std_logic_vector(7 downto 0);
         crc_out : OUT  std_logic_vector(7 downto 0)
        );
    END COMPONENT;
     -- component delcaration for ROM look-up
     component rom_for_crc8
    Port ( address  : in  STD_LOGIC_VECTOR (2 downto 0);
           data_out : out  STD_LOGIC_VECTOR (7 downto 0)
            );
     end component;

    -- clock stuff
   signal clk : std_logic := '0';
   -- clock period
   constant clk_period : time := 20 ns;

    -- CRC generator data
    -- input
   signal data_in_one : std_logic_vector(7 downto 0) := (others => '0');
   signal data_in_two : std_logic_vector(7 downto 0) := (others => '0');
   -- output
   signal crc_out_one : std_logic_vector(7 downto 0);
   signal crc_out_two : std_logic_vector(7 downto 0);

    -- ROM
   -- output data
    signal data_out_a0 : std_logic_vector(7 downto 0);
    signal data_out_66 : std_logic_vector(7 downto 0);
    -- access address
    signal address : std_logic_vector(2 downto 0) := (others => '0');

    signal stopp: std_logic := '0';

BEGIN
     -- Instantiate the Unit Under Test (UUT)
    uut_one: crc8 PORT MAP (
        clk => clk,
        data_in => data_in_one,
        crc_out => crc_out_one
    );

    uut_two: crc8 PORT MAP (
        clk => clk,
        data_in => data_in_two,
        crc_out => crc_out_two
    );

     -- instance of ROM lookup for constant X"a0" input
    rom_a0 : entity work.rom_for_crc8(const_a0)
    port map (
        address => address,
        data_out => data_out_a0
    );
    -- instance of ROM lookup for constant X"66" input
    rom_66 : entity work.rom_for_crc8(const_66)
    port map (
        address => address,
        data_out => data_out_66
    );

   -- Clock process definitions
    clk_process :process
        variable wait_done : natural := 0;
    begin
        -- if wait_done = 0
        -- then
        --     wait for clk_period * 1;
        --     wait_done := 1;
        -- end if;
        if stopp = '1'
        then
            wait;
        end if;
        clk <= '1';
        wait for clk_period/2;
        clk <= '0';
        wait for clk_period/2;
    end process;


   -- Stimulus process
   stim_proc: process
   begin
        -- input your code here
        -- wait for 100 ns;

        data_in_one <= X"a0";
        data_in_two <= X"66";

        for I in 0 to 7 loop
            address <= std_logic_vector(to_unsigned(I, address'length));
            wait for clk_period/2;
            assert crc_out_one = data_out_a0
                report "invalid CRC for a0" severity error;
            assert crc_out_two = data_out_66
                report "invalid CRC for 66" severity error;
            wait for clk_period/2;
        end loop;

        stopp <= '1';

      wait;
   end process;

END;
