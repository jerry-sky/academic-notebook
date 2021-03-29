
run:
	ghdl -r $(r)

wave:
	ghdl -r $(r) --wave=$(r).ghw
	gtkwave $(r).ghw

build: lab2_gates example Xand ex5

lab2_gates:
	ghdl -a lab2-gates.vhd
	ghdl -e gateAND
	ghdl -e gateNOT
	ghdl -e gateXOR
	ghdl -e gateOR

example:
	ghdl -a example.vhd
	ghdl -e example
	ghdl -a example_tb.vhd
	ghdl -e example_tb

Xand:
	ghdl -a Xand.vhd
	ghdl -e Xand
	ghdl -a Xand_tb.vhd
	ghdl -e Xand_tb

ex5:
	ghdl -a ex5.vhd
	ghdl -e ex5
	ghdl -a ex5_tb.vhd
	ghdl -e ex5_tb

clean:
	rm -f *.cf *.ghw
