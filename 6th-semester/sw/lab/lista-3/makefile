
run:
	ghdl -r $(r)

wave: wave-quiet
	gtkwave $(r).ghw

wave-quiet:
	ghdl -r $(r) --wave=$(r).ghw

build: simple twoway lfsr

simple:
	ghdl -a simple.vhd
	ghdl -e simple
	ghdl -a simple_tb.vhd
	ghdl -e simple_tb

twoway:
	ghdl -a twoway.vhd
	ghdl -e twoway
	ghdl -a twoway_tb.vhd
	ghdl -e twoway_tb

lfsr:
	ghdl -a lfsr.vhd
	ghdl -e lfsr
	ghdl -a lfsr_tb.vhd
	ghdl -e lfsr_tb

lfsr-c.o:
	gcc -c shift_lfsr.c
	gcc -c lfsr.c
	gcc -o main.o shift_lfsr.o lfsr.o

_lfsr-generator:
	lfsr-generator --length=16 --shift-amounts=1 --taps=16,15,14,5 --shift-left > shift_lfsr.c

clean:
	rm -f *.cf *.ghw *.o *.gch
