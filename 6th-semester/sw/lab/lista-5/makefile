
run:
	ghdl -r $(r)

wave: wave-quiet
	gtkwave $(r).ghw

wave-quiet:
	ghdl -r $(r) --wave=$(r).ghw

build: clock_divider

clock_divider:
	ghdl -a clock_divider.vhd
	ghdl -e clock_divider
	ghdl -a clock_exp_divider.vhd
	ghdl -e clock_exp_divider
	ghdl -a clock_divider_tb.vhd
	ghdl -e clock_divider_tb

clean:
	rm -f *.cf *.ghw *.o *.gch
