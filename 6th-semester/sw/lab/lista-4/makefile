
run:
	ghdl -r $(r)

wave: wave-quiet
	gtkwave $(r).ghw

wave-quiet:
	ghdl -r $(r) --wave=$(r).ghw

build: rom pack crc8

crc8:
	ghdl -a crc8.vhd
	ghdl -e crc8
	ghdl -a crc8_tb.vhd
	ghdl -e crc8_tb

pack:
	ghdl -a pack.vhd

rom:
	ghdl -a rom.vhd
	ghdl -e rom_for_crc8

clean:
	rm -f *.cf *.ghw *.o *.gch
