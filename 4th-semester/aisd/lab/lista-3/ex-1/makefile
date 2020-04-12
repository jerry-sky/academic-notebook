Flags = -B .

main.out: ex-1.out ex-2.out algorithms.out sort.out swap-and-compare.out sort-direction.out quick-sort.out insertion-sort.out merge-sort.out dual-pivot-quick-sort.out radix-sort.out
	g++ $(Flags) main.cpp -o main.out $^

ex-1.out:
	g++ $(Flags) -c ex-1.cpp -o ex-1.out

ex-2.out:
	g++ $(Flags) -c ex-2.cpp -o ex-2.out

sort-direction.out:
	g++ $(Flags) -c shared/sort-direction.cpp -o sort-direction.out

swap-and-compare.out:
	g++ $(Flags) -c shared/swap-and-compare.cpp -o swap-and-compare.out

sort.out:
	g++ $(Flags) -c shared/algorithms/sort.cpp -o sort.out

quick-sort.out:
	g++ $(Flags) -c shared/algorithms/quick-sort.cpp -o quick-sort.out

insertion-sort.out:
	g++ $(Flags) -c shared/algorithms/insertion-sort.cpp -o insertion-sort.out

merge-sort.out:
	g++ $(Flags) -c shared/algorithms/merge-sort.cpp -o merge-sort.out

dual-pivot-quick-sort.out:
	g++ $(Flags) -c shared/algorithms/dual-pivot-quick-sort.cpp -o dual-pivot-quick-sort.out

radix-sort.out:
	g++ $(Flags) -c shared/algorithms/radix-sort.cpp -o radix-sort.out

algorithms.out:
	g++ $(Flags) -c shared/algorithms.cpp -o algorithms.out

clean:
	rm -rf *.out
