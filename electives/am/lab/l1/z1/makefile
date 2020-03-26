
all: happy-cat.out norm.out sum-squared.out sum.out generate-neighbourhood.out
	g++ main.cpp -o main $^

happy-cat.out:
	g++ -c happy-cat.cpp -o happy-cat.out

norm.out:
	g++ -c norm.cpp -o norm.out

sum-squared.out:
	g++ -c sum-squared.cpp -o sum-squared.out

sum.out:
	g++ -c sum.cpp -o sum.out

generate-neighbourhood.out:
	g++ -c generate-neighbourhood.cpp -o generate-neighbourhood.out

clean:
	rm -rf *.out main
