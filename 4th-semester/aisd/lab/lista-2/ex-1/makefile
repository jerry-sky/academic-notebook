all: main

main: main.main.out sort-direction.out sort.out swap-and-compare.out
	g++ -o main.out main.main.out sort-direction.out sort.out swap-and-compare.out

main.main.out:
	g++ -c main.cpp -o main.main.out

sort-direction.out:
	g++ -c sort-direction.cpp -o sort-direction.out

sort.out:
	g++ -c sort.cpp -o sort.out

swap-and-compare.out:
	g++ -c swap-and-compare.cpp -o swap-and-compare.out

clean:
	rm -r main *.out
