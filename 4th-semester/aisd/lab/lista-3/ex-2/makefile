Flags = -B .

main.out: random-generator.out
	g++ $(Flags) main.cpp -o main.out $^

random-generator.out:
	g++ $(Flags) -c random-generator.cpp -o random-generator.out

clean:
	rm -rf *.out
