
run:
	ghdl -r $(r)

wave:
	ghdl -r $(r) --wave=$(r).ghw
	gtkwave $(r).ghw

build: hello adder ex4

hello:
	ghdl -a hello.vhdl
	ghdl -e hello_world

adder:
	ghdl -a adder.vhdl
	ghdl -e adder
	ghdl -a adder_tb.vhdl
	ghdl -e adder_tb

ex4:
	ghdl -a ex-4.vhdl
	ghdl -e ex4
	ghdl -a ex-4_tb.vhdl
	ghdl -e ex4_tb

clean:
	rm -f *.cf *.ghw
