
.PHONY: external.o main.bin

build: node.o external.o main.bin

main.bin:
	gnatmake main.adb -o main.bin

external.o:
	gnatmake -c external.ads

node.o:
	gnatmake node.adb

randint.o:
	gnatmake randint.adb

clean:
	rm -rf *.ali *.o *.bin
