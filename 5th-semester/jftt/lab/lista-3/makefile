all: ex-1 ex-2

.PHONY: ex-1 ex-2

ex-2:
	echo "#!/bin/bash\n\npython3 ex-2.py\n" > ex-2
	chmod +x ex-2

ex-1: ex-1.l ex-1.y
	bison -o ex-1_y.c -d ex-1.y
	flex -o ex-1_l.c ex-1.l
	gcc -o ex-1 ex-1_y.c ex-1_l.c -lm

clean:
	rm -rf ex-1 ex-2 *.c *.h parser.out parsetab.py __pycache__
