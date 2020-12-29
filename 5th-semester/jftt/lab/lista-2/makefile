all: ex-1.o ex-2.o ex-3.o ex-4.o

ex-1.o:
	flex -oex-1.c ex-1.l
	gcc -oex-1.o ex-1.c

ex-2.o:
	flex -oex-2.c ex-2.l
	gcc -oex-2.o ex-2.c

ex-3.o:
	flex -oex-3.c ex-3.l
	gcc -oex-3.o ex-3.c

ex-4.o:
	flex -oex-4.c ex-4.l
	gcc -oex-4.o ex-4.c -lm

clean:
	rm -rf *.o *.c
