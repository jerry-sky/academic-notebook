Flags = -B .

all: select.out selection-algorithm.out swap-and-compare.out sort-direction.out randomized-select.out random-generator.out
	g++ $(Flags) main.cpp -o main.out $^

selection-algorithm.out:
	g++ $(Flags) -c algorithms/selection-algorithm.cpp -o selection-algorithm.out

sort-direction.out:
	g++ $(Flags) -c algorithms/sort-direction.cpp -o sort-direction.out

swap-and-compare.out:
	g++ $(Flags) -c algorithms/swap-and-compare.cpp -o swap-and-compare.out

select.out:
	g++ $(Flags) -c algorithms/select.cpp -o select.out

randomized-select.out:
	g++ $(Flags) -c algorithms/randomized-select.cpp -o randomized-select.out

random-generator.out:
	g++ $(Flags) -c random-generator.cpp -o random-generator.out

clean:
	rm -rf *.out
